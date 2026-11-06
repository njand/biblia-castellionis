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
