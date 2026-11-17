# Paragraphs over 250 words: breaks proposed

Built 2026-11-16 after your note on Leviticus 13 (59 verses, one break). Decision 52 (brief.md): a paragraph of
more than about 250 words is split where SBLGNT, or the BSB and WEB together, break and the Latin's sentence ends.

## What was found

- 24 settled paragraphs are over 250 words: 13 in Leviticus, 5 in Exodus, 4 in Genesis, one each in Acts, John,
  2 Corinthians. Leviticus 13:1–46 is 750 words, 11:1–47 691, 16:1–34 595, 4:1–35 550.
- Why: Leviticus was paragraphed at the BSB's section headings, not its paragraphs. Of its 77 paragraphs, 70 begin
  at one of the BSB's 70 headings; the BSB has 378 paragraph breaks (`\b \m`) in the book. Exodus is closer (141
  paragraphs, 114 at headings, of 583 BSB breaks); Genesis and the NT use about half the BSB's breaks (Genesis 403
  of 752, Matthew 263 of 537), which is why their paragraphs read well.
- The 250-word rule itself is not in the pipeline's code; it was applied by hand in each review, and in Leviticus
  only five times (6:19, 7:35, 26:27, 27:14, 27:22).

## How the breaks were chosen

At a verse where the BSB (`\p`, or `\b \m`) and the WEB both start a paragraph, and the Latin's verse before it
ends with `.`, `?` or `!`; none leaving a paragraph under 40 words. Inside a speech (God's laws, Peter at Acts 3)
the new paragraph reopens with “, as the settled text does (Lev 2:1, 7:1; Exod 23:10). Four long paragraphs have no
such place and are left alone: Gen 44:18–34 (Judah's speech: the WEB never breaks), Gen 46:7–27 (the list of Jacob's
family), Gen 49:1–27 (Jacob's blessing, poetry), Exod 15:1–19 (the song, poetry). 2 Cor 7:5–16 (255 words) has one
agreed break, at 7:8, but the Latin's sentence runs on there.

Each item can be accepted or left out on its own (`accept 1, 3–5`, `accept all except 7`).

**Decision:** accept all (Nathan, 2026-11-16: "3. A"; the wider re-paragraphing of the law books, option B, not taken now)

1. **Acts 3:11–26** (278 words): 1 breaks, at 3:17.
   **Apply:** `Acts.3.17` la: `\v 17 Et nunc,` → `\p \v 17 “Et nunc,`  (inside the speech: reopens with “)

2. **Exod 21:12–36** (363 words): 4 breaks, at 21:15, 21:20, 21:26, 21:33.
   **Apply:** `Exod.21.15` la: `\v 15 Quī patrem` → `\p \v 15 “Quī patrem`  (inside the speech: reopens with “)
   **Apply:** `Exod.21.20` la: `\v 20 Sī quis` → `\p \v 20 “Sī quis`  (inside the speech: reopens with “)
   **Apply:** `Exod.21.26` la: `\v 26 Sī quis` → `\p \v 26 “Sī quis`  (inside the speech: reopens with “)
   **Apply:** `Exod.21.33` la: `\v 33 Sī quis` → `\p \v 33 “Sī quis`  (inside the speech: reopens with “)

3. **Exod 22:1–15** (254 words): 2 breaks, at 22:5, 22:10.
   **Apply:** `Exod.22.5` la: `\v 5 Sī quis` → `\p \v 5 “Sī quis`  (inside the speech: reopens with “)
   **Apply:** `Exod.22.10` la: `\v 10 Sī quis` → `\p \v 10 “Sī quis`  (inside the speech: reopens with “)

4. **Exod 29:5–30** (415 words): 3 breaks, at 29:15, 29:19, 29:26.
   **Apply:** `Exod.29.15` la: `\v 15 Posteā arietem` → `\p \v 15 “Posteā arietem`  (inside the speech: reopens with “)
   **Apply:** `Exod.29.19` la: `\v 19 Deinde alterum` → `\p \v 19 “Deinde alterum`  (inside the speech: reopens with “)
   **Apply:** `Exod.29.26` la: `\v 26 Posteā sūmitō` → `\p \v 26 “Posteā sūmitō`  (inside the speech: reopens with “)

5. **Exod 34:10–28** (345 words): 3 breaks, at 34:17, 34:21, 34:25.
   **Apply:** `Exod.34.17` la: `\v 17 Deum cōnflātilem` → `\p \v 17 “Deum cōnflātilem`  (inside the speech: reopens with “)
   **Apply:** `Exod.34.21` la: `\v 21 Sex diēbus` → `\p \v 21 “Sex diēbus`  (inside the speech: reopens with “)
   **Apply:** `Exod.34.25` la: `\v 25 Cum meæ` → `\p \v 25 “Cum meæ`  (inside the speech: reopens with “)

6. **Gen 33:1–17** (301 words): 3 breaks, at 33:4, 33:8, 33:15.
   **Apply:** `Gen.33.4` la: `\v 4 Tum Ēsāus` → `\p \v 4 Tum Ēsāus`
   **Apply:** `Gen.33.8` la: `\v 8 Tum Ēsāus:` → `\p \v 8 Tum Ēsāus:`
   **Apply:** `Gen.33.15` la: `\v 15 At Ēsāus:` → `\p \v 15 At Ēsāus:`

7. **John 10:22–39** (251 words): 2 breaks, at 10:31, 10:34.
   **Apply:** `John.10.31` la: `\v 31 Hīc Jūdæī` → `\p \v 31 Hīc Jūdæī`
   **Apply:** `John.10.34` la: `\v 34 Et Jēsūs` → `\p \v 34 Et Jēsūs`

8. **John 19:1–15** (253 words): 4 breaks, at 19:6, 19:8, 19:11, 19:13.
   **Apply:** `John.19.6` la: `\v 6 At pontificēs` → `\p \v 6 At pontificēs`
   **Apply:** `John.19.8` la: `\v 8 Hāc vōce` → `\p \v 8 Hāc vōce`
   **Apply:** `John.19.11` la: `\v 11 Respondit Jēsūs:` → `\p \v 11 Respondit Jēsūs:`
   **Apply:** `John.19.13` la: `\v 13 Hāc audītā` → `\p \v 13 Hāc audītā`

9. **Lev 1:1–17** (263 words): 2 breaks, at 1:10, 1:14.
   **Apply:** `Lev.1.10` la: `\v 10 Sīn ex` → `\p \v 10 “Sīn ex`  (inside the speech: reopens with “)
   **Apply:** `Lev.1.14` la: `\v 14 Sīn ex` → `\p \v 14 “Sīn ex`  (inside the speech: reopens with “)

10. **Lev 4:1–35** (550 words): 4 breaks, at 4:13, 4:22, 4:27, 4:32.
   **Apply:** `Lev.4.13` la: `\v 13 Sīn autem` → `\p \v 13 “Sīn autem`  (inside the speech: reopens with “)
   **Apply:** `Lev.4.22` la: `\v 22 Sī quis` → `\p \v 22 “Sī quis`  (inside the speech: reopens with “)
   **Apply:** `Lev.4.27` la: `\v 27 Item sī` → `\p \v 27 “Item sī`  (inside the speech: reopens with “)
   **Apply:** `Lev.4.32` la: `\v 32 Quod sī` → `\p \v 32 “Quod sī`  (inside the speech: reopens with “)

11. **Lev 5:1–13** (295 words): 2 breaks, at 5:7, 5:11.
   **Apply:** `Lev.5.7` la: `\v 7 Quod sī` → `\p \v 7 “Quod sī`  (inside the speech: reopens with “)
   **Apply:** `Lev.5.11` la: `\v 11 Quod sī` → `\p \v 11 “Quod sī`  (inside the speech: reopens with “)

12. **Lev 9:1–24** (368 words): 3 breaks, at 9:5, 9:8, 9:23.
   **Apply:** `Lev.9.5` la: `\v 5 Tum illī` → `\p \v 5 Tum illī`
   **Apply:** `Lev.9.8` la: `\v 8 Tum Aharōn` → `\p \v 8 Tum Aharōn`
   **Apply:** `Lev.9.23` la: `\v 23 Tum ingressī` → `\p \v 23 Tum ingressī`

13. **Lev 11:1–47** (691 words): 7 breaks, at 11:4, 11:9, 11:13, 11:24, 11:29, 11:39, 11:41.
   **Apply:** `Lev.11.4` la: `\v 4 Sed sunt` → `\p \v 4 “Sed sunt`  (inside the speech: reopens with “)
   **Apply:** `Lev.11.9` la: `\v 9 Item dē` → `\p \v 9 “Item dē`  (inside the speech: reopens with “)
   **Apply:** `Lev.11.13` la: `\v 13 Dē volucribus` → `\p \v 13 “Dē volucribus`  (inside the speech: reopens with “)
   **Apply:** `Lev.11.24` la: `\v 24 Quisquis eōrum` → `\p \v 24 “Quisquis eōrum`  (inside the speech: reopens with “)
   **Apply:** `Lev.11.29` la: `\v 29 Atque hæc` → `\p \v 29 “Atque hæc`  (inside the speech: reopens with “)
   **Apply:** `Lev.11.39` la: `\v 39 Quod sī` → `\p \v 39 “Quod sī`  (inside the speech: reopens with “)
   **Apply:** `Lev.11.41` la: `\v 41 Quidquid humī` → `\p \v 41 “Quidquid humī`  (inside the speech: reopens with “)

14. **Lev 13:1–46** (750 words): 6 breaks, at 13:9, 13:12, 13:18, 13:24, 13:29, 13:38.
   **Apply:** `Lev.13.9` la: `\v 9 Lepræ affectus` → `\p \v 9 “Lepræ affectus`  (inside the speech: reopens with “)
   **Apply:** `Lev.13.12` la: `\v 12 Sīn autem` → `\p \v 12 “Sīn autem`  (inside the speech: reopens with “)
   **Apply:** `Lev.13.18` la: `\v 18 Sī quō` → `\p \v 18 “Sī quō`  (inside the speech: reopens with “)
   **Apply:** `Lev.13.24` la: `\v 24 Sī cujus` → `\p \v 24 “Sī cujus`  (inside the speech: reopens with “)
   **Apply:** `Lev.13.29` la: `\v 29 Sī cujus` → `\p \v 29 “Sī cujus`  (inside the speech: reopens with “)
   **Apply:** `Lev.13.38` la: `\v 38 Sī quis` → `\p \v 38 “Sī quis`  (inside the speech: reopens with “)

15. **Lev 14:1–32** (520 words): 4 breaks, at 14:8, 14:10, 14:21, 14:23.
   **Apply:** `Lev.14.8` la: `\v 8 Pūrificandus autem` → `\p \v 8 “Pūrificandus autem`  (inside the speech: reopens with “)
   **Apply:** `Lev.14.10` la: `\v 10 Octāvō diē` → `\p \v 10 “Octāvō diē`  (inside the speech: reopens with “)
   **Apply:** `Lev.14.21` la: `\v 21 Quod sī` → `\p \v 21 “Quod sī`  (inside the speech: reopens with “)
   **Apply:** `Lev.14.23` la: `\v 23 Hæc diē` → `\p \v 23 “Hæc diē`  (inside the speech: reopens with “)

16. **Lev 16:1–34** (595 words): 6 breaks, at 16:11, 16:15, 16:20, 16:23, 16:26, 16:29.
   **Apply:** `Lev.16.11` la: `\v 11 Tum suum` → `\p \v 11 “Tum suum`  (inside the speech: reopens with “)
   **Apply:** `Lev.16.15` la: `\v 15 Tum populī` → `\p \v 15 “Tum populī`  (inside the speech: reopens with “)
   **Apply:** `Lev.16.20` la: `\v 20 Postquam sacrārium` → `\p \v 20 “Postquam sacrārium`  (inside the speech: reopens with “)
   **Apply:** `Lev.16.23` la: `\v 23 Deinde veniat` → `\p \v 23 “Deinde veniat`  (inside the speech: reopens with “)
   **Apply:** `Lev.16.26` la: `\v 26 Quī autem` → `\p \v 26 “Quī autem`  (inside the speech: reopens with “)
   **Apply:** `Lev.16.29` la: `\v 29 Hoc īnstitūtō` → `\p \v 29 “Hoc īnstitūtō`  (inside the speech: reopens with “)

17. **Lev 18:1–30** (407 words): 6 breaks, at 18:6, 18:10, 18:13, 18:17, 18:19, 18:24.
   **Apply:** `Lev.18.6` la: `\v 6 Ad cōnsanguineum` → `\p \v 6 “Ad cōnsanguineum`  (inside the speech: reopens with “)
   **Apply:** `Lev.18.10` la: `\v 10 Neptis tuæ,` → `\p \v 10 “Neptis tuæ,`  (inside the speech: reopens with “)
   **Apply:** `Lev.18.13` la: `\v 13 Māterteræ tuæ` → `\p \v 13 “Māterteræ tuæ`  (inside the speech: reopens with “)
   **Apply:** `Lev.18.17` la: `\v 17 Cum muliere,` → `\p \v 17 “Cum muliere,`  (inside the speech: reopens with “)
   **Apply:** `Lev.18.19` la: `\v 19 Ad mulierem` → `\p \v 19 “Ad mulierem`  (inside the speech: reopens with “)
   **Apply:** `Lev.18.24` la: `\v 24 Nē vōs` → `\p \v 24 “Nē vōs`  (inside the speech: reopens with “)

18. **Lev 19:19–37** (268 words): 4 breaks, at 19:23, 19:26, 19:30, 19:35.
   **Apply:** `Lev.19.23` la: `\v 23 Cum autem` → `\p \v 23 “Cum autem`  (inside the speech: reopens with “)
   **Apply:** `Lev.19.26` la: `\v 26 Nē quid` → `\p \v 26 “Nē quid`  (inside the speech: reopens with “)
   **Apply:** `Lev.19.30` la: `\v 30 Sabbata mea` → `\p \v 30 “Sabbata mea`  (inside the speech: reopens with “)
   **Apply:** `Lev.19.35` la: `\v 35 In jūdiciō,` → `\p \v 35 “In jūdiciō,`  (inside the speech: reopens with “)

19. **Lev 22:1–16** (253 words): 2 breaks, at 22:4, 22:10.
   **Apply:** `Lev.22.4` la: `\v 4 Quisquis dē` → `\p \v 4 “Quisquis dē`  (inside the speech: reopens with “)
   **Apply:** `Lev.22.10` la: `\v 10 Aliēnus nēmō` → `\p \v 10 “Aliēnus nēmō`  (inside the speech: reopens with “)

20. **Lev 22:17–33** (259 words): 1 breaks, at 22:26.
   **Apply:** `Lev.22.26` la: `\v 26 “Bōs autem,”` → `\p \v 26 “Bōs autem,”`

