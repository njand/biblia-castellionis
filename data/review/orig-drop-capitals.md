# The drop capital's word in the approved printed texts (New Testament, Genesis)

Proposed 2026-11-15. For Exodus you decided (your "Yes, approve" to `exod31-40-orig.md`) that a chapter's first word
beside its drop capital, which both printers set with a small capital or two after the initial (*CVm*,
*AVditionem*), is written as a normal capitalized word, with the printers' *u* inside a word for the small capital
*V* (*Cum*, *Auditionem*); a book's first word printed wholly in capitals (*PRIMVM*, *PRINCIPIO*, *SENIOR*,
*MVLTIFARIAM*) is the print's own convention and stays. Exodus is set so (`orig.opening_word`).

The same rule would change 34 words in the approved `text/orig/` files, which are never rewritten without
your word. **Your decision**: accept to have them set the same way, so both Testaments follow one rule.

| File | Chapter | As now | Proposed |
|---|---|---|---|
| `text/orig/1CO.usfm` | 6:1 | *AVdet* | *Audet* |
| `text/orig/1CO.usfm` | 14:1 | *PErsequimini* | *Persequimini* |
| `text/orig/1TH.usfm` | 4:1 | *QVod* | *Quod* |
| `text/orig/1TI.usfm` | 5:1 | *SEniorem* | *Seniorem* |
| `text/orig/2CO.usfm` | 3:1 | *INgredimur* | *Ingredimur* |
| `text/orig/2CO.usfm` | 8:1 | *CErtiores* | *Certiores* |
| `text/orig/2TH.usfm` | 2:1 | *ROgamus* | *Rogamus* |
| `text/orig/2TH.usfm` | 3:1 | *QVod* | *Quod* |
| `text/orig/ACT.usfm` | 26:1 | *HIc* | *Hic* |
| `text/orig/GEN.usfm` | 14:1 | *COmmissum* | *Commissum* |
| `text/orig/GEN.usfm` | 18:1 | *PRæterea* | *Præterea* |
| `text/orig/GEN.usfm` | 34:1 | *DIna* | *Dina* |
| `text/orig/GEN.usfm` | 38:1 | *Ivdas* | *Iudas* |
| `text/orig/GEN.usfm` | 45:1 | *HIc* | *Hic* |
| `text/orig/GEN.usfm` | 50:1 | *Tvm* | *Tum* |
| `text/orig/HEB.usfm` | 10:1 | *VMbram* | *Vmbram* |
| `text/orig/HEB.usfm` | 13:1 | *DVret* | *Duret* |
| `text/orig/JHN.usfm` | 10:1 | *CErtò* | *Certò* |
| `text/orig/LUK.usfm` | 5:1 | *CVm* | *Cum* |
| `text/orig/LUK.usfm` | 11:1 | *CVm* | *Cum* |
| `text/orig/LUK.usfm` | 15:1 | *FRequentabant* | *Frequentabant* |
| `text/orig/LUK.usfm` | 19:1 | *EO* | *Eo* |
| `text/orig/LUK.usfm` | 21:1 | *CVm* | *Cum* |
| `text/orig/MAT.usfm` | 17:1 | *POst* | *Post* |
| `text/orig/MAT.usfm` | 24:1 | *CVm* | *Cum* |
| `text/orig/MAT.usfm` | 26:1 | *POsteaquam* | *Posteaquam* |
| `text/orig/MAT.usfm` | 27:1 | *MAnè* | *Manè* |
| `text/orig/MRK.usfm` | 11:1 | *CVm* | *Cum* |
| `text/orig/MRK.usfm` | 13:1 | *EXeunti* | *Exeunti* |
| `text/orig/MRK.usfm` | 14:1 | *CVm* | *Cum* |
| `text/orig/MRK.usfm` | 15:1 | *MAnè* | *Manè* |
| `text/orig/REV.usfm` | 2:1 | *EPhesinæ* | *Ephesinæ* |
| `text/orig/REV.usfm` | 12:1 | *VIsumque* | *Visumque* |
| `text/orig/ROM.usfm` | 3:1 | *QVæ* | *Quæ* |

**Decision:** accept (Nathan, 2026-11-15: "Yes, apply them"): the 34 words set in `text/orig/`, the rows behind 33 of them in `data/decisions/*.orig.tsv`, and the rule applied by `orig.build` for both Testaments. Rebuilt with `--force` to check: Luke comes out exactly as approved; Genesis differs only at 25:12 (below).

## One more: Gen 25:12 *Ismælis*, an error in the approved Genesis

The approved `text/orig/GEN.usfm` has *Ismælis* at 25:12, where 1738 prints ***Ismaelis autem*** (leaf 84, seen
2026-11-15 on the crop of that line while checking the Ismael places; the row for it was not added then). Every other
Ismael form in the printed Genesis is *Ismael-*, read on the page. A rebuild gives *Ismaelis*. **Your decision**:
correct the approved file (and add the row).

**Decision:** accept (Nathan, 2026-11-15: "Yes, correct it"): `text/orig/GEN.usfm` 25:12 now *Ismaelis*, and its row added.

## Three more, found checking whether any *Tvm* was left (your question of 2026-11-15)

Each seen on 1738's page; none has a row behind it (each came from the OCR), so each would get one.

1. **Gen 18:33** *Tvm Ioua* → ***Tum Ioua***: 1738 begins a chapter here (its chapter divisions are not the KJV's), with a
   drop capital *T* and the small capitals *Vm* (leaf 77, first line): the same case as the 34 above, which the
   chapter-opening rule missed because the KJV's chapter does not begin there.
2. **Gen 18:33** *cum abrahamo* → ***cum Abrahamo***: the same line prints *cumAbrahamo* with a capital *A* (no space,
   as 1738 runs words together; the printed text spaces words).
3. **Exod 3:14** *ERO Qvi ERO* → ***ERO QVI ERO***: the name is printed wholly in capitals (leaf 116, line 98); the OCR
   read the small *V I* as *vi*.

**Decision:** accept (Nathan, 2026-11-15: "Yes, apply them"): the three set in `text/orig/GEN.usfm` and `EXO.usfm`, with their rows.
