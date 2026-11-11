"""Where things live. Downloads go to sources/ (git-ignored); parsed, reviewable data goes to data/."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SOURCES = ROOT / "sources"            # raw downloads, cached; never edited; git-ignored
DATA = ROOT / "data"                  # parsed data committed to git
WITNESSES = DATA / "witnesses"        # one folder per witness, one TSV per book (id<TAB>text)
VERSIFICATION = DATA / "versification"
LEDGER = DATA / "status.tsv"

TXT = ROOT / "TXT"
