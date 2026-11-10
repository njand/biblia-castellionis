"""The website (build/site/): static HTML for GitHub Pages, replacing the 2019 WordPress site.

  index.html                    the books and their chapters
  <slug>/index.html             one book's chapters
  <slug>/<n>.html               a chapter: verse anchors (matthaeus/14.html#3; Pages also serves matthaeus/14#3),
                                a switch to hide the macrons, and, where the parallel text is at hand, an English
                                column beside the Latin, verse by verse (BSB by default; sources/parallel/<key>/)
  colophon.html                 licence and credits (Wikisource pages and revisions)
  style.css, app.js, .nojekyll

`chapter_html` renders a chapter's paragraphs and poetry; the EPUB uses it too. Links are relative, so the site
also reads from the file system."""

import html
import shutil

from pipeline import paths, publish, tsv

ENGLISH = {"bsb": "Berean Standard Bible (BSB), public domain", "kjv": "King James Version (KJV), public domain",
           "web": "World English Bible (WEB), public domain"}


def esc(text):
    return html.escape(text, quote=False)


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

CSS = """:root {
  --bg: #fbfaf7; --fg: #1d1b18; --muted: #6f6a62; --rule: #e2ddd3; --accent: #7a2e1f; --panel: #f2efe8;
  --serif: "Palatino Linotype", Palatino, "Book Antiqua", "URW Palladio L", Georgia, serif;
}
@media (prefers-color-scheme: dark) {
  :root { --bg: #191816; --fg: #e8e4dc; --muted: #9c968c; --rule: #34312c; --accent: #e09a7f; --panel: #23211e; }
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body { margin: 0; background: var(--bg); color: var(--fg); font-family: var(--serif); font-size: 19px;
  line-height: 1.6; }
a { color: var(--accent); }
header.bar { border-bottom: 1px solid var(--rule); padding: .5rem 1rem; display: flex; flex-wrap: wrap;
  gap: .5rem 1rem; align-items: center; justify-content: space-between; font-size: .85rem; }
header.bar nav a { text-decoration: none; }
header.bar .tools { display: flex; gap: .5rem; }
button { font: inherit; font-size: .8rem; color: var(--fg); background: var(--panel); border: 1px solid var(--rule);
  border-radius: 4px; padding: .2rem .6rem; cursor: pointer; }
button[aria-pressed="true"] { border-color: var(--accent); color: var(--accent); }
main { max-width: 38rem; margin: 0 auto; padding: 1.5rem 1rem 3rem; }
main.wide { max-width: 64rem; }
h1 { font-weight: normal; font-variant: small-caps; letter-spacing: .04em; text-align: center; line-height: 1.3;
  margin: 1rem 0 1.5rem; }
h1 small { display: block; font-size: .55em; color: var(--muted); font-variant: normal; letter-spacing: 0; }
h2 { font-weight: normal; font-variant: small-caps; letter-spacing: .04em; margin: 2rem 0 .5rem; }
h2 a { text-decoration: none; }
.chapter p { margin: 0; text-indent: 1.2em; text-align: justify; hyphens: manual; }
.chapter p.first, .chapter p.m, .chapter p.nb, .chapter .poem + p.m { text-indent: 0; }
.chapter p.argumentum { font-style: italic; text-indent: 0; color: var(--muted); margin-bottom: 1rem; }
.chapter p.d { font-style: italic; text-indent: 0; margin-bottom: .5rem; }
.chapter .poem { margin: .45em 0; }
.chapter .q1, .chapter .q2, .chapter .q3 { padding-left: 2em; text-indent: -1em; }
.chapter .q2 { padding-left: 3.5em; }
.chapter .q3 { padding-left: 5em; }
.chapter .b { height: .6em; }
.c { float: left; font-size: 3.3em; line-height: .9; margin: .04em .14em 0 0; color: var(--accent); text-indent: 0; }
.v { font-size: .62em; vertical-align: super; line-height: 0; color: var(--muted); text-decoration: none;
  padding: 0 .1em 0 .15em; }
a.v:hover { color: var(--accent); }
:target { scroll-margin-top: 4rem; }
a.v:target { color: var(--accent); font-weight: bold; }
.qt { font-style: italic; }
.chapters { display: flex; flex-wrap: wrap; gap: .35rem; padding: 0; list-style: none; }
.chapters a { display: inline-block; min-width: 2.4em; text-align: center; padding: .2em .3em;
  border: 1px solid var(--rule); border-radius: 4px; text-decoration: none; }
.pager { display: flex; justify-content: space-between; margin-top: 2.5rem; font-size: .9rem; }
.pager a { text-decoration: none; }
table.parallel { border-collapse: collapse; width: 100%; }
table.parallel td { vertical-align: top; padding: .35em .5em; border-top: 1px solid var(--rule); }
table.parallel td.n { color: var(--muted); font-size: .75em; width: 2.5em; text-align: right; padding-top: .7em; }
table.parallel td.en { font-family: Georgia, serif; font-size: .9em; color: var(--muted); width: 45%; }
.parallel-view { display: none; }
body.english .reading-view { display: none; }
body.english .parallel-view { display: block; }
body.english main { max-width: 64rem; }
footer { max-width: 38rem; margin: 0 auto; padding: 1rem 1rem 3rem; font-size: .8rem; color: var(--muted);
  border-top: 1px solid var(--rule); }
.colophon p { margin: .6em 0; }
.colophon ul { padding-left: 1.2em; }
@media (max-width: 600px) {
  body { font-size: 18px; }
  .chapter p { text-align: left; }
  table.parallel, table.parallel tbody, table.parallel tr, table.parallel td { display: block; width: auto; }
  table.parallel td.n { text-align: left; padding: .5em .5em 0; }
  table.parallel td { border-top: 0; }
  table.parallel tr { border-top: 1px solid var(--rule); }
}
"""

JS = """(function () {
  'use strict';
  var store = {
    get: function (key) { try { return window.localStorage.getItem(key); } catch (e) { return null; } },
    set: function (key, value) { try { window.localStorage.setItem(key, value); } catch (e) {} }
  };
  var originals = new WeakMap();
  function strip(text) { return text.normalize('NFD').replace(/\\u0304/g, '').normalize('NFC'); }
  function setMacrons(on) {
    var main = document.querySelector('main');
    var walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT);
    for (var node = walker.nextNode(); node; node = walker.nextNode()) {
      if (!originals.has(node)) { originals.set(node, node.data); }
      node.data = on ? originals.get(node) : strip(originals.get(node));
    }
    var button = document.getElementById('macrons');
    if (button) { button.setAttribute('aria-pressed', on ? 'true' : 'false'); }
  }
  function setEnglish(on) {
    document.body.classList.toggle('english', on);
    var button = document.getElementById('english');
    if (button) { button.setAttribute('aria-pressed', on ? 'true' : 'false'); }
  }
  var macrons = store.get('macrons') !== 'off';
  var english = store.get('english') === 'on';
  if (!macrons) { setMacrons(false); }
  if (english && document.getElementById('english')) {
    setEnglish(true);
    if (location.hash) {
      var row = document.getElementById('p' + location.hash.slice(1));
      if (row) { row.scrollIntoView(); }
    }
  }
  document.addEventListener('click', function (event) {
    var target = event.target;
    if (target.id === 'macrons') { macrons = !macrons; store.set('macrons', macrons ? 'on' : 'off'); setMacrons(macrons); }
    if (target.id === 'english') { english = !english; store.set('english', english ? 'on' : 'off'); setEnglish(english); }
  });
  document.addEventListener('keydown', function (event) {
    if (event.altKey || event.ctrlKey || event.metaKey || /input|textarea/i.test(event.target.tagName)) { return; }
    var link = document.querySelector(event.key === 'ArrowLeft' ? 'a[rel=prev]' : event.key === 'ArrowRight' ? 'a[rel=next]' : null);
    if (link) { location.href = link.href; }
  });
})();
"""


def page(title, body, root, bar="", tools="", main_class="", description=""):
    return f"""<!DOCTYPE html>
<html lang="la">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{esc(title)}</title>
<meta name="description" content="{html.escape(description or publish.SERIES)}"/>
<link rel="stylesheet" href="{root}style.css"/>
</head>
<body>
<header class="bar"><nav><a href="{root}index.html">Biblia Sacra</a>{bar}</nav><div class="tools">{tools}<button type="button" id="macrons" aria-pressed="true" title="Macrons on or off">ā / a</button></div></header>
<main class="{main_class}">
{body}
</main>
<footer><a href="{root}colophon.html">Colophon, licence and credits</a> · CC BY-SA 4.0 · <a href="{publish.REPOSITORY}">{publish.REPOSITORY.removeprefix('https://')}</a></footer>
<script src="{root}app.js"></script>
</body>
</html>
"""


def chapter_grid(book, prefix=""):
    links = "".join(f'<li><a href="{prefix}{c.number}.html">{c.number}</a></li>' for c in book.chapters)
    return f'<ul class="chapters">{links}</ul>'


def load_english(key, osis, sources):
    """{id: text} of a parallel English text, or {} when it is not at hand."""
    if not key:
        return {}
    path = (sources or paths.SOURCES) / "parallel" / key / f"{osis}.tsv"
    if not path.exists():
        return {}
    return {row["id"]: row["text"] for row in tsv.read(path)}


def parallel_html(book, chapter, english):
    rows = []
    for number, segments in publish.verse_segments(chapter).items():
        vid = f"{book.info.osis}.{chapter.number}.{number}"
        rows.append(f'<tr id="p{number}"><td class="n">{number or ""}</td><td class="la">{segments_html(segments)}'
                    f'</td><td class="en" lang="en">{esc(english.get(vid, ""))}</td></tr>')
    return '<table class="parallel">\n' + "\n".join(rows) + "\n</table>"


def write(selected, folder, title, version, english_key="bsb", sources=None):
    """Write the site; returns [folder, messages…]."""
    if folder.exists():
        shutil.rmtree(folder)
    folder.mkdir(parents=True)
    (folder / "style.css").write_text(CSS, encoding="utf-8", newline="\n")
    (folder / "app.js").write_text(JS, encoding="utf-8", newline="\n")
    (folder / ".nojekyll").write_text("", encoding="utf-8")
    notes, used_english = [], False
    order = [(book, chapter) for book in selected for chapter in book.chapters]
    for index, (book, chapter) in enumerate(order):
        english = load_english(english_key, book.info.osis, sources)
        used_english = used_english or bool(english)
        if english_key and not english and chapter.number == 1:
            notes.append(f"no {english_key} text for {book.info.osis} under sources/parallel: no English column")
        pager = []
        if index:
            prev_book, prev = order[index - 1]
            href = f"{prev.number}.html" if prev_book is book else f"../{prev_book.slug}/{prev.number}.html"
            pager.append(f'<a rel="prev" href="{href}">← {esc(prev_book.short)} {prev.number}</a>')
        else:
            pager.append("<span></span>")
        if index + 1 < len(order):
            next_book, nxt = order[index + 1]
            href = f"{nxt.number}.html" if next_book is book else f"../{next_book.slug}/{nxt.number}.html"
            pager.append(f'<a rel="next" href="{href}">{esc(next_book.short)} {nxt.number} →</a>')
        body = [f"<h1>{esc(book.short)} {chapter.number}</h1>",
                '<div class="chapter reading-view">',
                chapter_html(chapter, str, "c"), "</div>"]
        tools = ""
        if english:
            body += ['<div class="chapter parallel-view">', parallel_html(book, chapter, english), "</div>"]
            tools = '<button type="button" id="english" aria-pressed="false" title="English column">English</button>'
        body.append(f'<nav class="pager">{"".join(pager)}</nav>')
        bar = f' › <a href="index.html">{esc(book.short)}</a> › {chapter.number}'
        out = folder / book.slug / f"{chapter.number}.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(f"{book.short} {chapter.number} · Biblia Sacra (Castellio)", "\n".join(body), "../",
                            bar, tools, description=f"{book.long}, caput {chapter.number}"),
                       encoding="utf-8", newline="\n")
    for book in selected:
        body = f'<h1>{"<br/>".join(esc(line) for line in book.title)}</h1>\n{chapter_grid(book)}'
        (folder / book.slug / "index.html").write_text(
            page(f"{book.short} · Biblia Sacra (Castellio)", body, "../", f" › {esc(book.short)}"),
            encoding="utf-8", newline="\n")
    sections = "\n".join(f'<h2><a href="{book.slug}/index.html">{esc(book.long)}</a></h2>\n'
                         f'{chapter_grid(book, book.slug + "/")}' for book in selected)
    edition = f"<br/><small>{esc(version)}</small>" if version else ""
    home = (f"<h1>Biblia Sacra<small>ex Sebastiānī Castelliōnis interpretātiōne</small></h1>\n"
            f'<p style="text-align:center">{esc(title)}{edition}</p>\n{sections}')
    (folder / "index.html").write_text(page("Biblia Sacra ex Sebastiani Castellionis interpretatione", home, ""),
                                       encoding="utf-8", newline="\n")
    (folder / "colophon.html").write_text(
        page("Colophon · Biblia Sacra (Castellio)", colophon_html(selected, english_key if used_english else None),
             "", " › Colophon", main_class="colophon"), encoding="utf-8", newline="\n")
    return [folder, *notes]


def colophon_html(selected, english_key=None):
    info = publish.credits(selected)
    pages = "".join(f'<li>{esc(short)}: <a href="{url}">{esc(url.rsplit("/", 1)[-1].replace("_", " "))}</a>, '
                    f'<a href="{oldid}">revision {revid}</a> (fetched {fetched})</li>'
                    for short, url, revid, oldid, fetched in info["pages"])
    english = (f"<p lang=\"en\">The English column is the {esc(ENGLISH.get(english_key, english_key))}, "
               f"shown verse by verse for reference.</p>") if english_key else ""
    return f"""<h1>Colophon</h1>
<div lang="en">
<p>{esc(info["about"])}</p>
<p>{esc(info["bases"])}</p>
<p>{esc(info["licence"])} <a href="{info["licence_url"]}">{info["licence_url"]}</a></p>
<p>{esc(info["wikisource"]).replace("Latin Wikisource", f'<a href="{info["wikisource_url"]}">Latin Wikisource</a>')}</p>
<ul>{pages}</ul>
{english}
<p>Source files, data, downloads (PDF, EPUB, plain text) and corrections: <a href="{info["repository"]}">{info["repository"]}</a>.</p>
</div>"""
