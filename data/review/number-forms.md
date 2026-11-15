# Classical number forms in the edited text (decision 70): where else the rule reaches

Proposed 2026-11-14. Every number in the settled text (all books) of the kind the rule is about: an 8 or 9 before a
round ten, which classical Latin often says by subtraction (*duodē-*, *ūndē-*). Counts from the Latin Library corpus
(`python -m pipeline latin attest`; T1–T2 are the Golden Age tiers, T3 Silver, T4 later):

| Number | Subtractive | Additive | Settled text |
|---|---|---|---|
| 18 | *duodēvīgintī* 55 (Livy 10, Plautus 2, Columella 3, Velleius 3) | *octōdecim* 13 (Livy 1, the rest late) | Gen 14:14 *trecentōs octōdecim*; elsewhere *duodēvīgintī* (3) |
| 19 | *ūndēvīgintī* 16 (Cicero 1, Livy 4, Augustus 2, Pliny, Tacitus) | *novemdecim* 1 (medieval) | *ūndēvīgintī* (Gen 11:25, kept) |
| 28 | *duodētrīgintā* 9 (Livy 4, Suetonius 2) | *vīgintī octō* 40 (Columella 4, Frontinus 5, the Digest 9, the Vulgate 6) | Exod 26:2 *vīgintī octō cubitōrum* |
| 69 | *ūndēseptuāgintā* 0 | *sexāgintā novem* 10 (Livy 1, Frontinus 3) | Gen 5:27 *nōngentōs sexāgintā novem* |
| 99 | *ūndēcentum* 0 in the corpus | *nōnāgintā novem* 15 (Frontinus 1; the Vulgate, later) | Matt 18:12, 13, Luke 15:4, 7 *nōnāgintā novem* |

The rule as you put it ("the more classical number forms, i.e. undeviginti") is clear where the corpus is: 18
and 19 are subtractive in the best authors, and 28 in Livy, the one Golden Age historian who uses either. For 69
and 99 the subtractive forms are not in the corpus at all (Gaffiot and the grammars give *ūndēcentum*, but no
author here uses it), and the additive forms are the ones Livy and Frontinus write.

## Proposed

1. **Gen 14:14** *trecentōs octōdecim* → *duodēvīgintī* (the subtractive 18, Livy ×10 against *octodecim* ×1).
   **Apply:** `Gen.14.14` la: `trecentōs octōdecim` → `trecentōs duodēvīgintī`
2. **Exod 26:2** *vīgintī octō cubitōrum* → *duodētrīgintā* (Livy ×4, Suetonius ×2; *vīgintī octō* in Columella
   and later).
   **Apply:** `Exod.26.2` la: `vīgintī octō cubitōrum` → `duodētrīgintā cubitōrum`
3. **Gen 5:27** *nōngentōs sexāgintā novem* → *nōngentōs ūndēseptuāgintā* (Nathan, 2026-11-14: "Apply the
   subtractive rule to 69 as well"). Not in the corpus; Wiktionary gives *ūndēseptuāgintā* (`latin macron`), formed as
   *ūndēvīgintī*, *ūndētrīgintā*: *ūn-dē-septuāgintā*, the *ā* of *septuāgintā* long as Gaffiot.
   **Apply:** `Gen.5.27` la: `nōngentōs sexāgintā novem` → `nōngentōs ūndēseptuāgintā`
4. **99 stays additive** (Matt 18:12–13, Luke 15:4, 7 *nōnāgintā novem*): *ūndēcentum* is not in the corpus.
   Your call: say if 99 should take the rule too.

**Decision:** pending
