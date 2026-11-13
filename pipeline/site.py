"""The website (build/site/): static HTML for GitHub Pages, replacing the 2019 WordPress site.

  index.html                    the books and their chapters
  <slug>/index.html             one book's chapters
  <slug>/<n>.html               a chapter: verse anchors (matthaeus/14.html#3; Pages also serves matthaeus/14#3),
                                a switch to hide the macrons, a light/dark switch, and a menu of the parallel texts
                                at hand (REFERENCES; sources/parallel/<key>/), one shown beside the Latin verse by
                                verse, in the KJV's numbering (parallel.aligned)
  downloads/                    the EPUBs, PDF and text built with the site, listed on index.html#downloads
  search.html, search.json      the search page (words, phrases, or a reference) and every verse's text
  colophon.html                 licence and credits (Wikisource pages and revisions, texts, fonts)
  style.css, app.js, books.js   books.js: the books and chapters, for the jump menu and references
  fonts/                        pipeline/fonts: Gentium Book and Ezra SIL, subset and renamed (OFL)
  .nojekyll

A chapter page also has text-size buttons, a jump menu, a search box, and verse selection: a click on a verse
number selects it (shift-click or "To verse…" a range), puts #3 or #3-7 in the address and offers to copy the link.

`chapter_html` renders a chapter's paragraphs and poetry; the EPUB uses it too. Links are relative, so the site
also reads from the file system."""

import html
import json
import shutil
from dataclasses import dataclass

from pipeline import parallel, paths, publish


@dataclass(frozen=True)
class Reference:
    """A text offered beside the Latin: `texts` names the parallel text (sources/parallel/<key>) per testament."""
    key: str
    short: str            # the menu's label (or {testament: label} where the text differs by testament)
    label: str            # the colophon's
    texts: dict

    def menu(self, testament):
        return self.short.get(testament, "") if isinstance(self.short, dict) else self.short

    def names(self):
        return " / ".join(self.short.values()) if isinstance(self.short, dict) else self.short


REFERENCES = [
    Reference("kjv", "English: KJV (1769)", "the King James Version (Authorized Version, 1611) in the standard text "
              "of 1769", {"vetus": "kjv", "novum": "kjv"}),
    Reference("bsb", "English: BSB", "the Berean Standard Bible", {"vetus": "bsb", "novum": "bsb"}),
    Reference("web", "English: WEB", "the World English Bible", {"vetus": "web", "novum": "web"}),
    Reference("orig", {"vetus": "Hebrew (Masoretic, WLC)", "novum": "Greek (Textus Receptus)"}, "for the Old Testament the Hebrew of the Westminster Leningrad Codex; for the "
              "New the Greek Textus Receptus (Stephanus 1550, the Elzevirs 1624 and Scrivener 1881 collated)",
              {"vetus": "wlc", "novum": "tr"}),
    Reference("lxx", "Septuagint", "the Septuagint in the Greek text of Brenton's edition (1851)", {"vetus": "lxx"}),
    Reference("vulgate", "Vulgate", "the Clementine Vulgate", {"vetus": "vulgate", "novum": "vulgate"}),
]
BY_REF = {ref.key: ref for ref in REFERENCES}
LANG = {"wlc": ("he", "rtl"), "tr": ("grc", "ltr"), "lxx": ("grc", "ltr"), "vulgate": ("la", "ltr")}


def esc(text):
    return html.escape(text, quote=False)


def title_h1(book, filt=lambda text: text):
    """The book's title as an <h1>: one line per \\mt1 part, the \\mt2/\\mt3 lines smaller."""
    lines = "".join(f'<span class="{"mt2" if minor else "mt1"}">{esc(filt(line))}</span>' for line, minor in book.title)
    return f"<h1>{lines}</h1>"


def chapter_html(chapter, verse_id, chapter_id, filt=lambda text: text, verse_link=True):
    """The chapter's paragraphs and poetry as HTML. `verse_id(n)` names a verse's anchor, `chapter_id` the drop
    cap's; `filt` is applied to every piece of text (strip_macrons for the edition without macrons)."""
    out = []
    if chapter.title:
        out.append(f'<p class="d">{esc(filt(chapter.title))}</p>')
    if chapter.summary:
        out.append(f'<p class="argumentum" id="{verse_id(0)}">{esc(filt(chapter.summary))}</p>')
    italic, first = False, True
    poem = []                                   # the lines of the poem being gathered
    notes = []                                  # [(reference, text)]: the chapter's footnotes, listed at its end

    def flush_poem():
        if poem:
            out.append('<div class="poem">' + "".join(poem) + "</div>")
            poem.clear()

    for block in chapter.blocks:
        if block.kind == "b":
            poem.append('<div class="b"></div>')
            continue
        parts = ['<i class="qt">'] if italic else []
        if first:
            parts.append(f'<span class="c" id="{chapter_id}">{chapter.number}</span>')
        for kind, value in block.content:
            if kind == "v":
                if value == 1:
                    parts.append(f'<span id="{verse_id(1)}"></span>')
                elif verse_link:
                    parts.append(f'<a class="v" id="{verse_id(value)}" href="#{verse_id(value)}">{value}</a>')
                else:
                    parts.append(f'<sup class="v" id="{verse_id(value)}">{value}</sup>')
            elif kind == "qt":
                italic = value
                parts.append('<i class="qt">' if value else "</i>")
            elif kind == "note":                # a small letter; the note shows on hover and in the EPUB as a pop-up
                notes.append(value)
                letter = publish.note_letter(len(notes) - 1)
                note_id = f"{chapter_id}-n{letter}"
                parts.append(f'<sup class="fn"><a epub:type="noteref" href="#{note_id}" id="{note_id}-ref" '
                             f'title="{esc(filt(value[1]))}">{letter}</a></sup>')
            else:
                parts.append(esc(filt(value)))
        if italic:
            parts.append("</i>")
        inner = "".join(parts).strip()
        if block.kind.startswith("q"):
            poem.append(f'<div class="{block.kind}">{inner}</div>')
        else:
            flush_poem()
            classes = " ".join(c for c in (block.kind, "first" if first else "") if c)
            out.append(f'<p class="{classes}">{inner}</p>')
        first = False
    flush_poem()
    if chapter.closing:
        out.append(f'<p class="cls">{esc(filt(chapter.closing))}</p>')
    for index, (reference, text) in enumerate(notes):
        letter = publish.note_letter(index)
        note_id = f"{chapter_id}-n{letter}"
        out.append(f'<aside class="fn" epub:type="footnote" id="{note_id}"><p><a href="#{note_id}-ref">{letter}</a> '
                   f'{esc(reference)} {esc(filt(text))}</p></aside>')
    return "\n".join(out)


def segments_html(segments):
    """One verse's pieces (publish.verse_segments) as inline HTML, poetry lines broken with <br/>."""
    out = []
    for text, italic, line_break in segments:
        piece = esc(text)
        if line_break:
            out.append("<br/>")
            piece = piece.lstrip()
        out.append(f'<i class="qt">{piece}</i>' if italic else piece)
    return "".join(out).strip()


# ---------------------------------------------------------------- pages

FONTS = paths.ROOT / "pipeline" / "fonts"     # Gentium Book and Ezra SIL, subset and renamed (OFL; fonts/README)

CSS = """@font-face { font-family: "Castellio Book"; font-style: normal; font-weight: 400; font-display: swap;
  src: url("fonts/castellio-book-regular.woff2") format("woff2"); }
@font-face { font-family: "Castellio Book"; font-style: italic; font-weight: 400; font-display: swap;
  src: url("fonts/castellio-book-italic.woff2") format("woff2"); }
@font-face { font-family: "Castellio Book"; font-style: normal; font-weight: 600; font-display: swap;
  src: url("fonts/castellio-book-semibold.woff2") format("woff2"); }
@font-face { font-family: "Castellio Hebrew"; font-style: normal; font-weight: 400; font-display: swap;
  src: url("fonts/castellio-hebrew.woff2") format("woff2"); }
:root {
  --bg: #fbfaf7; --fg: #1d1b18; --muted: #6f6a62; --rule: #e2ddd3; --accent: #7a2e1f; --panel: #f2efe8;
  --mark: rgba(122, 46, 31, .12);
  --serif: "Castellio Book", "Gentium Book Plus", "Palatino Linotype", Palatino, Georgia, serif;
  --hebrew: "Castellio Hebrew", "SBL Hebrew", "Ezra SIL", "Noto Serif Hebrew", "Times New Roman", serif;
  --scale: 1;
  color-scheme: light;
}
:root[data-theme="dark"] {
  --bg: #191816; --fg: #e8e4dc; --muted: #9c968c; --rule: #34312c; --accent: #e09a7f; --panel: #23211e;
  --mark: rgba(224, 154, 127, .18);
  color-scheme: dark;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #191816; --fg: #e8e4dc; --muted: #9c968c; --rule: #34312c; --accent: #e09a7f; --panel: #23211e;
    --mark: rgba(224, 154, 127, .18);
    color-scheme: dark;
  }
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body { margin: 0; background: var(--bg); color: var(--fg); font-family: var(--serif);
  font-size: calc(19px * var(--scale)); line-height: 1.6; }
a { color: var(--accent); }
header.bar { position: sticky; top: 0; z-index: 2; background: var(--bg); border-bottom: 1px solid var(--rule);
  padding: .45rem 1rem; display: flex; flex-wrap: wrap; gap: .45rem 1rem; align-items: center;
  justify-content: space-between; font-size: 15px; }
header.bar nav a { text-decoration: none; }
header.bar .tools, header.bar .jump { display: flex; flex-wrap: wrap; gap: .4rem; align-items: center; }
.parallel-choice { display: inline-flex; align-items: center; gap: .3rem; }
.parallel-choice label { font-size: 13px; color: var(--muted); }
button, select, input { font: inherit; font-size: 13px; color: var(--fg); background: var(--panel);
  border: 1px solid var(--rule); border-radius: 4px; padding: .2rem .5rem; }
button, select { cursor: pointer; }
input[type="search"] { width: 9.5rem; }
button[aria-pressed="true"], select.on { border-color: var(--accent); color: var(--accent); }
button:focus-visible, select:focus-visible, input:focus-visible, a:focus-visible { outline: 2px solid var(--accent);
  outline-offset: 1px; }
.sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
main { max-width: 38rem; margin: 0 auto; padding: 1.5rem 1rem 3rem; }
main.wide { max-width: 64rem; }
h1 { font-weight: normal; font-variant: small-caps; letter-spacing: .04em; text-align: center; line-height: 1.3;
  margin: 1rem 0 1.5rem; }
h1 span.mt1, h1 span.mt2 { display: block; }
h1 span.mt2 { font-size: .55em; letter-spacing: .06em; }
h1 small { display: block; font-size: .55em; color: var(--muted); font-variant: normal; letter-spacing: 0; }
h1 small.caput { font-variant: small-caps; letter-spacing: .08em; margin-top: .2em; }
h2 { font-weight: normal; font-variant: small-caps; letter-spacing: .04em; margin: 2rem 0 .5rem; }
h2 a { text-decoration: none; }
.chapter p { margin: 0; text-indent: 1.2em; text-align: justify; hyphens: manual; }
.chapter p.first, .chapter p.m, .chapter p.nb, .chapter .poem + p.m { text-indent: 0; }
.chapter p.argumentum { font-style: italic; text-indent: 0; color: var(--muted); margin-bottom: 1rem; }
.chapter p.cls { font-style: italic; text-indent: 0; font-size: .9em; margin-top: 1rem; }
sup.fn { font-size: .6em; line-height: 0; font-style: italic; }
sup.fn a { color: var(--muted); text-decoration: none; padding: 0 .1em; }
aside.fn { font-size: .8em; color: var(--muted); margin: .2rem 0 0; }
aside.fn:first-of-type { border-top: 1px solid currentColor; padding-top: .3rem; margin-top: 1rem; }
aside.fn p { text-indent: 0; margin: 0; }
aside.fn a { font-style: italic; text-decoration: none; color: inherit; }
.chapter p.d { font-style: italic; text-indent: 0; margin-bottom: .5rem; }
.chapter .poem { margin: .45em 0; }
.chapter .q1, .chapter .q2, .chapter .q3 { padding-left: 2em; text-indent: -1em; }
.chapter .q2 { padding-left: 3.5em; }
.chapter .q3 { padding-left: 5em; }
.chapter .b { height: .6em; }
.c { float: left; font-size: 3.3em; line-height: .9; margin: .04em .14em 0 0; color: var(--accent); text-indent: 0; }
@media screen { .chapter .c { display: none; } }      /* the "Caput" heading names the chapter on screen */
.v { font-size: .62em; vertical-align: super; line-height: 0; color: var(--muted); text-decoration: none;
  padding: .2em .15em .2em .2em; cursor: pointer; }
a.v:hover { color: var(--accent); }
:target { scroll-margin-top: 4.5rem; }
.v.sel, td.n.sel { color: var(--accent); font-weight: 600; }
::highlight(verses) { background-color: var(--mark); }
tr.sel td { background: var(--mark); }
.qt { font-style: italic; }
.chapters { display: flex; flex-wrap: wrap; gap: .35rem; padding: 0; list-style: none; }
.chapters a { display: inline-block; min-width: 2.4em; text-align: center; padding: .2em .3em;
  border: 1px solid var(--rule); border-radius: 4px; text-decoration: none; }
.pager { display: flex; justify-content: space-between; margin-top: 2.5rem; font-size: .9rem; }
.pager a { text-decoration: none; }
#verse-bar { position: fixed; left: 50%; bottom: 1rem; transform: translateX(-50%); z-index: 3; display: flex;
  gap: .5rem; align-items: center; padding: .4rem .6rem; background: var(--panel); border: 1px solid var(--rule);
  border-radius: 6px; box-shadow: 0 2px 10px rgba(0, 0, 0, .15); font-size: 14px; max-width: calc(100% - 2rem); }
#verse-bar[hidden] { display: none; }
#verse-bar .hint { color: var(--muted); font-size: 12px; }
#verse-bar .hint:empty { display: none; }
#verse-bar, #verse-bar button { white-space: nowrap; }
table.parallel { border-collapse: collapse; width: 100%; }
table.parallel td { vertical-align: top; padding: .35em .5em; border-top: 1px solid var(--rule); }
table.parallel td.n { color: var(--muted); font-size: .75em; width: 2.5em; text-align: right; padding-top: .7em;
  cursor: pointer; }
table.parallel td.ref { display: none; width: 45%; font-size: .9em; color: var(--muted); }
td.ref[lang="he"] { font-family: var(--hebrew); font-size: 1.05em; line-height: 1.8; text-align: right; }
p.ref-note { display: none; font-size: .8em; color: var(--muted); font-style: italic; }
.parallel-view { display: none; }
body[data-ref] .reading-view { display: none; }
body[data-ref] .parallel-view { display: block; }
body[data-ref] main { max-width: 64rem; }
@SHOWN@
.search form { display: flex; gap: .5rem; margin-bottom: 1rem; }
.search form input { flex: 1; font-size: 16px; padding: .35rem .6rem; width: auto; }
.search form button { font-size: 15px; }
.search .count { color: var(--muted); font-size: .85em; }
.search ol { list-style: none; padding: 0; }
.search li { padding: .5em 0; border-top: 1px solid var(--rule); }
.search li a.ref { font-variant: small-caps; text-decoration: none; margin-right: .5em; }
.search mark { background: var(--mark); color: inherit; border-radius: 2px; }
footer { max-width: 38rem; margin: 0 auto; padding: 1rem 1rem 3rem; font-size: .8rem; color: var(--muted);
  border-top: 1px solid var(--rule); }
.colophon p { margin: .6em 0; }
.colophon ul { padding-left: 1.2em; }
.print-only { display: none; }
.downloads { border: 1px solid var(--rule); border-radius: 6px; padding: .2rem 1rem .7rem; margin: 1.5rem 0 1rem;
  background: var(--panel); font-size: .9rem; }
.downloads h2 { margin: .6rem 0 .4rem; }
.downloads ul { list-style: none; padding: 0; margin: 0; display: grid;
  grid-template-columns: repeat(auto-fill, minmax(14rem, 1fr)); gap: .5rem 1.25rem; }
.downloads li { line-height: 1.45; }
.downloads .what, .downloads .size, .downloads p { color: var(--muted); font-size: .85em; }
.downloads li a { text-decoration: none; }
.downloads .part { font-style: italic; }
.downloads p { margin: .6rem 0 0; }
@media (max-width: 600px) {
  body { font-size: calc(18px * var(--scale)); }
  header.bar { position: static; }
  header.bar { padding: .4rem .75rem; gap: .35rem .5rem; }
  input[type="search"] { width: 6.5rem; }
  #ref { max-width: 7.5rem; }
  #theme .label { display: none; }
  #verse-bar { bottom: .5rem; font-size: 13px; gap: .35rem; }
  .chapter p { text-align: left; }
  table.parallel, table.parallel tbody, table.parallel tr, table.parallel td { display: block; width: auto; }
  table.parallel td.n { width: auto; text-align: left; padding: .5em .5em 0; }
  table.parallel td, table.parallel td.ref { border-top: 0; width: auto; }
  table.parallel tr { border-top: 1px solid var(--rule); }
@SHOWN_MOBILE@
}
@page { margin: 2cm 2.2cm 2.2cm; }
@media print {
  :root, :root[data-theme], :root:not([data-theme="light"]) {
    --bg: #fff; --fg: #000; --muted: #555; --rule: #bbb; --accent: #6b2416; --mark: transparent; color-scheme: light;
  }
  body { font-size: 11.5pt; line-height: 1.45; }
  header.bar, .pager, footer, #verse-bar, .search form { display: none !important; }
  main, body[data-ref] main { max-width: none; padding: 0; }
  h1 { margin: 0 0 1em; break-after: avoid; }
  h1 small.caput { display: none; }                   /* in print, as in the PDF, the large numeral names it */
  h2 { break-after: avoid; }
  .chapter p { orphans: 3; widows: 3; }
  .chapter .poem { break-inside: avoid; }
  a { color: inherit; text-decoration: none; }
  .v { color: var(--muted); }
  .v.sel, td.n.sel { font-weight: normal; color: var(--muted); }
  table.parallel tr { break-inside: avoid; }
  table.parallel td.ref { color: #333; }
  .print-only { display: block; margin-top: 2em; font-size: 9pt; color: var(--muted); text-align: center; }
}
""".replace("@SHOWN@", "\n".join(f'body[data-ref="{ref.key}"] td.ref[data-r="{ref.key}"] {{ display: table-cell; }}\n'
                                f'body[data-ref="{ref.key}"] p.ref-note[data-r="{ref.key}"] {{ display: block; }}'
                                for ref in REFERENCES)).replace(
    "@SHOWN_MOBILE@", "\n".join(f'  body[data-ref="{ref.key}"] td.ref[data-r="{ref.key}"] {{ display: block; }}'
                                for ref in REFERENCES))

# Read before the stylesheet applies, so a chosen theme or text size never flashes the default.
HEAD_SCRIPT = ("<script>try{var t=localStorage.getItem('theme'),s=+localStorage.getItem('size')||0,"
               "e=document.documentElement;if(t==='light'||t==='dark'){e.setAttribute('data-theme',t);}"
               "if(s){e.style.setProperty('--scale',Math.pow(1.1,s).toFixed(3));}}catch(x){}</script>")

JS = """(function () {
  'use strict';
  var store = {
    get: function (key) { try { return window.localStorage.getItem(key); } catch (e) { return null; } },
    set: function (key, value) { try { window.localStorage.setItem(key, value); } catch (e) {} }
  };
  var root = document.documentElement;
  var base = (document.querySelector('script[src$="app.js"]').getAttribute('src') || 'app.js').replace(/app\\.js$/, '');

  // ---------------------------------------------------------------- macrons
  var originals = new WeakMap();
  function strip(text) { return text.normalize('NFD').replace(/\\u0304/g, '').normalize('NFC'); }
  function setMacrons(on) {
    var main = document.querySelector('main');
    // the Latin only: normalizing would reorder the Hebrew points
    var walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT, { acceptNode: function (node) {
      return node.parentElement.closest('.ref') ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT; } });
    for (var node = walker.nextNode(); node; node = walker.nextNode()) {
      if (!originals.has(node)) { originals.set(node, node.data); }
      node.data = on ? originals.get(node) : strip(originals.get(node));
    }
    var button = document.getElementById('macrons');
    if (button) { button.setAttribute('aria-pressed', on ? 'true' : 'false'); }
  }

  // ---------------------------------------------------------------- theme and text size
  var THEMES = ['auto', 'light', 'dark'];
  var LABELS = { auto: '\\u25D0 Auto', light: '\\u2600 Light', dark: '\\u263E Dark' };
  function setTheme(theme) {
    if (theme === 'auto') { root.removeAttribute('data-theme'); } else { root.setAttribute('data-theme', theme); }
    var button = document.getElementById('theme');
    if (button) {
      button.innerHTML = '<span aria-hidden="true">' + LABELS[theme].charAt(0) + '</span><span class="label">' +
        LABELS[theme].slice(1) + '</span>';
      button.title = 'Colours: ' + theme + ' (click to change)';
      button.setAttribute('aria-label', 'Colours: ' + theme);
    }
  }
  var size = Math.max(-2, Math.min(5, +store.get('size') || 0));
  function setSize(step) {
    size = Math.max(-2, Math.min(5, step));
    root.style.setProperty('--scale', Math.pow(1.1, size).toFixed(3));
    store.set('size', String(size));
    var smaller = document.getElementById('smaller'), larger = document.getElementById('larger');
    if (smaller) { smaller.disabled = size <= -2; }
    if (larger) { larger.disabled = size >= 5; }
  }

  // ---------------------------------------------------------------- the text beside the Latin
  var select = document.getElementById('ref');
  function setRef(key) {
    var known = select && Array.prototype.some.call(select.options, function (o) { return o.value === key; });
    if (!known) { key = ''; }
    if (key) { document.body.setAttribute('data-ref', key); } else { document.body.removeAttribute('data-ref'); }
    if (select) { select.value = key; select.classList.toggle('on', !!key); }
  }

  // ---------------------------------------------------------------- jump menu
  var BOOKS = window.CASTELLIO_BOOKS || [];
  var bookSelect = document.getElementById('jump-book'), chapterSelect = document.getElementById('jump-chapter');
  function fillChapters(slug, current) {
    var book = BOOKS.filter(function (b) { return b[0] === slug; })[0];
    chapterSelect.innerHTML = '';
    var blank = document.createElement('option');
    blank.value = ''; blank.textContent = 'Caput';
    chapterSelect.appendChild(blank);
    (book ? book[2] : []).forEach(function (n) {
      var o = document.createElement('option');
      o.value = n; o.textContent = n;
      if (String(n) === String(current)) { o.selected = true; }
      chapterSelect.appendChild(o);
    });
  }
  if (bookSelect && chapterSelect) {
    BOOKS.forEach(function (b) {
      var o = document.createElement('option');
      o.value = b[0]; o.textContent = b[1];
      bookSelect.appendChild(o);
    });
    var here = document.body.getAttribute('data-slug');
    if (here) { bookSelect.value = here; }
    fillChapters(bookSelect.value, document.body.getAttribute('data-chapter'));
    bookSelect.addEventListener('change', function () {
      fillChapters(bookSelect.value);
      var book = BOOKS.filter(function (b) { return b[0] === bookSelect.value; })[0];
      if (book && book[2].length === 1) { location.href = base + book[0] + '/' + book[2][0] + '.html'; }
      else { chapterSelect.focus(); }
    });
    chapterSelect.addEventListener('change', function () {
      if (chapterSelect.value) { location.href = base + bookSelect.value + '/' + chapterSelect.value + '.html'; }
    });
  }

  // ---------------------------------------------------------------- verses: select, highlight, copy a link
  var chapterEl = document.querySelector('.reading-view');
  var bar = document.getElementById('verse-bar');
  var selection = null;            // [first, last]
  function verseNumbers() {
    return Array.prototype.map.call(document.querySelectorAll('.reading-view [id]'), function (el) { return el.id; })
      .filter(function (id) { return /^\\d+$/.test(id); }).map(Number);
  }
  function rangeOf(first, last) {
    var start = document.getElementById(String(first));
    if (!start || !chapterEl) { return null; }
    var range = document.createRange();
    range.setStartBefore(start);
    var after = verseNumbers().filter(function (n) { return n > last; })[0];
    var end = after !== undefined ? document.getElementById(String(after)) : null;
    if (end) { range.setEndBefore(end); } else { range.setEndAfter(chapterEl.lastElementChild || chapterEl); }
    return range;
  }
  function label(first, last) {
    return document.body.getAttribute('data-cite') + ',' + first + (last > first ? '\\u2013' + last : '');
  }
  function show(first, last, scroll) {
    selection = first === null ? null : [Math.min(first, last), Math.max(first, last)];
    document.querySelectorAll('.sel').forEach(function (el) { el.classList.remove('sel'); });
    if (window.CSS && CSS.highlights) { CSS.highlights.delete('verses'); }
    if (!selection) {
      if (bar) { bar.hidden = true; }
      if (/^#\\d+(-\\d+)?$/.test(location.hash)) { history.replaceState(null, '', location.pathname + location.search); }
      return;
    }
    var a = selection[0], b = selection[1];
    for (var n = a; n <= b; n++) {
      var marker = document.getElementById(String(n));
      if (marker) { marker.classList.add('sel'); }
      var row = document.getElementById('p' + n);
      if (row) { row.classList.add('sel'); var cell = row.querySelector('td.n'); if (cell) { cell.classList.add('sel'); } }
    }
    var range = rangeOf(a, b);
    if (range && window.CSS && CSS.highlights && window.Highlight) { CSS.highlights.set('verses', new Highlight(range)); }
    history.replaceState(null, '', '#' + a + (b > a ? '-' + b : ''));
    if (bar) {
      bar.hidden = false;
      bar.querySelector('.where').textContent = label(a, b);
      bar.querySelector('.hint').textContent = '';
      var copy = bar.querySelector('.copy');
      copy.textContent = 'Copy link';
    }
    if (scroll) {
      var target = document.body.hasAttribute('data-ref') ? document.getElementById('p' + a) : document.getElementById(String(a));
      if (target) { target.scrollIntoView({ block: 'center' }); }
    }
  }
  function fromHash(scroll) {
    var m = /^#(\\d+)(?:-(\\d+))?$/.exec(location.hash);
    if (m) { show(+m[1], m[2] ? +m[2] : +m[1], scroll); }
  }
  function copyText(text, done) {
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(done, function () { fallbackCopy(text); done(); });
    } else { fallbackCopy(text); done(); }
  }
  function fallbackCopy(text) {
    var area = document.createElement('textarea');
    area.value = text; area.setAttribute('readonly', ''); area.style.position = 'fixed'; area.style.opacity = '0';
    document.body.appendChild(area); area.select();
    try { document.execCommand('copy'); } catch (e) {}
    document.body.removeChild(area);
  }

  // ---------------------------------------------------------------- start
  var macrons = store.get('macrons') !== 'off';
  var theme = store.get('theme') || 'auto';
  if (THEMES.indexOf(theme) < 0) { theme = 'auto'; }
  if (!macrons) { setMacrons(false); }
  setTheme(theme);
  setSize(size);
  if (select) {
    var ref = store.get('ref');
    if (ref === null && store.get('english') === 'on') { ref = 'bsb'; }   // the earlier English switch
    setRef(ref || '');
    select.addEventListener('change', function () {
      store.set('ref', select.value); setRef(select.value);
      if (selection) { show(selection[0], selection[1], true); }
    });
  }
  if (/^#\\d+(-\\d+)?$/.test(location.hash) && 'scrollRestoration' in history) { history.scrollRestoration = 'manual'; }
  fromHash(true);
  // again once the fonts and the page have settled, which moves the lines
  window.addEventListener('load', function () { if (selection) { show(selection[0], selection[1], true); } });
  window.addEventListener('hashchange', function () { fromHash(true); });

  document.addEventListener('click', function (event) {
    // the button itself, also when the click lands on text inside it (the theme button's spans)
    var target = (event.target.closest && event.target.closest('button')) || event.target;
    if (target.id === 'macrons') { macrons = !macrons; store.set('macrons', macrons ? 'on' : 'off'); setMacrons(macrons); }
    if (target.id === 'theme') {
      theme = THEMES[(THEMES.indexOf(theme) + 1) % THEMES.length]; store.set('theme', theme); setTheme(theme);
    }
    if (target.id === 'smaller') { setSize(size - 1); }
    if (target.id === 'larger') { setSize(size + 1); }
    var number = target.closest && (target.closest('a.v') || target.closest('td.n'));
    if (number && document.getElementById('verse-bar')) {
      var n = number.tagName === 'A' ? +number.id : +number.parentElement.id.slice(1);
      if (!n && n !== 0) { return; }
      event.preventDefault();
      if (event.shiftKey && selection) { show(selection[0], n, false); }
      else if (selection && selection[0] === n && selection[1] === n) { show(null); }
      else if (selection && selection[0] === selection[1] && bar && bar.dataset.extend === 'on') { show(selection[0], n, false); }
      else { show(n, n, false); }
      if (bar) { bar.dataset.extend = 'off'; }
    }
    if (target.classList && target.classList.contains('copy') && selection) {
      copyText(location.href, function () { target.textContent = 'Copied'; });
    }
    if (target.classList && target.classList.contains('extend')) {
      if (bar) { bar.dataset.extend = 'on'; bar.querySelector('.hint').textContent = 'now tap the last verse'; }
    }
    if (target.classList && target.classList.contains('clear')) { show(null); }
  });
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && selection) { show(null); return; }
    if (event.altKey || event.ctrlKey || event.metaKey || /input|textarea|select/i.test(event.target.tagName)) { return; }
    var link = document.querySelector(event.key === 'ArrowLeft' ? 'a[rel=prev]' : event.key === 'ArrowRight' ? 'a[rel=next]' : null);
    if (link) { location.href = link.href; }
  });

  // ---------------------------------------------------------------- the search page
  var results = document.getElementById('results');
  if (results) {
    var input = document.getElementById('q');
    var params = new URLSearchParams(location.search);
    var query = params.get('q') || '';
    input.value = query;
    // a letter for a letter, so a match's place in the folded text is its place in the text
    var fold = function (text) {
      return text.normalize('NFD').replace(/\\u0304/g, '').normalize('NFC').toLowerCase()
        .replace(/j/g, 'i').replace(/v/g, 'u');
    };
    var foldQuery = function (text) {
      return fold(text).replace(/ae/g, '\\u00e6').replace(/oe/g, '\\u0153');
    };
    var escapeHtml = function (s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); };
    if (query.trim()) {
      var reference = /^\\s*(\\d?\\s*[a-z\\u00e6\\u0153\\u0101-\\u017f]+)\\.?\\s*(\\d+)(?:[\\s:,.]+(\\d+)(?:\\s*[-\\u2013]\\s*(\\d+))?)?\\s*$/i.exec(query);
      if (reference) {
        var wanted = foldQuery(reference[1].replace(/\\s+/g, ''));
        var hit = BOOKS.filter(function (b) {
          return b[3].some(function (name) { return foldQuery(name.replace(/\\s+/g, '')).indexOf(wanted) === 0; });
        })[0];
        if (hit && hit[2].indexOf(+reference[2]) >= 0) {
          location.replace(base + hit[0] + '/' + reference[2] + '.html' +
                           (reference[3] ? '#' + reference[3] + (reference[4] ? '-' + reference[4] : '') : ''));
          return;
        }
      }
      results.innerHTML = '<p class="count">Searching\\u2026</p>';
      fetch(base + 'search.json').then(function (r) { return r.json(); }).then(function (verses) {
        var words = foldQuery(query).split(/\\s+/).filter(Boolean);
        var phrase = /^\\s*".+"\\s*$/.test(query) ? [foldQuery(query.replace(/"/g, '').trim())] : words;
        var found = [];
        verses.forEach(function (v) {
          var text = fold(v[2]);
          if (phrase.every(function (w) { return text.indexOf(w) >= 0; })) { found.push(v); }
        });
        var shown = found.slice(0, 300).map(function (v) {
          var text = v[2], folded = fold(text), marks = [];
          phrase.forEach(function (w) {
            for (var at = folded.indexOf(w); at >= 0; at = folded.indexOf(w, at + w.length)) { marks.push([at, at + w.length]); }
          });
          marks.sort(function (x, y) { return x[0] - y[0]; });
          var out = '', last = 0;
          marks.forEach(function (m) {
            if (m[0] < last) { return; }
            out += escapeHtml(text.slice(last, m[0])) + '<mark>' + escapeHtml(text.slice(m[0], m[1])) + '</mark>';
            last = m[1];
          });
          out += escapeHtml(text.slice(last));
          return '<li><a class="ref" href="' + base + v[1] + '">' + escapeHtml(v[0]) + '</a>' + out + '</li>';
        });
        results.innerHTML = '<p class="count">' + found.length + (found.length === 1 ? ' verse' : ' verses') +
          (found.length > 300 ? ' (the first 300 shown)' : '') + '</p><ol>' + shown.join('') + '</ol>';
        if (!macrons) { setMacrons(false); }
      }, function () {
        results.innerHTML = '<p class="count">The search index could not be loaded (it needs the site served over http).</p>';
      });
    }
  }
})();
"""


def page(title, body, root, bar="", tools="", main_class="", description="", data=None):
    """A page; `data` are the body's data-* attributes (data-book, data-slug, data-chapter on a chapter)."""
    attrs = "".join(f' data-{key}="{html.escape(str(value))}"' for key, value in (data or {}).items())
    jump = (f'<form class="jump" action="{root}search.html" role="search">'
            f'<label class="sr" for="jump-book">Book</label><select id="jump-book"><option value="">Liber</option></select>'
            f'<label class="sr" for="jump-chapter">Chapter</label><select id="jump-chapter"></select>'
            f'<label class="sr" for="search-q">Search</label>'
            f'<input type="search" id="search-q" name="q" placeholder="Quærere…" title="Words, or a reference: Mt 5,3"/>'
            f'</form>')
    return f"""<!DOCTYPE html>
<html lang="la">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{esc(title)}</title>
<meta name="description" content="{html.escape(description or publish.SERIES)}"/>
{HEAD_SCRIPT}
<link rel="preload" href="{root}fonts/castellio-book-regular.woff2" as="font" type="font/woff2" crossorigin/>
<link rel="stylesheet" href="{root}style.css"/>
</head>
<body{attrs}>
<header class="bar"><nav><a href="{root}index.html">Biblia Sacra</a>{bar}</nav>{jump}<div class="tools">{tools}<button type="button" id="smaller" title="Smaller text" aria-label="Smaller text">A−</button><button type="button" id="larger" title="Larger text" aria-label="Larger text">A+</button><button type="button" id="macrons" aria-pressed="true" title="Macrons on or off">ā / a</button><button type="button" id="theme" title="Colours">◐ Auto</button></div></header>
<main class="{main_class}">
{body}
</main>
<footer>{f'<a href="{root}index.html#downloads">Downloads (EPUB, PDF, text)</a> · ' if HAS_DOWNLOADS else ''}<a href="{root}colophon.html">Colophon, licence and credits</a> · CC BY-SA 4.0 · <a href="{publish.REPOSITORY}">{publish.REPOSITORY.removeprefix('https://')}</a></footer>
<script src="{root}books.js"></script>
<script src="{root}app.js"></script>
</body>
</html>
"""


VERSE_BAR = ('<div id="verse-bar" hidden role="status"><span class="where"></span>'
             '<button type="button" class="copy">Copy link</button>'
             '<button type="button" class="extend" title="Select a range: then tap the last verse (or shift-click it)">'
             'To verse…</button><button type="button" class="clear" aria-label="Clear the selection">×</button>'
             '<span class="hint"></span></div>')


def chapter_grid(book, prefix=""):
    links = "".join(f'<li><a href="{prefix}{c.number}.html">{c.number}</a></li>' for c in book.chapters)
    return f'<ul class="chapters">{links}</ul>'


def load_references(keys, book, sources):
    """[(Reference, parallel key, {kjv id: text}, {chapter: note})] of the texts offered beside this book: those at
    hand whose numbering has been checked against the KJV for it (parallel.aligned)."""
    out = []
    for key in keys:
        ref = BY_REF[key]
        text_key = ref.texts.get(book.info.testament)
        found = parallel.aligned(text_key, book.info.osis, sources) if text_key else None
        if found and found[0]:
            out.append((ref, text_key, *found))
    return out


def parallel_html(book, chapter, refs):
    notes = "".join(f'<p class="ref-note" data-r="{ref.key}" lang="en">{esc(gaps[chapter.number])}</p>'
                    for ref, _, _, gaps in refs if chapter.number in gaps)
    rows = []
    for number, segments in publish.verse_segments(chapter).items():
        vid = f"{book.info.osis}.{chapter.number}.{number}"
        cells = []
        for ref, text_key, verses, _ in refs:
            lang, direction = LANG.get(text_key, ("en", "ltr"))
            dir_attr = f' dir="{direction}"' if direction == "rtl" else ""
            cells.append(f'<td class="ref" data-r="{ref.key}" lang="{lang}"{dir_attr}>{esc(verses.get(vid, ""))}</td>')
        rows.append(f'<tr id="p{number}"><td class="n">{number or ""}</td><td class="la">{segments_html(segments)}'
                    f'</td>{"".join(cells)}</tr>')
    return notes + '<table class="parallel">\n' + "\n".join(rows) + "\n</table>"


# Names a reader may type for a book in the search box (besides the Latin short title and the OSIS code).
ENGLISH_NAMES = {
    "Gen": ["Genesis", "Gn"], "Exod": ["Exodus", "Ex"], "Lev": ["Leviticus", "Lv"], "Num": ["Numbers", "Nm"],
    "Deut": ["Deuteronomy", "Dt"], "Josh": ["Joshua", "Jos"], "Judg": ["Judges", "Jdg"], "Ruth": ["Ruth"],
    "1Sam": ["1 Samuel", "1Sm"], "2Sam": ["2 Samuel", "2Sm"], "1Kgs": ["1 Kings", "1Ki"], "2Kgs": ["2 Kings", "2Ki"],
    "1Chr": ["1 Chronicles"], "2Chr": ["2 Chronicles"], "Ezra": ["Ezra"], "Neh": ["Nehemiah"], "Esth": ["Esther"],
    "Job": ["Job"], "Ps": ["Psalms", "Psalm"], "Prov": ["Proverbs"], "Eccl": ["Ecclesiastes", "Qoheleth"],
    "Song": ["Song of Songs", "Canticles"], "Isa": ["Isaiah", "Is"], "Jer": ["Jeremiah"], "Lam": ["Lamentations"],
    "Ezek": ["Ezekiel"], "Dan": ["Daniel"], "Hos": ["Hosea"], "Joel": ["Joel"], "Amos": ["Amos"], "Obad": ["Obadiah"],
    "Jonah": ["Jonah"], "Mic": ["Micah"], "Nah": ["Nahum"], "Hab": ["Habakkuk"], "Zeph": ["Zephaniah"],
    "Hag": ["Haggai"], "Zech": ["Zechariah"], "Mal": ["Malachi"], "Matt": ["Matthew", "Mt"], "Mark": ["Mark", "Mk"],
    "Luke": ["Luke", "Lk"], "John": ["John", "Jn"], "Acts": ["Acts"], "Rom": ["Romans", "Rm"],
    "1Cor": ["1 Corinthians", "1Co"], "2Cor": ["2 Corinthians", "2Co"], "Gal": ["Galatians"],
    "Eph": ["Ephesians"], "Phil": ["Philippians"], "Col": ["Colossians"], "1Thess": ["1 Thessalonians"],
    "2Thess": ["2 Thessalonians"], "1Tim": ["1 Timothy"], "2Tim": ["2 Timothy"], "Titus": ["Titus"],
    "Phlm": ["Philemon"], "Heb": ["Hebrews"], "Jas": ["James"], "1Pet": ["1 Peter"], "2Pet": ["2 Peter"],
    "1John": ["1 John"], "2John": ["2 John"], "3John": ["3 John"], "Jude": ["Jude"], "Rev": ["Revelation", "Apocalypse"],
}


def books_js(selected):
    """window.CASTELLIO_BOOKS: [[slug, short title, [chapters], [names to search by]], …] for the jump menu."""
    rows = [[book.slug, book.short, [c.number for c in book.chapters],
             [book.short, publish.strip_macrons(book.short), publish.CITATION.get(book.info.osis, book.info.osis),
              book.info.osis, *ENGLISH_NAMES.get(book.info.osis, [])]]
            for book in selected]
    return "window.CASTELLIO_BOOKS = " + json.dumps(rows, ensure_ascii=False, separators=(",", ":")) + ";\n"


def search_index(selected):
    """[[reference, link, text], …] of every verse (verse 0: the summary or title) for the search page."""
    out = []
    for book in selected:
        for chapter in book.chapters:
            for number, segments in publish.verse_segments(chapter).items():
                text = " ".join(" ".join(piece for piece, _, _ in segments).split())
                where = publish.cite(book.info.osis, chapter.number, number)
                out.append([where, f"{book.slug}/{chapter.number}.html#{number or 1}", text])
    return json.dumps(out, ensure_ascii=False, separators=(",", ":"))


SEARCH = """<h1>Quærere<small>Search the Latin</small></h1>
<div class="search" lang="en">
<form action="search.html" role="search"><label class="sr" for="q">Search</label>
<input type="search" id="q" name="q" placeholder="Words, &quot;a phrase&quot;, or a reference (Mt 5,3)" autofocus/>
<button type="submit">Search</button></form>
<p class="count">Every word must appear in the verse; macrons, æ/ae, œ/oe, j/i and v/u do not matter. Put a phrase in
quotation marks. A reference (<i>Gn 1,3</i>, <i>Mt 5,3-12</i>, <i>2Cor 2</i>, <i>Lūcās 2</i>; English names too) opens the passage.</p>
<div id="results"></div>
</div>"""


HAS_DOWNLOADS = False           # set by write: whether the footer links to the downloads

# The home page's downloads, a row per format: (format, what it is for, [(end of the file name, link label)]).
# The stem of the names varies with the books built; a plain ending (".epub") passes over the -sine-macronibus files.
DOWNLOADS = [
    ("EPUB", "for e-readers and phones", [(".epub", "with macrons"), ("-sine-macronibus.epub", "without")]),
    ("PDF", "A5, to read on a screen or print", [(".pdf", "PDF")]),
    ("Plain text", "", [(".txt", "with macrons"), ("-sine-macronibus.txt", "without")]),
    ("Data", "one row per verse", [(".tsv", "TSV"), (".json", "JSON")]),
]


def downloads_html(files, parts=((None, None),)):
    """The home page's list of the files in downloads/: [(name, bytes)]. A format with no file built is left out.
    `parts` are the [(label, file stem)] built: a line each under every format when there are several (the whole
    Bible, the Old Testament, the New); a stem of None takes any file with the format's ending."""
    if not files:
        return ""

    def find(stem, end):
        if stem is not None:
            return next(((name, size) for name, size in files if name == stem + end), None)
        plain = not end.startswith("-")
        return next(((name, size) for name, size in files
                     if name.endswith(end) and not (plain and "-sine-macronibus" in name)), None)

    rows = []
    for kind, what, variants in DOWNLOADS:
        lines = []
        for label, stem in parts:
            links = [f'<a href="downloads/{html.escape(found[0])}" download>{esc(variant)}</a> '
                     f'<span class="size">{found[1] / 1_000_000:.1f} MB</span>'
                     for end, variant in variants if (found := find(stem, end))]
            if links:
                lines.append((f'<span class="part">{esc(label)}:</span> ' if label else "") + " · ".join(links))
        if lines:
            note = f' <span class="what">{esc(what)}</span>' if what else ""
            rows.append(f'<li><b>{esc(kind)}</b>{note}<br/>{"<br/>".join(lines)}</li>')
    return (f'<section class="downloads" id="downloads" lang="en"><h2>Downloads</h2><ul>{"".join(rows)}</ul>'
            f'<p>Made from the same text as these pages, and updated with them. Dated editions: '
            f'<a href="{publish.REPOSITORY}/releases">releases</a>.</p></section>\n')


def write(selected, folder, title, version, references=tuple(BY_REF), sources=None, downloads=(),
          parts=((None, None),)):
    """Write the site; returns [folder, messages…]. `references` are the keys of REFERENCES to offer;
    `downloads` the files built with it (EPUB, PDF, text), copied to downloads/ and listed on the home page, by
    `parts` ([(label, file stem)], as downloads_html)."""
    global HAS_DOWNLOADS
    if folder.exists():
        shutil.rmtree(folder)
    folder.mkdir(parents=True)
    files = []
    if downloads:
        (folder / "downloads").mkdir()
        for path in downloads:
            shutil.copy2(path, folder / "downloads" / path.name)
            files.append((path.name, path.stat().st_size))
    HAS_DOWNLOADS = bool(files)
    (folder / "style.css").write_text(CSS, encoding="utf-8", newline="\n")
    (folder / "app.js").write_text(JS, encoding="utf-8", newline="\n")
    (folder / "books.js").write_text(books_js(selected), encoding="utf-8", newline="\n")
    (folder / "search.json").write_text(search_index(selected), encoding="utf-8", newline="\n")
    (folder / ".nojekyll").write_text("", encoding="utf-8")
    shutil.copytree(FONTS, folder / "fonts")
    references = tuple(references or ())
    notes, used, loaded = [], {}, {}
    order = [(book, chapter) for book in selected for chapter in book.chapters]
    for index, (book, chapter) in enumerate(order):
        if book.info.osis not in loaded:
            loaded[book.info.osis] = load_references(references, book, sources)
            offered = {ref.key for ref, *_ in loaded[book.info.osis]}
            for key in references:
                if key not in offered and BY_REF[key].texts.get(book.info.testament):
                    notes.append(f"{key}: not offered for {book.info.osis} (not under sources/parallel, or its "
                                 f"numbering not checked in data/versification/<key>.map.tsv)")
        refs = loaded[book.info.osis]
        for ref, text_key, *_ in refs:
            used.setdefault(ref.key, set()).add(text_key)
        pager = []
        if index:
            prev_book, prev = order[index - 1]
            href = f"{prev.number}.html" if prev_book is book else f"../{prev_book.slug}/{prev.number}.html"
            pager.append(f'<a rel="prev" href="{href}">← {esc(publish.cite(prev_book.info.osis, prev.number))}</a>')
        else:
            pager.append("<span></span>")
        if index + 1 < len(order):
            next_book, nxt = order[index + 1]
            href = f"{nxt.number}.html" if next_book is book else f"../{next_book.slug}/{nxt.number}.html"
            pager.append(f'<a rel="next" href="{href}">{esc(publish.cite(next_book.info.osis, nxt.number))} →</a>')
        body = [f'<h1>{esc(book.short)}<small class="caput">Caput {chapter.number}</small></h1>',
                '<div class="chapter reading-view">',
                chapter_html(chapter, str, "c"), "</div>"]
        tools = ""
        if refs:
            body += ['<div class="chapter parallel-view">', parallel_html(book, chapter, refs), "</div>"]
            options = "".join(f'<option value="{ref.key}">{esc(ref.menu(book.info.testament))}</option>'
                              for ref, *_ in refs)
            tools = (f'<span class="parallel-choice"><label for="ref">Parallel:</label>'
                     f'<select id="ref" title="A text shown beside this one, verse by verse">'
                     f'<option value="">None</option>{options}</select></span>')
        body.append(f'<nav class="pager">{"".join(pager)}</nav>')
        body.append(f'<p class="print-only">{esc(book.long)}, caput {chapter.number} · Biblia Sacra ex Sēbastiānī '
                    f'Castelliōnis interpretātiōne{f" ({esc(version)})" if version else ""} · '
                    f'{publish.REPOSITORY.removeprefix("https://")}</p>')
        body.append(VERSE_BAR)
        bar = f' › <a href="index.html">{esc(book.short)}</a> › Caput {chapter.number}'
        out = folder / book.slug / f"{chapter.number}.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(f"{publish.cite(book.info.osis, chapter.number)} · {book.short} · Biblia Sacra (Castellio)", "\n".join(body), "../",
                            bar, tools, description=f"{book.long}, caput {chapter.number}",
                            data={"book": book.short, "slug": book.slug, "chapter": chapter.number,
                                  "cite": publish.cite(book.info.osis, chapter.number)}),
                       encoding="utf-8", newline="\n")
    for book in selected:
        body = f'{title_h1(book)}\n{chapter_grid(book)}'
        (folder / book.slug / "index.html").write_text(
            page(f"{book.short} · Biblia Sacra (Castellio)", body, "../", f" › {esc(book.short)}",
                 data={"slug": book.slug}),
            encoding="utf-8", newline="\n")
    sections = "\n".join(f'<h2><a href="{book.slug}/index.html">{esc(book.long)}</a></h2>\n'
                         f'{chapter_grid(book, book.slug + "/")}' for book in selected)
    edition = f"<br/><small>{esc(version)}</small>" if version else ""
    home = (f"<h1>Biblia Sacra<small>ex Sēbastiānī Castelliōnis interpretātiōne</small></h1>\n"
            f'<p style="text-align:center">{esc(title)}{edition}</p>\n{downloads_html(files, parts)}{sections}')
    (folder / "index.html").write_text(page("Biblia Sacra ex Sebastiani Castellionis interpretatione", home, ""),
                                       encoding="utf-8", newline="\n")
    (folder / "search.html").write_text(page("Quærere · Biblia Sacra (Castellio)", SEARCH, "", " › Quærere"),
                                        encoding="utf-8", newline="\n")
    (folder / "colophon.html").write_text(
        page("Colophon · Biblia Sacra (Castellio)", colophon_html(selected, used), "", " › Colophon",
             main_class="colophon"), encoding="utf-8", newline="\n")
    return [folder, *notes]


def colophon_html(selected, used=None):
    """`used`: {reference key: {parallel keys shown}} (from write); credits each text offered beside the Latin."""
    info = publish.credits(selected)
    pages = "".join(f'<li>{esc(short)}: <a href="{url}">{esc(url.rsplit("/", 1)[-1].replace("_", " "))}</a>, '
                    f'<a href="{oldid}">revision {revid}</a> (fetched {fetched})</li>'
                    for short, url, revid, oldid, fetched in info["pages"])
    parallels = ""
    if used:
        items = "".join(f"<li>{esc(ref.names())}: {esc(ref.label)}.</li>" for ref in REFERENCES if ref.key in used)
        mapped = any(key in ("wlc", "lxx") for keys in used.values() for key in keys)
        oshb = (', for the Hebrew and the Septuagint by the verse map of the <a href="https://hb.openscriptures.org">'
                'Open Scriptures Hebrew Bible</a> (CC BY 4.0)') if mapped else ""
        parallels = (f'<p>Beside the Latin, verse by verse, the reader may show one of these texts, all in the public '
                     f'domain, as published by <a href="https://ebible.org">eBible.org</a>:</p><ul>{items}</ul>'
                     f'<p>They are shown in the verse numbering of the King James Version, which this edition '
                     f'follows; where a text numbers its verses otherwise, they are moved to the KJV’s numbers '
                     f'(<code>data/versification/</code> in the repository){oshb}. A passage that cannot be matched '
                     f'verse by verse is left out, with a note.</p>')
    fonts = ('<p>Type: Gentium Book (SIL) for the Latin, Greek and English, and Ezra SIL for the Hebrew, both under '
             'the <a href="https://openfontlicense.org">SIL Open Font License 1.1</a>, reduced to the letters used here '
             'and so renamed <i>Castellio Book</i> and <i>Castellio Hebrew</i> as the licence asks.</p>')
    return f"""<h1>Colophon</h1>
<div lang="la">
<p>{esc(info["about"])}</p>
<p>{esc(info["bases"])}</p>
<p>{esc(info["edited"])}</p>
<p>{esc(info["licence"])} <a href="{info["licence_url"]}">{info["licence_url"]}</a></p>
<p>{esc(info["wikisource"]).replace(info["wikisource_name"], f'<a href="{info["wikisource_url"]}">{info["wikisource_name"]}</a>', 1)}</p>
</div>
<div lang="en">
<p>Wikisource pages and revisions used:</p>
<ul>{pages}</ul>
{parallels}
{fonts}
<p>Source files, data, downloads (PDF, EPUB, plain text) and corrections: <a href="{info["repository"]}">{info["repository"]}</a>.</p>
</div>"""
