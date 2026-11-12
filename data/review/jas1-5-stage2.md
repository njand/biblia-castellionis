# James 1–5, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-12 (decision 30's standing rule), on the route of 1 Timothy and Titus (`data/review/1tim1-6-stage2.md`,
`data/review/titus1-3-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 917–919: the title and Athanasius's
  argument at the foot of 916, 1:1–2:21 on 917, 2:21–4:13 on 918, 4:14–5:20 on 919). 1556 is the reference: where it
  reads otherwise, its reading is recorded as a variant (section 5); its e-rara OCR has James on pages 10282439–41 and
  reaches most of the letter, though garbled at 1:5–8, 1:13–17 and 2:1–11 (it does not reach 1:6–8 or 2:14–18). Stage 1 drafted Wikisource's
  James as **`text/draft/JAS.usfm`** (BSB paragraphs). You have no earlier work on James; `TXT/1 - OCR` (the
  1726–27 printing, Google Books OCR, uncorrected) is the witness `1726`, read as an OCR.
- **Wikisource's James is the early wording**, as its Galatians, Colossians and Titus: *perfectam actionem* for
  *perfectum opus* (1:4), *et excito* for *ac excito* (1:6), *adjuvaret … sit* for *adjuverit … fuerit* (2:22), *sic
  se habet* (2:23), *esse graviores* (3:1), *Fratres, nolite* (4:11), *viri boni* for *justi* (5:16), each with the
  early-line printings 1715, 1747, 1750, and slips of its own (*existimare*, *incidistis*, *credit*, *parcant*,
  *virres*, *et vestris*, *amicitias*, *adlenabit*, *petiiset*). 1556 has the revised reading wherever its OCR can be
  read, except 1:4 *perfectam actionem* and 2:22 *adjuvaret* (with Wikisource), and it reads *misericordia* where
  1573 and Wikisource read *pietas* at 2:13 and 3:17 (section 5).
- **Versification** (decision 5): the draft is at the KJV counts (108 verses), no edits file. 1573 prints every verse
  number and agrees with the draft everywhere but **4:10–11**: 1573 runs *Nolite alius alii detrahere … legemque
  damnat* into 10 and starts 11 at *Quod si legem damnas* (canvas 918, on the image); the KJV's 4:11 opens *Speak not
  evil one of another, brethren* (Μὴ καταλαλεῖτε ἀλλήλων), as the draft. Kept; nothing to move.
- **Collation** (`python -m pipeline collate Jas 1-5`; `data/calibration/Jas1-5-collation.tsv`, 187 places: 34
  *correct*, 8 *others-1573-agrees*, 5 *others*, 137 *base-only* (86 reading, 19 division, 17 f/s, 8 spelling, 7
  edge), 3 *uncovered*), with the edge and f/s checks. Read on the page image (crops in
  `sources/mdz-1573/crops/Jas.*`, 37): every reading where 1573 and another printing agree against Wikisource, the
  *others* places that touch the text (4:1 *ex*), every base-only reading whose 1573 words are Latin (1:6 *ac*, 1:18
  *et*, 1:22 *taxat*, 2:22 *adiuuerit*, 3:14 *et*, 5:16 *iusti*), the edge places (2:24 *non solum fide*, 4:7 *vos
  fugiet*, 4:10–11 *euehet. Nolite*, 4:11 *condemnator*: all printed; 1:27 *mundo* is in the OCR, *múdo*) and the L. … G.
  marks of 5:3. The rest of the base-only readings are 1573's OCR (*tétationem*, *chariſsini*, *avmbra*, *tede*,
  *inanat*, *fontein*, *vilum*), word breaks at line ends (*tribu bus*, *occi dito*, *Sci licet*, *reuo cauerit*),
  words run together (*Glorieturautem*, *Nemodum*, *Sicloqmini*, *Quodfiamaram*, *Nuncin*), note letters and margin
  notes run into the text (section 4), the running head (2:21 *IACOBI EPISTOLA*) and the verse numbers *It* (3:11)
  and *ii* (5:11). Each place was also read against 1556 (its e-rara OCR, `sources/erara-1556/`) and the archive.org
  printings (1758, 1681, 1715, 1747, 1750).
- **Every verse was read whole against 1573's page text** (canvases 917–919), not only the collation's places: it
  found the missing *Fratres* of 4:11 (the collation saw it only as an edge place, 1573's verse 10 holding the clause)
  and nothing further.
- **The three uncovered verses** (1573's OCR 50–58% of the words) were read whole on the image: 1:23 *Nã ſi quis
  ſermonẽ audit, nec exequitur, is perin-de eſt ac ſi q̃s corporis ſui faciẽ contẽpletur in ſpeculo,* (crop
  `Jas.1.23-sermonem`), 3:16 *Vbi enim inuidia eſt & ſimultas, ibi eſt inconſtan-tia, omniſq; vitioſa res.*
  (`Jas.3.16-inconstantia`) and 4:10 *Sũmittite vos Dño, & vos euehet.* (`Jas.4.10-Sumittite`). None differs from the
  draft but in spelling (*exequitur*, *Summittite*, section 4).
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fide/side*, *fides*,
  *fidei*, *fit/sit*, *fieri*, *fons/sons*, *fuistis/suistis*, *fallit*, *ferarum/serarum*, *facis*, *foribus*,
  *finem*, *fructum*) was read in its verse: all are *f* by sense and on the page. Every *s* word whose *f*-form is
  Latin (*si/fi*, *sit/fit*, *sine/fine*, *sontem/fontem*, *sui/fui*, *serpentum*, *sede*, *sex*, *soror*, *suam*):
  all are *s* by sense, and the places where 1573's OCR has the *f* and the *f*-form could be construed were read on
  the image: 1:25 *qui nõ ſit obliuioſus*, 2:17 *mortua ſit*, 2:20 *fidem ſine operibus*, 4:14 *quid ſit cras
  futurum*, 5:12 *vt etiam ſit etiam*, 5:20 *qui ſontem ab erroris ſui via* are all long s. None found.
- **In all, 19 corrections**: 9 Wikisource slips (section 1), 8 readings of Castellio's revised text (section 2), 1
  dropping of the L. … G. marks (section 2d), 1 word division (section 3). Spellings (*quum*, *carissimi*,
  *umquam*, *tentari*, *quotidianoque*, *intelligere*, *paullisper*, *exsequitur*, *exspectat*, *adlectus*,
  *adflictate*, …) are left to stage 3 (decisions 37, 41 and 42's rules); eight rules proposed (section 6). Four places
  where 1556 reads against 1573 are recorded (section 5), one of them from a doubtful OCR.

## 1. Wikisource slips: 1573 and the other printings agree against it (9)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **James 1:2** *Summopere gaudendum existimare, fratres mei* → *existimate*. 1573 *Summopere gaudendum exi-/ſtimate, fratres mei* (canvas 917), the imperative (ἡγήσασθε); 1556 (OCR *éxiftimate*), 1758, 1750. Wikisource alone.
   **Apply:** `Jas.1.2` la: `gaudendum existimare,` → `gaudendum existimate,`
2. **James 1:2** *quum in varias incidistis periclitationes* → *inciditis*. 1573 *cùm in varias / inciditis periclitationes* (canvas 917), the present (ὅταν … περιπέσητε); 1556 (OCR *in^ cíditis*), 1758. 1750 *incidistis* with Wikisource.
   **Apply:** `Jas.1.2` la: `varias incidistis periclitationes` → `varias inciditis periclitationes`
3. **James 2:19** *Tu Deum unum esse credit* → *credis*. 1573 *Tu Deum vnum eſſe credis : Rectè facis* (canvas 917), σὺ πιστεύεις; 1556 (OCR *eífecredis*), 1758, 1681, 1747, 1750. Wikisource alone.
   **Apply:** `Jas.2.19` la: `esse credit:` → `esse credis:`
4. **James 3:3** *ut nobis parcant* → *ut nobis pareant*. 1573 *vt / nobis pareant, eorumq; totum corpus agimus* (canvas 918), εἰς τὸ πείθεσθαι αὐτοὺς ἡμῖν, that they obey us; 1556, 1758 (OCR *reant*), 1681, 1715, 1747, 1750. Wikisource alone.
   **Apply:** `Jas.3.3` la: `nobis parcant,` → `nobis pareant,`
5. **James 3:5** *magnas virres habet* → *vires*. 1573 *magnas / vires habet* (canvas 918); 1556, 1758, 1681, 1750.
   **Apply:** `Jas.3.5` la: `magnas virres habet` → `magnas vires habet`
6. **James 4:1** *nonne hinc, et vestris libidinibus* → *ex vestris*. 1573 *nónne hinc, ex / veſtris libidinibus* (canvas 918), ἐκ τῶν ἡδονῶν ὑμῶν; 1556 (OCR *hínc, ex ueftríslibidinibus*), 1758, 1681, 1715, 1750. Wikisource alone.
   **Apply:** `Jas.4.1` la: `hinc, et vestris libidinibus` → `hinc, ex vestris libidinibus`
7. **James 4:4** *nescitis, mundi amicitias Dei esse inimicitias* → *mundi amicitiam*. 1573 *neſcitis mundi a-/micitiam, Dei eſſe inimicitias* (canvas 918), ἡ φιλία τοῦ κόσμου; 1556, 1758, 1681, 1715, 1747. 1750 *amicitias* with Wikisource.
   **Apply:** `Jas.4.4` la: `mundi amicitias Dei` → `mundi amicitiam Dei`
8. **James 5:15** *eumque adlenabit Dominus* → *adlevabit*. 1573 *eũq; alleua-/bit Dominus* (canvas 919), ἐγερεῖ; 1556 (*alleuabít*), 1758, 1681, 1715, 1747, 1750 (*adleuabit*). The *ad-* is stage 3's (section 6).
   **Apply:** `Jas.5.15` la: `eumque adlenabit Dominus` → `eumque adlevabit Dominus`
9. **James 5:17** *quum precibus petiiset* → *petiisset*. 1573 *cùm precibus petijſſet ne plueret* (canvas 919); 1758, 1681, 1715, 1750 (1556's OCR *petrjfer*).
   **Apply:** `Jas.5.17` la: `precibus petiiset,` → `precibus petiisset,`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (8)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 differs in order or form. 1556 has
the revised reading too wherever its OCR can be read, except 1:4 and 2:22 *adjuvaret* (section 5).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **James 1:4** *Patientia autem perfectam actionem habeat* → *perfectum opus*. 1573 *Patientia autem perfectum opus habeat, vt perfe-/cti* (canvas 917), ἔργον τέλειον; 1758, 1681 (OCR *pcrfcctuin <» pus*). **1556** *perfectam actionem* (OCR), with Wikisource and 1750: a 1573 change (section 5). For your eye.
   **Apply:** `Jas.1.4` la: `autem perfectam actionem habeat` → `autem perfectum opus habeat`
2. **James 1:6** *ventis acto et excito* → *ventis acto ac excito*. 1573 *ventis acto / ac excito.* (canvas 917); 1758, 1726. The early line *et* (Wikisource, 1715, 1750); 1556's OCR does not reach the verse.
   **Apply:** `Jas.1.6` la: `ventis acto et excito` → `ventis acto ac excito`
3. **James 2:22** *utque operibus fides perfecta sit* → *perfecta fuerit*. 1573 *vtque operi-/bus fides perfecta fuerit.* (canvas 918); 1556 (OCR *perfecta fuerít*), 1758. The early line *sit* (Wikisource, 1715, 1747, 1750).
   **Apply:** `Jas.2.22` la: `fides perfecta sit.` → `fides perfecta fuerit.`
4. **James 2:22** *ut fides ejus opera adjuvaret* → *adjuverit*. 1573 *Vides, vt fides eius opera adiuuerit, vtque* (canvas 918), the perfect matching *fuerit*; 1758 (OCR *adjuyerit*). **1556** *adiuuaret* (OCR), with Wikisource, 1715, 1747, 1750: a 1573 change (section 5). For your eye.
   **Apply:** `Jas.2.22` la: `opera adjuvaret,` → `opera adjuverit,`
5. **James 2:23** *scriptum illud, quod sic se habet* → *quod sic habet*. 1573 *ſcriptum illud, quod / ſic habet: Credidit Abrahamus Deo* (canvas 918); 1556 (OCR *quod fic habet*), 1758. The early line *sic se habet* (Wikisource, 1681, 1715, 1747, 1750).
   **Apply:** `Jas.2.23` la: `quod sic se habet` → `quod sic habet`
6. **James 3:1** *scientes, nos esse graviores poenas daturos* → *nos graviores esse poenas*. 1573 *ſcientes / ᵃ nos grauiores eſſe pœnas daturos.* (canvas 918; *a* a note letter); 1556 (OCR *nos grauiores effe poenas*), 1758, 1681. The early line *esse graviores* (Wikisource, 1715, 1747, 1750).
   **Apply:** `Jas.3.1` la: `nos esse graviores poenas` → `nos graviores esse poenas`
7. **James 4:11** *Fratres, nolite alius alii detrahere* → *Nolite alius alii detrahere*. 1573 *& vos euehet. Nolite alius a-/lij detrahere. Qui fratri detrahit* (canvas 918, end of its verse 10; no *Fratres* before or after); 1556 (OCR *Nolite alíus alij detrahere*), 1758. The early line has it (Wikisource, 1681, 1747, 1750; 1715's OCR does not reach it), as the Greek (Μὴ καταλαλεῖτε ἀλλήλων, ἀδελφοί) and the Vulgate (*fratres*). For your eye: Castellio's two last texts both drop the vocative the Greek has; the capital follows the draft's verse openings.
   **Apply:** `Jas.4.11` la: `Fratres, nolite alius alii detrahere:` → `Nolite alius alii detrahere:`
8. **James 5:16** *efficitque viri boni precatio* → *efficitque justi precatio*. 1573 *Multum valet efficitq; iuſti pre-/catio.* (canvas 919), δέησις δικαίου; 1556 (OCR *fufti precatio*), 1758. The early line *viri boni* (Wikisource, 1715, 1747, 1750).
   **Apply:** `Jas.5.16` la: `efficitque viri boni precatio.` → `efficitque justi precatio.`

## 2a. Found by the f/s sweep (0)

None: every *f* and *s* word whose other form is Latin was read in its verse, and on the image where 1573's OCR has
the other letter (intro). No decision needed.

## 2b. Found where 1573 was not aligned (0)

The three uncovered verses (1:23, 3:16, 4:10) were read whole on the image (intro): none differs from the draft but
in spelling. The *Fratres* of 4:11 (section 2, item 7) was found by reading 4:10–11 against the page text. No
decision needed.

## 2c. Verse boundaries (0)

1573's 4:11 starts at *Quod si legem damnas* (intro); the KJV's, and the draft's, at the clause before. Kept (decision
5). No decision needed.

## 2d. Castellio's L. … G. marks: 5:3 (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; read on the 1573 page image)

1. **James 5:3** *consumet, L. poenam G. vobis congessistis* → *consumet, poenam vobis congessistis*. 1573 *in morem conſumet, L. Pœnam G. vobis congeſsiſtis / in vltimum tempus.* (canvas 919, on the image; *L.* and *G.* in italics) and 1556 (OCR *L, Poenam Gs,*) and 1681 (OCR *L. Poc-£n G.*) mark *Poenam* as taken from the Latin (the Vulgate *Thesaurizastis vobis iram*; the Greek ἐθησαυρίσατε has no object); 1758, 1715, 1747, 1750 and 1726 print the word without the marks. Wikisource prints the marks with a lower-case *poenam*. Your decision on Matt 19:4 (*keep unmarked*), as 2 Tim 3:4 (`data/review/2tim1-4-stage2.md`), keeps the marked word and drops the marks; they stay on record in 1573's witness row (the aligner's `L…G` flag). The capital (1573, 1758, 1715, 1726 *Poenam*) is left to stage 3. For your eye.
   **Apply:** `Jas.5.3` la: `consumet, L. poenam G. vobis` → `consumet, poenam vobis`

## 3. Word division (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12)

1. **James 1:24** *Deinde seipsum speculatus* → *se ipsum*. Your settled *sē ipsum* (28×) against *seipsum* 4×, as 1 Tim 2:6. Not a quotation. 1573 joins it (*ſeipſum*, canvas 917, on the image); 1715 and 1747 lack the word.
   **Apply:** `Jas.1.24` la: `Deinde seipsum speculatus` → `Deinde se ipsum speculatus`

## 4. Checked and kept

- **4:10–11**: 1573 numbers 11 from *Quod si legem damnas* (intro); the KJV's boundary kept.
- **1:18** *nos genuit veritatis oratione*: 1573's OCR *&* is the note letter *b* (canvas 917, on the image; margin
  *b Euangelio*), as 1681 (*b veritatis*). Kept.
- **3:14** *nolite contra verum jactare vos*: 1573's OCR *&* is the note letter *c* (canvas 918, on the image; margin
  *c ita loqui, quasi istis vitijs careatis*), as 1556 (OCR *c íactare*). Kept.
- **1:22** *non eum dumtaxat audiatis*: 1573 *non eum dun-/taxat* (canvas 917, on the image; its OCR lost *dun-*).
  Spelling (*duntaxat*) to stage 3. Kept.
- **Edge places, printed in 1573** (on the image): 2:24 *non ſolum fide.* (a line the OCR lost), 4:7 *& is / vos
  fugiet:*, 4:11 *condemnator* (turned up at the end of the line above, *( condemnator.*); 1:27 *à múdo* (OCR). Kept.
- **1:24** *seipsum*: 1715 and 1747 omit it; 1573, 1556, 1758, 1750, 1726 have it. Kept (section 3 divides it).
- **4:5** *qui in vobis habitat*: 1715, 1747 *in vos*; 1573, 1758, 1750 *vobis*, 1556 (OCR *ínuobis*). Kept.
- **3:6** *et ipsa a geenna inflammanda*: 1573 *& ipſa à Gehen-/na* (canvas 918, on the image), 1556 (OCR *ipfaá …
  Ciehenna*); 1681, 1747 *ipsa gehenna* without *a*. The *a* kept; the spelling *geenna* to section 6.
- **2:13** *qui pietatem non exercuerit: at pietas judicio insultat*, **3:17** *pietate bonisque referta fructibus*:
  1573 prints *pietatem … pietas* and *pietate* (canvases 917–918, on the image), with Wikisource and the other
  printings; 1556's OCR *misericordiam … misericordia*, *misericordia* (section 5). Kept.
- **2:8** *Siquidem legi paretis*: 1573 *Si quidem* (canvas 917), with 1715, 1726; Wikisource and 1750 join it. One
  word or two, the same sense (εἰ μέντοι); your settled text has neither. Kept, for your eye.
- **2:8** *alterum ut teipsum diligito*: 1573 *teipſum*; kept joined as a quotation (Lev 19:18), as Rom 13:9 and Gal
  5:14.
- **3:12** *Potestne*: 1573 *Poteſt'ne*, 1556, 1715, 1747, 1726 apart. Kept joined, as Wikisource, 1758, 1681.
- **1:22** *vos ipsos*: 1573 *voſipſos*; the draft already divides it. Kept.
- **1:2** *quum*, **4:16** *ejusmodi*, **1:13** *Nemo dum*, **2:20** *Vis autem*: 1573's spacing or spelling differs; kept.
- **Note letters and margin notes**, not text: 1:17 *a* (*species*), 1:18 *b* (*Euangelio*), 1:25 *c* (*quæ liberos
  facit*), 2:4 *a* (OCR *perſonaru rationem ha… iudicaſtis*), 2:13 *b* (*iudicium non metuit, vtpote innocentia tuta
  aduersum pœnas*), 3:1 *a*, 3:3 *De lingua*, 3:6 *b* (*… vt si dicas scelerum mare, scelerum Oceanus*), 3:14 *c*,
  5:12 *a* (*simpliciter constanterque & vera affir…*, OCR *… negate*), 5:20 *b* (OCR *in causa fuisse …*); the
  references (as the OCR reads them: 1:12 *Esch14.18*, 1:19 *Prou.17.27*, 2:9 *Mar.22.39*, 2:25 *Iof.2.1*, 4:6
  *Prou.3.34*, 4:8 *Zachar.1.3*, 4:10 *1. Petr.5.6*, 4:12 *Rom.14.4*, 5:12 *Mat.5.34*, 5:17 *3.Reg.17.1*,
  *Luc.4.25*, 5:18 *3.Reg.1.18*);
  the chapter summaries; the running head (2:21); and 1573's annotations after chapters 1–4 (the second on 2:18,
  *χωρὶς τῶν ἔργων*).
- **Punctuation and capitals, left to stage 3**: 1:5 *exprobrat:* (1573 a comma), 2:3 *dicatis;* (1573 a colon),
  2:14 *habeat?* (1573 *?*), 2:23 *Dei amicus* (1573 *dei*), 4:11 *detrahere:* (1573 a stop), 4:12 *(atque judex)*
  (1573, 1556, 1758, 1681 without the parentheses; 1715, 1747, 1750 with them), 5:3 *poenam* (1573 *Pœnam*), 5:6
  *Condemnastis* (1573 *condemnaſtis*).
- **Spellings, left to stage 3** (decisions 37, 41 and 42's rules, and section 6): *quum*, *Quum* (1573 *cùm*,
  *Cùm*), *carissimi* (1573 *chariſsimi*), *umquam*, *quemquam*, *quocumque*, *tamquam* (1573 *vnquam*, *quenquam*,
  *quocunq;*, *tanquam*), *quidquam* (1573 *quicquam*), *tentationem*, *tentari*, *tentatur*, *tentat*, *adlectus*,
  *adsequi*, *adflictate*, *Adfligitur*, *adlevabit* (1573 *allectus*, *aſſequi*, *afflictate*, *Affligitur*,
  *alleuabit*), *exsequitur*, *exsecramur*, *exsecratione*, *exsecutor* (1573 *exequitur*, *execr-*, *executor*),
  *exspectat*, *exstat* (1573 *expectat*, *extat*), *paullisper* (1573 *pauliſper*), *quotidianoque*, *intelligere*,
  *intelligens*, *Intelligentes*, *Intelligat*, *heredesque* (1573 *hæredesq;*), *litteris* (1573 *literis*), *nuntiis*
  (1573 *nuncijs*), *dumtaxat* (1573 *duntaxat*), *annulos* (1573 and 1556 *anulos*; your settled *annul-* 4×, Gaffiot
  *ānulus*), *Submittite* (1573 *Sũmittite*, 1556, 1758, 1681, 1747 *Summittite*; your settled text has both
  *submitt-* 3× and *summitt-* 2×), *frenat*, *frenare*, *Frenos*, *effrenatum* (1573 *fræn-*), *feminae* (1573
  *fœminæ*), *caelum* (1573 *cœlum*), *maerorem* (1573 *mœrorem*), *geenna* (section 6), *eis*, *Jesu*, *Jobi*.

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656, pages 10282439–41), not the page image.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| Jas 1:3 | *fidei vestrae exploratione* | = | OCR *fiducia uefira exploratíone* (perhaps *fiduciae vestrae*; doubtful) | every other printing with 1573 |
| Jas 1:4 | *perfectum opus habeat* | = | *perfectam actionem habeat* | Wikisource, 1750 with 1556; 1758, 1681 with 1573 |
| Jas 2:13 | *qui pietatem non exercuerit: at pietas judicio insultat* | = | *qui misericordiam non exercuerit: at misericordia iudicio* (OCR *mife rícordíam … míferícordías iudi*) | Wikisource and the other printings with 1573 |
| Jas 2:22 | *opera adjuverit* | = | *opera adiuuaret* | Wikisource, 1715, 1747, 1750 with 1556; 1758 with 1573 |
| Jas 3:17 | *pietate bonisque referta fructibus* | = | *misericordia bo[nisque referta] fructib[us]* (OCR *miferícordia bores fructib.*) | Wikisource and the other printings with 1573 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-12; 1:3 recorded
as doubtful, the OCR alone)

## 6. Spelling rules proposed

Decision 37 assimilates *ad-* (compounds of *sum*, *adnuntio* and names excepted) and writes *tempto*, word by word;
these James forms have no row in `data/rules/orthography.tsv` yet (checked with `normalize.propose()` on the draft).
Proposed, not written to the file:

| old | new | scope | Where | Evidence |
|---|---|---|---|---|
| adlectus | allectus | word | 1:14 | 1573 *allectus* (canvas 917); 1556 (*allectus*), 1758, 1715, 1747, 1726 |
| adsequi | assequi | word | 4:2 | 1573 *aſſequi* (canvas 918); 1758, 1715; your settled *assequ-*; as the approved *adsequar → assequar* |
| adflictate | afflictate | word | 4:9 | 1573 *afflictate* (canvas 918); 1556 (OCR *atflíctate*), 1758; your settled *afflīct-*; as the approved *adflictis → afflictis* |
| adfligitur | affligitur | word | 5:13 | 1573 *Affligitur* (canvas 919); 1556, 1758, 1715; your settled *afflīg-*; as the approved *adfligimur → affligimur* |
| adlevabit | allevabit | word | 5:15 (after section 1's item 8) | 1573 *alleuabit* (canvas 919); 1556, 1758, 1681, 1715, 1747; your settled *allevāvit* 5×; as the approved *adlevavit → allevavit* |
| tentatur | temptatur | word | 1:13 (2×), 1:14 | decision 37 (*tempto*); as the approved *tentari → temptari*, *tentaretur → temptaretur* |
| tentat | temptat | word | 1:13 | decision 37 (*tempto*); as the approved *tentavit → temptavit* |
| geenna | gehenna | word | 3:6 | 1573 *Gehen-na* (canvas 918, on the image); 1556 (OCR *Ciehenna*), 1681, 1747 *gehenna*; your settled *gehenna*, *gehennam* 11×, none *geenn-*; Gaffiot *gehenna* |

(*adest*, *adhibemus*, *adipiscimini*, *admissis*, *adulterato*, *adventus*, *adversatur*, *advocet*, *adjuverit* do not
assimilate.)

**Decision:** accept (Claude, 2026-11-12, under decisions 37 and 42; added to `data/rules/orthography.tsv`)
