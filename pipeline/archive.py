"""Scans of Castellio editions on archive.org: OCR text, page numbers and (optionally) hOCR word boxes.

Each witness is one edition. Two items hold several editions, so a witness picks its files by a substring of
the file name. Downloads go to sources/archive/<key>/ as text.txt, page_numbers.json and hocr.html (hOCR is
14–40 MB per volume, so only with --hocr). Page images are fetched later, a page at a time, when a reading
needs checking; the jp2 zips are ~1 GB each and are never downloaded whole."""

import json
import os
import urllib.parse
from dataclasses import dataclass

from pipeline import net, paths, tsv

DOWNLOAD = "https://archive.org/download"
METADATA = "https://archive.org/metadata"


@dataclass(frozen=True)
class Witness:
    key: str
    year: int
    scope: str            # "OT", "NT" or "Bible"
    item: str
    match: str            # substring that picks this edition's files within the item ("" = all)
    note: str = ""


WITNESSES = [
    Witness("1738", 1738, "OT", "bibliasacraexseb01cast", "",
            "Leipzig, vol. 1; Wikisource's Old Testament source; ABBYY OCR"),
    Witness("1750", 1750, "Bible", "biblia-sacra-ex-sebastiani-castellionis-interpretatione-eivsqve-postrema-1750",
            "Evvlgata 1750", "Tesseract OCR, noisy"),
    Witness("1715", 1715, "NT", "biblia-sacra-ex-sebastiani-castellionis-interpretatione-eivsqve-postrema-1750",
            "Bibliorum 1715", "Tesseract OCR"),
    Witness("1747", 1747, "NT", "novvm-testamentvm-latinvm-sebastiano-castellione-interprete-ex-eivsdem-postrema-castigatione-1747",
            "Germanica 1747", "with Gesner's essay; Tesseract OCR, noisy"),
    Witness("1681", 1681, "NT", "ned-kbn-all-00001225-001", "",
            "Koninklijke Bibliotheek; ABBYY OCR"),
    Witness("1758-1", 1758, "NT", "bim_eighteenth-century_novum-testamentum-ex-seb_1758_1", "",
            "vol. 1 (Matthew–John?); Tesseract OCR with long s, good"),
    Witness("1758-2", 1758, "NT", "bim_eighteenth-century_novum-testamentum-ex-seb_1758_2", "",
            "vol. 2; Tesseract OCR with long s, good"),
]

BY_KEY = {witness.key: witness for witness in WITNESSES}

FILES = {"_djvu.txt": "text.txt", "_page_numbers.json": "page_numbers.json", "_hocr.html": "hocr.html"}


def base_name(witness: Witness, metadata):
    """The file-name stem shared by this edition's derivative files (`<stem>_djvu.txt`, …)."""
    stems = [f["name"][: -len("_djvu.txt")] for f in metadata["files"] if f["name"].endswith("_djvu.txt")]
    stems = [stem for stem in stems if witness.match in stem]
    if len(stems) != 1:
        raise SystemExit(f"archive: expected one OCR file for {witness.key} in {witness.item}, found {stems}")
    return stems[0]


def fetch(witness: Witness, hocr=False, refresh=False):
    """Download one witness's files. Returns a manifest row."""
    folder = paths.SOURCES / "archive" / witness.key
    meta_path = net.download(f"{METADATA}/{witness.item}", folder / "metadata.json", refresh)
    metadata = json.loads(meta_path.read_text(encoding="utf-8"))
    stem = base_name(witness, metadata)
    for suffix, local in FILES.items():
        if suffix == "_hocr.html" and not hocr:
            continue
        url = f"{DOWNLOAD}/{witness.item}/" + urllib.parse.quote(stem + suffix)
        net.download(url, folder / local, refresh)
    info = metadata.get("metadata", {})
    # Items holding several editions have no single imagecount; count this edition's pages instead.
    pages = json.loads((folder / "page_numbers.json").read_text(encoding="utf-8")).get("pages", [])
    return (witness.key, witness.year, witness.scope, witness.item, stem,
            info.get("ocr", ""), len(pages) or info.get("imagecount", ""),
            f"https://archive.org/details/{witness.item}", witness.note)


def write_manifest(rows):
    tsv.write(paths.WITNESSES / "archive.tsv", rows,
              header=("key", "year", "scope", "item", "file_stem", "ocr", "pages", "url", "note"))


# ---------------------------------------------------------------- word boxes and page-image crops (hOCR)

CROPS = paths.SOURCES / "archive" / "crops"
PAGE_IMAGE = "https://archive.org/download/{item}/page/n{leaf}.jpg"
_PAGES = {}


def pages(key):
    """[(leaf index, [mdz.Word], (page width, page height))] of an edition's hOCR (sources/archive/<key>/hocr.html),
    words in reading order with their page line; cached per run."""
    import re
    from pipeline import mdz
    if key in _PAGES:
        return _PAGES[key]
    text = (paths.SOURCES / "archive" / key / "hocr.html").read_text(encoding="utf-8")
    out = []
    for n, page in enumerate(re.split(r'<div class="ocr_page"', text)[1:]):
        size = re.search(r'bbox 0 0 (\d+) (\d+)', page[:300])
        words, line = [], 0
        for chunk in re.split(r'<span class="ocr_line"', page)[1:]:
            line += 1
            for m in re.finditer(r'class="ocrx_word"[^>]*title="bbox (\d+) (\d+) (\d+) (\d+)[^"]*">([^<]*)<', chunk):
                x0, y0, x1, y1 = map(int, m.groups()[:4])
                words.append(mdz.Word(n, m.group(5).strip(), (x0, y0, x1, y1), 0, line))
        out.append((n, words, (int(size.group(1)), int(size.group(2))) if size else (0, 0)))
    _PAGES[key] = out
    return out


def find(key, context, target_index, leaves=None):
    """The Word that best fits `context` (as mdz.find), on the given leaves or anywhere: pages are first narrowed to
    words like the target, so a whole volume can be searched."""
    import difflib
    from pipeline import align
    want = [align.fold(w, fs=True) for w in context]
    best, best_score = None, 0.0
    for leaf, words, _ in pages(key):
        if leaves is not None and leaf not in leaves:
            continue
        folded = [align.fold(w.text, fs=True) for w in words]
        for j, f in enumerate(folded):
            score = difflib.SequenceMatcher(None, f, want[target_index]).ratio()
            if score < 0.7:
                continue
            for k, w in enumerate(want):
                if k == target_index:
                    continue
                expected = j + (k - target_index)
                score += any(folded[n] == w or difflib.SequenceMatcher(None, folded[n], w).ratio() >= 0.75
                             for n in range(max(0, expected - 3), min(len(folded), expected + 4)))
            if score > best_score:
                best, best_score = words[j], score
    return best


def fetch_crop(key, word, name):
    """The word's line with a line above and below, cut from archive.org's page image (archive.org's IIIF crops
    time out; the page is downloaded and cropped with Windows' System.Drawing through PowerShell, the standard
    library having no JPEG codec). Pages and crops are cached in sources/archive/crops/."""
    import subprocess
    CROPS.mkdir(parents=True, exist_ok=True)
    path = CROPS / f"{name}.jpg"
    if path.exists():
        return path
    page_path = CROPS / f"{key}-page-{word.canvas:04d}.jpg"
    # archive.org's page images are numbered one below the hOCR's pages (checked on Gen 41:56, 1738).
    net.download(PAGE_IMAGE.format(item=BY_KEY[key].item, leaf=word.canvas - 1), page_path)
    _, words, (width, height) = pages(key)[word.canvas]
    lines = [w for w in words if abs(w.line - word.line) <= 1]
    own = [w for w in lines if w.line == word.line]
    box = (min(w.box[0] for w in own) - 60, min(w.box[1] for w in lines) - 15,
           max(w.box[2] for w in own) + 60, max(w.box[3] for w in lines) + 15)
    if os.name != "nt":
        x, y, w, h = _pixel_box(page_path, (width, height), box)
        _magick(str(page_path), "-crop", f"{w}x{h}+{x}+{y}", "+repage", "-quality", "90", str(path))
        return path
    script = ("Add-Type -AssemblyName System.Drawing; "
              f"$i = [System.Drawing.Image]::FromFile('{page_path}'); "
              f"$sx = $i.Width / {width}; $sy = $i.Height / {height}; "
              f"$x = [math]::Max(0, [int]({box[0]} * $sx)); $y = [math]::Max(0, [int]({box[1]} * $sy)); "
              f"$w = [math]::Min($i.Width - $x, [int](({box[2]} - {box[0]}) * $sx)); "
              f"$h = [math]::Min($i.Height - $y, [int](({box[3]} - {box[1]}) * $sy)); "
              "$b = New-Object System.Drawing.Bitmap $i; "
              "$c = $b.Clone((New-Object System.Drawing.Rectangle $x, $y, $w, $h), $b.PixelFormat); "
              f"$c.Save('{path}', [System.Drawing.Imaging.ImageFormat]::Jpeg); $c.Dispose(); $b.Dispose(); $i.Dispose()")
    subprocess.run(["powershell", "-NoProfile", "-Command", script], check=True, capture_output=True)
    return path


# ---------------------------------------------------------------- the edition read from its hOCR: leaves, lines, indents

LINE_MARK = ""    # a private-use character: a token of its own in align.words, never in the OCR


def witness(key):
    """An align.Witness of an edition read from its hOCR (the same ABBYY words as its _djvu.txt, in the same order),
    with each token's leaf (`canvas_at`, as mdz.witness) and line (`line_at`: (leaf, line)), and `line_start`:
    {token index of a line's first word: (leaf, line)} for the lines that do not continue a hyphenated word.

    Each line is marked in the text before cleaning and the marks are taken out after, so the tokens are exactly
    those of the unmarked text. A line that continues a hyphenated word (conſi-|deret) has its mark after its first
    word, so the hyphen is still joined."""
    import itertools
    import re
    from pipeline import align
    chunks, marks = [], []
    hyphen = False
    for leaf, words, (width, height) in pages(key):
        # The catchword (the next page's first word, alone at the foot of the page on the right: 1738 leaf 106
        # "Deinde") is not the text: left out, or the aligner pairs it in place of the word it repeats.
        last = max((w.line for w in words), default=None)
        tail = [w for w in words if w.line == last]
        if len(tail) == 1 and tail[0].box[0] > 0.6 * width and tail[0].box[1] > 0.85 * height:
            words = [w for w in words if w.line != last]
        for line, group in itertools.groupby(words, key=lambda w: w.line):
            texts = [w.text for w in group if w.text]     # the hOCR has empty words
            if not texts:
                continue
            if hyphen and len(texts) > 1:
                chunks.append(" ".join(texts[:1]) + " " + LINE_MARK + " " + " ".join(texts[1:]) + "\n")
                marks.append((leaf, line, False))
            elif hyphen:
                chunks.append(texts[0] + "\n")
            else:
                chunks.append(LINE_MARK + " " + " ".join(texts) + "\n")
                marks.append((leaf, line, True))
            hyphen = bool(re.search(r"\w[-¬]\s*$", texts[-1]))
    text = "".join(chunks)
    marked = align.words(align.clean(text))
    w = align.Witness(text.replace(LINE_MARK, ""))
    w.canvas_at, w.line_at, w.line_start = [], [], {}
    at, n = (marks[0][0], marks[0][1]), 0
    for token, _ in marked:
        if token == LINE_MARK:
            leaf, line, starts = marks[n]
            n += 1
            at = (leaf, line)
            if starts:
                w.line_start[len(w.canvas_at)] = at
            continue
        w.canvas_at.append(at[0])
        w.line_at.append(at)
    if [t for t, _ in marked if t != LINE_MARK] != [t for t, _ in w.tokens]:
        raise SystemExit(f"archive.witness({key}): the line marks changed the tokens")
    return w


def is_number(text):
    """A verse number in the margin as the OCR reads it (3, 2$, zg, o for 9)."""
    import re
    return bool(re.fullmatch(r"[\dIlioOSsz$gq]{1,3}[.,]?", text)) and any(c.isdigit() or c in "oOz$" for c in text)


def indents(key, leaves=None):
    """{(leaf, line): (indent in pixels, the OCR word the text starts with)} of the lines an edition indents to begin a paragraph (1738: Gen 44:3, 44:13,
    leaf 107). The page is set in two columns, the verse numbers in the outer margins. A line's start is its first
    word's left edge, or the next word's where the first stands in the margin (a verse number, whose box the OCR runs
    on to the word: 1738 Gen 44:3 "3" 42–121); a short word in the margin is a number however it is read: 1738 Exod 6:26 "at";
    the column's margin there is the lower quartile of the starts of the six lines
    above and below (headings and drop capitals stand further in; lines holding only margin numbers are left out). A line is a paragraph's first when it starts 40–140 px (about 1–2½ ems at 400 dpi; a skewed column's lines wander up to 30) inside that
    margin, and the line above in the column (for a column's first line, the last of the column before) ends a sentence (. ? ! :) or is short: and a line beside a drop capital (a glyph over
    2.2 times the usual height) counts only as the capital's first line: so neither a drop capital's
    second line nor a hyphenated word's second half counts, nor a chapter summary's hanging lines, which follow no
    stop. Running heads (the top 60 px) are left out."""
    import itertools
    import re
    import statistics
    out = {}
    previous = None                                          # the last line of the column before (for a column's first)
    for leaf, words, (width, _) in pages(key):
        if leaves is not None and leaf not in leaves and leaf + 1 not in leaves:
            previous = None
            continue
        rows = []
        for line, group in itertools.groupby(words, key=lambda w: w.line):
            ws = list(group)
            middle = (ws[0].box[0] + ws[-1].box[2]) / 2
            if ws[0].box[1] < 60 or all(w.box[2] < 0.06 * width or w.box[0] > 0.88 * width for w in ws):
                continue                                     # a running head, or the margin's numbers on their own
            rows.append({"line": line, "ws": ws, "col": 0 if middle < width / 2 else 1})
        heights = sorted(w.box[3] - w.box[1] for w in words) or [0]
        usual = heights[len(heights) // 2]
        capitals = [w.box for w in words if w.box[3] - w.box[1] > 2.2 * usual and len(w.text) <= 3]
        for col in (0, 1):
            cr = [r for r in rows if r["col"] == col]
            firsts = [r["ws"][0].box[0] for r in cr]
            # First pass: each line's text start, past a word standing in the margin (a verse number).
            for i, r in enumerate(cr):
                ws, r["start"], r["word"] = r["ws"], r["ws"][0].box[0], 0
                near = firsts[max(0, i - 6):i] + firsts[i + 1:i + 7]
                # The verse numbers stand left of the left column and right of the right one, on every page.
                if col == 0 and len(near) >= 4 and ws[0].box[0] < statistics.median(near) - 15:
                    if len(ws) > 1 and (is_number(ws[0].text) or len(re.sub(r"\W", "", ws[0].text)) <= 3):
                        r["start"], r["word"] = ws[1].box[0], 1
                    else:
                        r["start"] = None                    # a number run on to the word (2atque): unknown
            starts = [r["start"] for r in cr]
            for i, r in enumerate(cr):
                near = [x for x in starts[max(0, i - 6):i] + starts[i + 1:i + 7] if x is not None]
                if len(near) < 4 or r["start"] is None:
                    continue
                margin = sorted(near)[len(near) // 4]        # low: headings and drop capitals stand further in
                ws, start = r["ws"], r["start"]
                indent = start - margin
                top = ws[0].box[1]
                if any(start - 80 <= c[2] <= start + 30 and c[1] + 30 < top <= c[3] for c in capitals):
                    continue                                 # beside a drop capital, below its first line
                above = cr[i - 1]["ws"] if i else previous
                if not 40 <= indent <= 140 or above is None or (leaves is not None and leaf not in leaves):
                    continue
                texts = [w.text for w in above if not (is_number(w.text) and w.box[0] > above[0].box[0] + 400)]
                ends = "".join(texts[-2:]).strip()
                right = statistics.median(rr["ws"][-1].box[2] for rr in cr[max(0, i - 6):i + 7])
                short = i > 0 and above[-1].box[2] < right - 120
                if re.search(r"[-¬]$", ends) or not (re.search(r"[.?!:]\W{0,2}$", ends) or short):
                    continue
                out[(leaf, r["line"])] = (round(indent), ws[r["word"]].text)
            if cr:
                previous = cr[-1]["ws"]
    return out



def skipped_leaves(key):
    """The hOCR leaves archive.org leaves out of its page images: the gaps in page_numbers.json's leaf list (1738:
    386–389, 410–413, 424–425 and 830–831, pages photographed again, found when 1 Kings was read, 2026-11-21)."""
    data = json.loads((paths.SOURCES / "archive" / key / "page_numbers.json").read_text(encoding="utf-8"))
    kept = sorted(p["leafNum"] for p in data.get("pages", []))
    return {n for a, b in zip(kept, kept[1:]) for n in range(a + 1, b)}


def page_image(key, leaf):
    """The leaf's page image (cached in sources/archive/crops/), or None for a leaf archive.org shows no image of.
    archive.org numbers its images one below the hOCR's leaves, counting only the leaves it keeps (skipped_leaves)."""
    skipped = skipped_leaves(key)
    if leaf in skipped:
        return None
    path = CROPS / f"{key}-page-{leaf:04d}.jpg"
    if not path.exists():
        CROPS.mkdir(parents=True, exist_ok=True)
        n = leaf - 1 - sum(1 for s in skipped if s < leaf)
        net.download(PAGE_IMAGE.format(item=BY_KEY[key].item, leaf=n), path)
    return path


def line_box(key, leaf, first, last=None, pad=(70, 12)):
    """(x0, y0, x1, y1) in hOCR pixels around lines first…last of a leaf (one column: the lines' own words)."""
    last = first if last is None else last
    _, words, _ = pages(key)[leaf]
    ws = [w for w in words if first <= w.line <= last]
    return (max(0, min(w.box[0] for w in ws) - pad[0]), max(0, min(w.box[1] for w in ws) - pad[1]),
            max(w.box[2] for w in ws) + pad[0], max(w.box[3] for w in ws) + pad[1])


def sheet(key, items, path, width=900):
    """One image of several crops, each under its label, for reading many places at a glance: items are
    [(label, leaf, (x0, y0, x1, y1) in hOCR pixels)]. Drawn with Windows' System.Drawing through PowerShell (the
    standard library has no JPEG codec), or with ImageMagick elsewhere. Each crop comes out at full size: PowerShell's
    names ignore case, so `$w` (a crop's width) overwrites `$W` (`width`), the scale is 1, and the sheet is as wide as
    its last crop (a wider crop is cut at the right). The sheets read so far were made so; ImageMagick's are as wide as
    the widest crop, and `width` is unused there."""
    import json
    import subprocess
    import tempfile
    spec = []
    for label, leaf, box in items:
        _, _, (w, h) = pages(key)[leaf]
        image = page_image(key, leaf)
        if image is None:  # a leaf photographed again, with no image of its own (skipped_leaves)
            continue
        spec.append({"label": label, "image": str(image), "box": list(box), "size": [w, h]})
    if not spec:
        return None
    path.parent.mkdir(parents=True, exist_ok=True)
    if os.name != "nt":
        _magick_sheet(spec, path)
        return path
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(spec, f)
        spec_path = f.name
    script = (
        "Add-Type -AssemblyName System.Drawing; "
        f"$spec = Get-Content -Raw -Encoding UTF8 '{spec_path}' | ConvertFrom-Json; $W = {width}; "
        "$parts = @(); $total = 0; "
        "foreach ($s in $spec) { $i = [System.Drawing.Image]::FromFile($s.image); "
        "$sx = $i.Width / $s.size[0]; $sy = $i.Height / $s.size[1]; "
        "$x = [math]::Max(0, [int]($s.box[0] * $sx)); $y = [math]::Max(0, [int]($s.box[1] * $sy)); "
        "$w = [math]::Min($i.Width - $x, [int](($s.box[2] - $s.box[0]) * $sx)); "
        "$h = [math]::Min($i.Height - $y, [int](($s.box[3] - $s.box[1]) * $sy)); "
        "$scale = [math]::Min(1.6, $W / $w); $oh = [int]($h * $scale); "
        "$parts += ,@($i, $x, $y, $w, $h, [int]($w * $scale), $oh, $s.label); $total += $oh + 30 }; "
        "$b = New-Object System.Drawing.Bitmap $W, ([math]::Max(1, $total)); "
        "$g = [System.Drawing.Graphics]::FromImage($b); $g.Clear([System.Drawing.Color]::White); "
        "$g.InterpolationMode = 'HighQualityBicubic'; "
        "$font = New-Object System.Drawing.Font 'Arial', 13; $at = 0; "
        "foreach ($p in $parts) { $g.DrawString($p[7], $font, [System.Drawing.Brushes]::Firebrick, 4, $at + 4); $at += 30; "
        "$g.DrawImage($p[0], (New-Object System.Drawing.Rectangle 0, $at, $p[5], $p[6]), "
        "(New-Object System.Drawing.Rectangle $p[1], $p[2], $p[3], $p[4]), 'Pixel'); $at += $p[6]; $p[0].Dispose() }; "
        f"$b.Save('{path}', [System.Drawing.Imaging.ImageFormat]::Jpeg); $g.Dispose(); $b.Dispose()")
    subprocess.run(["powershell", "-NoProfile", "-Command", script], check=True, capture_output=True)
    os.unlink(spec_path)
    return path


# ---------------------------------------------------------------- page images without Windows: ImageMagick
# On Windows the crops and sheets are cut with System.Drawing through PowerShell; elsewhere (Ubuntu) with
# ImageMagick (`apt install imagemagick`: `convert` in version 6, `magick` in 7), the same boxes and sizes.

def jpeg_size(path):
    """(width, height) of a JPEG, read from its SOF marker (the standard library has no JPEG codec)."""
    with open(path, "rb") as f:
        data = f.read()
    at = 2
    while at + 9 < len(data):
        if data[at] != 0xFF:
            at += 1
            continue
        marker = data[at + 1]
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7 or marker == 0xFF:
            at += 1 if marker == 0xFF else 2
            continue
        length = int.from_bytes(data[at + 2:at + 4], "big")
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
            return int.from_bytes(data[at + 7:at + 9], "big"), int.from_bytes(data[at + 5:at + 7], "big")
        at += 2 + length
    raise ValueError(f"{path}: no JPEG frame header")


def _pixel_box(image, hocr_size, box):
    """(x, y, w, h) in the image's pixels of a box in hOCR pixels, clipped to the image, as the PowerShell does."""
    iw, ih = jpeg_size(image)
    sx, sy = iw / hocr_size[0], ih / hocr_size[1]
    x, y = max(0, int(box[0] * sx)), max(0, int(box[1] * sy))
    return x, y, min(iw - x, int((box[2] - box[0]) * sx)), min(ih - y, int((box[3] - box[1]) * sy))


def _magick(*args):
    import shutil
    import subprocess
    program = shutil.which("magick") or shutil.which("convert")
    if not program:
        raise SystemExit("archive: page crops need ImageMagick here (sudo apt install imagemagick)")
    subprocess.run([program, *args], check=True, capture_output=True)


def _magick_sheet(spec, path):
    """The sheet of `sheet`, drawn by ImageMagick: each crop at full size under a red label, as wide as the widest."""
    boxes = [_pixel_box(s["image"], s["size"], s["box"]) for s in spec]
    width = max(w for _, _, w, _ in boxes)
    args = []
    for s, (x, y, w, h) in zip(spec, boxes):
        label = s["label"].replace("%", "%%")
        args += ["(", "-size", f"{width}x30", "xc:white", "-fill", "firebrick", "-pointsize", "17",
                 "-annotate", "+4+21", label, ")",
                 # +size: a -size before a JPEG makes the decoder shrink it
                 "(", "+size", s["image"], "-crop", f"{w}x{h}+{x}+{y}", "+repage",
                 "-background", "white", "-gravity", "NorthWest", "-extent", f"{width}x{h}", ")"]
    _magick(*args, "-append", "-quality", "90", str(path))
