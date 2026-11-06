"""Read-only Latin lookups, borrowed from the fur-fulminis project (as e-liber's tools/latin.py does).

Forwards a few `lrl` subcommands to ../fur-fulminis/tools/lrl (or $LATIN_REF_HOME/tools/lrl), which reads its
own data/ folder: the macron database (W = Wiktionary, M = Macronizer, G = Gaffiot 2016), Lewis & Short, the
Neo-Latin Lexicon and the tiered Latin Library corpus. Nothing here can write to that project.

  macron <form>…            known macronizations of a form, with sources, lemmas, parses and Gaffiot's headword
  macron-check --text PATH  words of a text file whose macrons match no known form (or that Gaffiot marks differently)
  ls <word>                 Lewis & Short
  attest <phrase>           search the corpus (--near N for proximity)
  lexicon <term>            Neo-Latin Lexicon
  wiki <term>               Vicipaedia / Wikipedia / Wikidata names

Gaffiot 2016 is CC BY-NC-ND: use its answers to decide, never copy its text into this repo."""

import os
import subprocess
import sys
from pathlib import Path

from pipeline import paths

ALLOWED = ("macron", "macron-check", "ls", "attest", "lexicon", "wiki")
HOME = Path(os.environ.get("LATIN_REF_HOME", paths.ROOT.parent / "fur-fulminis"))
LRL = HOME / "tools" / "lrl"


def run(argv, capture=False):
    """Run an allowed lrl command. Returns the exit code, or (code, stdout) with capture=True."""
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return (0, "") if capture else 0
    cmd, rest = argv[0], argv[1:]
    if cmd not in ALLOWED:
        raise SystemExit(f'latin: "{cmd}" is not a lookup; allowed: {", ".join(ALLOWED)}')
    # Without --text, macron-check would read a fur-fulminis chunk instead of this project's text.
    if cmd == "macron-check" and "--text" not in rest and not {"-h", "--help"} & set(rest):
        raise SystemExit("latin: macron-check needs --text PATH")
    if not LRL.exists():
        raise SystemExit(f"latin: {LRL} not found; set LATIN_REF_HOME to the fur-fulminis folder")
    result = subprocess.run([sys.executable, str(LRL), cmd, *rest], check=False, capture_output=capture,
                            encoding="utf-8" if capture else None)
    return (result.returncode, result.stdout) if capture else result.returncode
