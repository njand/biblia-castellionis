"""Scans of Castellio editions on archive.org: OCR text, page numbers and (optionally) hOCR word boxes.

Each witness is one edition. Two items hold several editions, so a witness picks its files by a substring of
the file name. Downloads go to sources/archive/<key>/ as text.txt, page_numbers.json and hocr.html (hOCR is
14–40 MB per volume, so only with --hocr). Page images are fetched later, a page at a time, when a reading
needs checking; the jp2 zips are ~1 GB each and are never downloaded whole."""

import json
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
