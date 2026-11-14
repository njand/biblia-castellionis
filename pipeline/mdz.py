"""The 1573 Basel edition (Perna; MDZ bsb10141277): hOCR pages → text and word boxes, and page-image crops.

The hOCR pages are cached in sources/mdz-1573/<canvas>.hocr (canvas 0747–0960 hold the New Testament). A page
has two text columns with marginal notes (scripture references, short summaries) outside them, Castellio's
annotations in full-width blocks, a running head and column numbers at the top. Pages are read in the hOCR's
block order; the narrow blocks (marginal notes) are dropped. A note the OCR ran into a text line stays.

Images come from the IIIF image service (`crop_url`); Git Bash curl fails TLS to MDZ here, so `fetch_crop` uses
PowerShell's Invoke-WebRequest. Crops are cached in sources/mdz-1573/crops/."""

import collections
import difflib
import html
import re
import subprocess
from dataclasses import dataclass

from pipeline import align, paths

FOLDER = paths.SOURCES / "mdz-1573"
CROPS = FOLDER / "crops"
NT = range(747, 961)
IMAGE = "https://api.digitale-sammlungen.de/iiif/image/v2/bsb10141277_{canvas:05d}/{x},{y},{w},{h}/{width},/0/default.jpg"
HOCR_URL = "https://api.digitale-sammlungen.de/ocr/bsb10141277/{canvas}"

LINE = re.compile(r'<span class=[\'"]ocr_line[\'"] title=[\'"]bbox ([\d ]+)[^\'"]*[\'"]>(.*?)</span>\s*(?=<span class=[\'"]ocr_line|</p)', re.S)
BLOCK = re.compile(r'<div class=[\'"]ocrx_block[\'"] title=[\'"]bbox ([\d ]+)[^\'"]*[\'"]>(.*?)</div>', re.S)
WORD = re.compile(r'<span class=[\'"]ocrx_word[\'"] title=[\'"]bbox ([\d ]+)[^\'"]*[\'"]>([^<]*)</span>')


@dataclass(frozen=True)
class Word:
    canvas: int
    text: str
    box: tuple          # (x0, y0, x1, y1)
    column: int         # 0 left half of the page, 1 right
    line: int           # line number on the page, in reading order


def page_words(canvas, source=None):
    """[Word] of one page in the hOCR's reading order, without the narrow blocks of marginal notes."""
    if source is None:
        path = FOLDER / f"{canvas:04d}.hocr"
        if not path.exists():
            return []
        source = path.read_text(encoding="utf-8", errors="ignore")
    page = re.search(r"ocr_page[^>]*bbox (\d+) (\d+) (\d+) (\d+)", source)
    width = int(page.group(3)) if page else 2500
    out, n = [], 0
    for bbox, body in BLOCK.findall(source):
        x0, y0, x1, y1 = map(int, bbox.split()[:4])
        if x1 - x0 < 0.15 * width:
            continue                                     # a marginal note (scripture reference, summary)
        column = 0 if (x0 + x1) / 2 < width / 2 else 1
        for _, line in LINE.findall(body):
            words = [Word(canvas, html.unescape(t), tuple(map(int, b.split()[:4])), column, n) for b, t in WORD.findall(line)]
            if words:
                out.extend(words)
                n += 1
    return out


# The OCR reads a capital I before a lower-case letter as l in the commonest names (lesus, lohannes, lacobus).
CAPITAL_I = re.compile(r"\bl(?=e[sfſ][uv]|oh|acob|sra|ord[ai]|erosol|erusal|ud[æę]|udae|udas?\b|udam\b)")   # ludæi, ludas
# It reads the nasal bar over a final u or e (horũ, itẽ) as an acute: horú, ité. Castellio's print marks adverbs
# with a grave (verò, quàm), so a final acute is taken as the bar (align.clean expands ũ → um).
NASAL = re.compile(r"(?<=\w)[úé](?=\W|$)")


def page_text(words):
    """Plain text of a page's words, one line per OCR line (lesus read as Iesus, horú as horũ)."""
    lines, current, key = [], [], None
    for word in words:
        if key is not None and (word.column, word.line) != key and current:
            lines.append(" ".join(current))
            current = []
        key = (word.column, word.line)
        current.append(word.text)
    if current:
        lines.append(" ".join(current))
    text = CAPITAL_I.sub("I", "\n".join(lines))
    return NASAL.sub(lambda m: {"ú": "ũ", "é": "ẽ"}[m.group()], text)


def nt_pages():
    """[(canvas, [Word])] of the New Testament pages that are cached."""
    return [(canvas, words) for canvas in NT if (words := page_words(canvas))]


def witness(pages=None):
    """An anchored align.Witness of the 1573 NT, with `canvas_at`: the canvas of each token."""
    pages = nt_pages() if pages is None else pages
    text, canvases = [], []
    for canvas, words in pages:
        page = page_text(words)
        text.append(page)
        canvases.append((canvas, len(align.words(align.clean(page)))))
    w = align.Witness("\n".join(text), anchors=True)
    # Tokens per page, as cleaned page by page; hyphens joined across a page break shift this by a token at most.
    w.canvas_at = []
    for canvas, count in canvases:
        w.canvas_at.extend([canvas] * count)
    w.canvas_at.extend([canvases[-1][0]] * max(0, len(w.tokens) - len(w.canvas_at)))
    return w


# ---------------------------------------------------------------- finding a word on the page, and its image

def find(canvases, context, target_index):
    """The Word on these canvases that best fits `context` (words of the verse around the one wanted, which is
    context[target_index]): a word like it, with as many of the other context words nearby as can be found."""
    words = [w for c in canvases for w in page_words(c)]
    folded = [align.fold(w.text, fs=True) for w in words]
    want = [align.fold(w, fs=True) for w in context]
    like = lambda a, b: a == b or difflib.SequenceMatcher(None, a, b).ratio() >= 0.75
    best, best_score = None, 0.0
    for j, f in enumerate(folded):
        score = difflib.SequenceMatcher(None, f, want[target_index]).ratio()
        for k, w in enumerate(want):
            if k == target_index:
                continue
            expected = j + (k - target_index)
            near = range(max(0, expected - 3), min(len(folded), expected + 4))
            score += any(like(folded[n], w) for n in near)
        if score > best_score:
            best, best_score = words[j], score
    return best


def line_box(word, above=1, below=1):
    """The box of the word's line on its page, with `above` lines before and `below` after."""
    words = page_words(word.canvas)
    lines = [w for w in words if word.line - above <= w.line <= word.line + below and w.column == word.column]
    own = [w for w in lines if w.line == word.line]
    x0 = min(w.box[0] for w in own)
    x1 = max(w.box[2] for w in own)
    return (x0, min(w.box[1] for w in lines), x1, max(w.box[3] for w in lines))


def crop_url(word, width=1000, above=15):
    """The IIIF URL of the word's line, with the lines above and below, the full width of its column; `above` more
    pixels over the top (a column's head, where the OCR can miss a carried-over line: 1 Tim 1:10 *contrarium est*)."""
    x0, y0, x1, y1 = line_box(word)
    x0, y0 = max(0, x0 - 60), max(0, y0 - above)
    return IMAGE.format(canvas=word.canvas, x=x0, y=y0, w=x1 - x0 + 120, h=y1 - y0 + 30, width=width)


def carried_over(word):
    """The first Word of the column that continues the text, when `word` sits on its column's last line (a verse
    carried over to the head of the next column, or of the next page's first column: 1 Tim 1:10 *contrarium est*);
    else None."""
    def text_lines(canvas, column):
        """[(top, [Word])] of a column's text lines, top to bottom: not the full-width annotations below the columns
        (the hOCR numbers lines in its block order, not the page's), the running head or column numbers."""
        words = page_words(canvas)
        if not words:
            return []
        left, right = min(w.box[0] for w in words), max(w.box[2] for w in words)
        middle, slack = (left + right) / 2, 0.04 * (right - left)
        lines = collections.defaultdict(list)
        for w in words:
            lines[(w.column, w.line)].append(w)
        out = []
        for (col, _), ws in lines.items():
            x0, x1 = min(w.box[0] for w in ws), max(w.box[2] for w in ws)
            inside = x1 < middle + slack if col == 0 else x0 > middle - slack     # not a centred heading or note
            if col == column and inside and any(c.islower() for w in ws for c in w.text):
                out.append((min(w.box[1] for w in ws), sorted(ws, key=lambda w: w.box[0])))
        return sorted(out, key=lambda t: t[0])

    # A page can hold two zones of columns, above and below Castellio's annotations (canvas 909: 1 Tim 1, the notes,
    # then chapter 2), so a column "ends" wherever the next line of the same column is more than GAP below.
    GAP = 100
    own = text_lines(word.canvas, word.column)
    at = next((i for i, (_, ws) in enumerate(own) if word in ws), None)
    if at is None or (at + 1 < len(own) and own[at + 1][0] - own[at][0] <= GAP):
        return None
    zone_top = own[at][0]
    for i in range(at, 0, -1):                           # up to the first line of this zone
        if own[i][0] - own[i - 1][0] > GAP:
            break
        zone_top = own[i - 1][0]
    if word.column == 0:                                  # the same zone's right column
        following = [t for t in text_lines(word.canvas, 1) if t[0] >= zone_top - GAP / 2]
    else:                                                 # the next zone's left column, or the next page's
        following = [t for t in text_lines(word.canvas, 0) if t[0] > own[at][0] + GAP] \
            or text_lines(word.canvas + 1, 0)
    return following[0][1][0] if following else None


def _download(url, path):
    subprocess.run(["powershell", "-NoProfile", "-Command",
                    f"Invoke-WebRequest -UseBasicParsing -Uri '{url}' -OutFile '{path}'"], check=True,
                   capture_output=True)


def fetch_crop(word, name):
    """Download the crop around a word (cached) and return its path. When the word is on its column's last line, the
    next column's first lines are saved too, as `<name>+next.jpg` beside it (a crop is one rectangle)."""
    CROPS.mkdir(parents=True, exist_ok=True)
    path = CROPS / f"{name}.jpg"
    if not path.exists():
        _download(crop_url(word), path)
    after = carried_over(word)
    if after is not None:
        nxt = CROPS / f"{name}+next.jpg"
        if not nxt.exists():
            _download(crop_url(after, above=140), nxt)
    return path
