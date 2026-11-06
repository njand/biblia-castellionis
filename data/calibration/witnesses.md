# Witnesses against the gold text

Each witness aligned word by word to the settled chapters (`python -m pipeline align`). **Found**: share of gold words the witness has at all (OCR that lost lines, columns read out of order, or the book missing). **Agree**: of the words found, how many read the same once case, accents and macrons, i/j, u/v and æ/ae are set aside. **f/s-blind**: the same, also counting f for long s as agreement. **Reading**: the editions' spelling habits also set aside (*quum/cum, eīs/iīs, coelum/cælum, Joannes/Johannēs*, h-, double letters): what is left is a misreading, or a different word in that edition (your text follows 1726–27). **Verse numbers**: printed numbers just before a verse that equal its number (numbers the OCR lost or misread don't count).

| Witness | Books | Gold words | Found | Agree | f/s-blind | Reading | Verse numbers |
|---|---|---:|---:|---:|---:|---:|---:|
| WordPress 2019 (your macrons) | Gen, Matt, Mark, Luke, John | 34,615 | 100.0% | 99.6% | 99.6% | 99.7% | 1/1 |
| Wikisource (1760 NT, 1738 OT) | Gen, Matt, Mark, Luke, John | 34,615 | 100.0% | 99.6% | 99.6% | 99.7% | 0/0 |
| 1726–27 Bible (Google Books OCR, TXT/1) | Gen, Matt, Mark, Luke, John | 34,615 | 43.6% | 81.5% | 95.9% | 97.0% | 897/944 |
| 1758 NT, 2 vols (Tesseract, long s) | Matt, Mark, Luke, John | 22,619 | 98.2% | 94.3% | 95.4% | 96.6% | 62/251 |
| 1747 NT (Tesseract) | Matt, Mark, Luke, John | 22,619 | 81.3% | 76.2% | 92.5% | 93.9% | 992/1138 |
| 1750 Bible (Tesseract) | Gen, Matt, Mark, Luke, John | 34,615 | 93.7% | 77.4% | 92.5% | 93.6% | 278/401 |
| 1715 NT (Tesseract) | Matt, Mark, Luke, John | 22,619 | 65.7% | 75.3% | 91.3% | 92.5% | 738/939 |
| 1738 OT vol. 1 (ABBYY) | Gen | 11,996 | 89.8% | 74.9% | 88.5% | 89.3% | 70/118 |
| 1681 NT (KB, ABBYY) | Matt, Mark, Luke, John | 22,619 | 59.9% | 65.2% | 75.1% | 75.7% | 603/921 |

## By book

| Witness | Book | Found | Agree | f/s-blind | Reading |
|---|---|---:|---:|---:|---:|
| ocr-1681 | Matt | 62.3% | 65.0% | 76.0% | 76.7% |
| ocr-1681 | Mark | 61.6% | 62.0% | 71.5% | 72.2% |
| ocr-1681 | Luke | 57.5% | 65.7% | 74.8% | 75.3% |
| ocr-1681 | John | 61.8% | 66.8% | 78.0% | 78.7% |
| ocr-1715 | Matt | 71.2% | 75.2% | 91.3% | 92.7% |
| ocr-1715 | Mark | 70.1% | 74.2% | 91.7% | 93.3% |
| ocr-1715 | Luke | 61.6% | 76.2% | 90.9% | 91.8% |
| ocr-1715 | John | 62.5% | 73.0% | 92.6% | 93.3% |
| ocr-1726 | Gen | 47.3% | 87.5% | 96.1% | 96.7% |
| ocr-1726 | Matt | 39.9% | 78.8% | 96.8% | 98.2% |
| ocr-1726 | Mark | 29.0% | 76.0% | 94.6% | 96.8% |
| ocr-1726 | Luke | 47.6% | 78.2% | 95.3% | 96.7% |
| ocr-1726 | John | 36.7% | 76.2% | 96.1% | 97.6% |
| ocr-1738 | Gen | 89.8% | 74.9% | 88.5% | 89.3% |
| ocr-1747 | Matt | 78.7% | 75.3% | 91.4% | 92.8% |
| ocr-1747 | Mark | 88.4% | 75.8% | 93.1% | 94.4% |
| ocr-1747 | Luke | 80.5% | 77.2% | 92.9% | 94.2% |
| ocr-1747 | John | 84.2% | 74.6% | 93.7% | 95.0% |
| ocr-1750 | Gen | 94.4% | 79.5% | 93.5% | 94.3% |
| ocr-1750 | Matt | 90.9% | 76.1% | 91.3% | 92.3% |
| ocr-1750 | Mark | 94.5% | 74.9% | 91.5% | 93.1% |
| ocr-1750 | Luke | 95.6% | 77.2% | 92.7% | 93.9% |
| ocr-1750 | John | 90.0% | 74.5% | 91.6% | 92.4% |
| ocr-1758 | Matt | 99.0% | 94.9% | 96.2% | 97.6% |
| ocr-1758 | Mark | 97.6% | 94.1% | 95.1% | 96.1% |
| ocr-1758 | Luke | 97.8% | 93.5% | 94.5% | 95.6% |
| ocr-1758 | John | 99.0% | 95.9% | 97.0% | 98.0% |
| wikisource | Gen | 100.0% | 99.2% | 99.2% | 99.5% |
| wikisource | Matt | 100.0% | 99.9% | 99.9% | 99.9% |
| wikisource | Mark | 100.0% | 99.6% | 99.6% | 99.7% |
| wikisource | Luke | 99.9% | 99.8% | 99.8% | 99.9% |
| wikisource | John | 100.0% | 99.8% | 99.9% | 99.9% |
| wordpress | Gen | 100.0% | 99.2% | 99.2% | 99.5% |
| wordpress | Matt | 100.0% | 99.9% | 99.9% | 99.9% |
| wordpress | Mark | 100.0% | 99.6% | 99.6% | 99.7% |
| wordpress | Luke | 100.0% | 99.8% | 99.8% | 99.9% |
| wordpress | John | 100.0% | 99.8% | 99.9% | 99.9% |

## Commonest disagreements in reading (gold → witness, folded)

- **ocr-1681**: eum→cum 36×, est→cft 32×, autem→autcm 31×, ei→ci 25×, et→c 24×, et→sc 23×, ille→illc 11×, eius→cius 11×, eo→co 11×, me→mc 9×
- **ocr-1715**: quae→quz 26×, haec→hzc 9×, est→elt 8×, quae→qua 8×, filius→homine 7×, hominis→natus 7×, pharisaei→pharifzi 7×, iesus→lefus 6×, eo→co 6×, haec→hxc 4×
- **ocr-1726**: allocutus→alloquutus 9×, cumque→quumque 5×, autem→aurem 3×, tricesimo→trigesimo 3×, quemdam→quendam 3×, tum→cum 3×, esse→efle 3×, umquam→unquam 3×, intellegens→intelligens 3×, sit→fic 3×
- **ocr-1738**: tum→turn 54×, sic→fie 24×, quem→quern 16×, eam→earn 16×, hic→hie 14×, quae→qux 12×, terram→terrain 9×, haec→hxc 9×, illa→ilia 8×, aetatis→xtatis 7×
- **ocr-1747**: filius→homine 9×, hominis→natus 9×, iesus→lefus 8×, collegio→fynagoga 6×, cumque→quumque 5×, esse→efle 5×, elisabeta→elizabeta 4×, et→t 4×, occulte→occulta 3×, sermonem→fermone 3×
- **ocr-1750**: et→ct 36×, iesus→lefus 17×, eo→co 14×, esse→efle 13×, allocutus→adlocutus 13×, eius→cius 11×, filius→homine 11×, eum→cum 8×, alloquitur→adloquitur 7×, elisabeta→elizabeta 6×
- **ocr-1758**: si→i 9×, exstitit→extitit 8×, filii→fil 7×, filii→fili 6×, alioqui→alioquin 4×, occulte→occulta 3×, exsequitur→exequitur 3×, atque→arque 3×, neue→neye 3×, et→set 3×
- **wikisource**: tricesimo→trigesimo 6×, aeriae→aereae 5×, aerias→aereas 3×, aeriis→aereis 2×, sescentesimo→sexcentesimo 2×, subole→sobole 2×, querqueto→querceto 2×, subolis→sobolis 2×, ne→nae 2×, deuersorium→diuersorium 2×
- **wordpress**: tricesimo→trigesimo 6×, aeriae→aereae 5×, aerias→aereas 3×, aeriis→aereis 2×, sescentesimo→sexcentesimo 2×, subole→sobole 2×, querqueto→querceto 2×, subolis→sobolis 2×, ne→nae 2×, deuersorium→diuersorium 2×
