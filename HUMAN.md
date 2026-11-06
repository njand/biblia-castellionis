# For Nathan

## Now

- **2026-11-05 — M0 (groundwork) built, not committed.** `python -m pipeline` fetches every witness and keeps the
  chapter ledger:
  - Wikisource: 58 books, 15,997 verses.
  - WordPress: Genesis 1–35 and the four Gospels.
  - archive.org OCR: seven volumes.
  - KJV, BSB, WEB, Vulgate, SBLGNT and OSHB.
  - `python -m pipeline status` shows where every chapter stands.
- **Next: M1 (calibration).** Learn the spelling and macron rules from the finished chapters, align the OCR
  witnesses to verses, and build the test harness that scores the pipeline against your hand-finished chapters.

## Decisions waiting

1. **Base edition.** Keep 1726–27 as primary and take Wikisource's (1738/1760) readings only where the scans show
   the same text? Or make Wikisource's editions the base and record 1726–27 differences as variants?
2. **Apocrypha.** In scope? Wikisource has Tobit, Judith and Wisdom; nothing yet for Sirach, Baruch or Maccabees,
   and the KJV versification table has no Apocrypha.
3. **Chapter summaries** (Wikisource's *argumenta*; your commented `\summary{}` in Genesis): include them?
4. **Quotation marks.** Confirm: “…” for direct speech, ‘…’ for reported discourse and nested quotes? Then the
   README's sentence on single quotes gets updated.
5. **Versification.** KJV everywhere, including the Hebrew/English differences and the Psalm titles?
6. **Review load.** Auto-apply macrons where the sources agree on audible vowels, corrections that two witnesses
   support, and approved spelling rules, with one chapter in ten read in full?
7. **License** for the edition, and how to credit Wikisource and the scan libraries.
8. **Data location.** The pipeline uses `../fur-fulminis/data` in place (the M0 default, via `LATIN_REF_HOME`).
   Copy it here instead?

## How to run

```
python -m pipeline fetch all        # once; downloads are cached in sources/ (≈260 MB)
python -m pipeline status
python -m pipeline status Matt --chapters
```
