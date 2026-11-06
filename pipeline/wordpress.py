"""The 2019 WordPress edition (https://bibliasacracastellionis.wordpress.com/) → one verse TSV per book.

Macronized, one verse per paragraph ("6. Admīrātus eōrum īnfīdentiam…"), KJV versification, older spelling
(ae, coepit) and no quotation marks. Used as a witness of earlier macron decisions.
Rows: `id  text  flags`, flags as in pipeline.wikisource (joined, gap, repeat)."""

import html
import re

from pipeline import net, paths, tsv, wikisource
from pipeline.books import Book

SITE = "https://bibliasacracastellionis.wordpress.com"
SOURCE = "wordpress"

PARAGRAPH = re.compile(r"<p[^>]*>(.*?)</p>", re.DOTALL)
VERSE = re.compile(r"^(\d{1,3})\.?\s+(.*)$", re.DOTALL)     # "36. Dīcēbat…", and sometimes "36 Dīcēbat…"


def chapter_numbers(index_html, slug):
    return sorted({int(n) for n in re.findall(rf'href="{re.escape(SITE)}/{re.escape(slug)}-(\d+)/"', index_html)})


def content(page_html):
    """The post body: between the entry-content div and the share buttons."""
    start = page_html.find('class="entry-content')
    if start < 0:
        return ""
    end = page_html.find('class="sharedaddy', start)
    return page_html[start:end if end > 0 else None]


def parse_chapter(page_html, osis, chapter):
    rows, verse = [], None
    for paragraph in PARAGRAPH.findall(content(page_html)):
        text = re.sub(r"<[^>]+>", "", paragraph)
        text = re.sub(r"\s+", " ", html.unescape(text).replace(" ", " ")).strip()
        if not text:
            continue
        match = VERSE.match(text)
        if match:
            number, text = int(match.group(1)), match.group(2)
            if number > (verse or 0) + 1:
                flags = {"gap"}
            else:
                flags = {"repeat"} if verse is not None and number <= verse else set()
            verse = number
            rows.append([tsv.verse_id(osis, chapter, number), "", flags])
        elif rows:
            rows[-1][2].add("joined")
        else:
            rows.append([tsv.verse_id(osis, chapter, 0), "", set()])
        # Some paragraphs hold two verses ("… jejūnābunt. 36 Dīcēbat …").
        pieces = wikisource.split_inline(text, (verse or 0) + 1)
        rows[-1][1] = f"{rows[-1][1]} {pieces[0][1]}".strip()
        for number, piece in pieces[1:]:
            verse = number
            rows.append([tsv.verse_id(osis, chapter, number), piece, {"split"}])
    return [(vid, text, ",".join(sorted(flags))) for vid, text, flags in rows]


def fetch(book: Book, refresh=False):
    """Download every chapter page (cached in sources/wordpress/) and write data/witnesses/wordpress/<osis>.tsv.
    Returns the rows, or None if the site has no such book."""
    if not book.wp:
        return None
    cache = paths.SOURCES / SOURCE / book.osis
    index = net.download(f"{SITE}/{book.wp}/", cache / "index.html", refresh).read_text(encoding="utf-8")
    rows = []
    for chapter in chapter_numbers(index, book.wp):
        page = net.download(f"{SITE}/{book.wp}-{chapter}/", cache / f"{chapter:03d}.html", refresh)
        rows += parse_chapter(page.read_text(encoding="utf-8"), book.osis, chapter)
    tsv.write(paths.WITNESSES / SOURCE / f"{book.osis}.tsv", rows, header=("id", "text", "flags"))
    return rows
