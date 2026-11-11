# *quum* or *cum*? The conjunction in the settled chapters

Found 2026-11-11 (Nathan asked why Exod 4:3 reads *Quumque*). The settled text spells the conjunction two ways:

- **cum** throughout the chapters from the earlier repo work: Matthew, Mark, Luke, John and Genesis 1–27 (no *quum*).
- **quum** in 243 places in the chapters drafted from Wikisource by the pipeline: Genesis 28–50 (47), Exodus 1–20
  (57), Acts (70), Romans (27), 1 Corinthians (26), 2 Corinthians (16). Wikisource prints *quum* there (Gen 46×,
  Acts 72× in `data/witnesses/wikisource/`), as the early modern printings do, and the drafts kept it.

## Why it was not normalized

The spelling rules (`data/rules/orthography.tsv`) were learned by `pipeline rules` from the differences between
Wikisource and the settled text of the time. Wikisource's Gospels already write *cum* (0 *quum* in
`data/witnesses/wikisource/Matt.tsv`), so *quum* → *cum* never appeared as a difference and no rule was made. Nor
did the review of the new chapters flag it: the proposals checked macrons, layout and readings, not this spelling.

## What the sources say

- **Gaffiot 2016** (`python -m pipeline latin macron quum`): points *quum* to *cum*, its headword for the conjunction.
- **Whitaker** (same lookup): *quum*, "Republican Latin form of cum".
- The brief: "Classical spellings as Gaffiot heads them".

## Recommendation

**cum** everywhere (and *cumque* for *quumque*, as Matt–John already write *Cumque* 11×), by the 243 items below;
and a rule `quum → cum` (word scope, with *quumque* → *cumque*) in `data/rules/orthography.tsv`, so the drafts to
come are normalized (added there as `proposed`; it becomes `approved` with this decision). Words that only contain
the letters (*æquum*, *inīquum*) are untouched: each Apply line names its own verse and matches once there.

## The settled places (243)

**Decision:** accept all (Nathan, 2026-11-11: "Yes, apply it")

1. *quum* → *cum*
   **Apply:** `Gen.36.24` la: `quum` → `cum`
2. *quum* → *cum*
   **Apply:** `Gen.37.4` la: `quum` → `cum`
3. *quum* → *cum*
   **Apply:** `Gen.37.10` la: `quum` → `cum`
4. *quum* → *cum*
   **Apply:** `Gen.37.29` la: `quum` → `cum`
5. *Quumque* → *Cumque*
   **Apply:** `Gen.37.35` la: `Quumque` → `Cumque`
6. *quum* → *cum*
   **Apply:** `Gen.38.2` la: `quum` → `cum`
7. *Quumque* → *Cumque*
   **Apply:** `Gen.38.21` la: `Quumque` → `Cumque`
8. *quum* → *cum*
   **Apply:** `Gen.38.25` la: `quum` → `cum`
9. *quum* → *cum*
   **Apply:** `Gen.38.29` la: `quum` → `cum`
10. *quum* → *cum*
   **Apply:** `Gen.39.3` la: `quum` → `cum`
11. *quum* → *cum*
   **Apply:** `Gen.39.14` la: `quum` → `cum`
12. *quum* → *cum*
   **Apply:** `Gen.40.13` la: `quum essēs` → `cum essēs`
13. *quum* → *cum*
   **Apply:** `Gen.40.14` la: `quum` → `cum`
14. *quum* → *cum*
   **Apply:** `Gen.40.20` la: `quum` → `cum`
15. *quum* → *cum*
   **Apply:** `Gen.41.8` la: `quum` → `cum`
16. *Quum* → *Cum*
   **Apply:** `Gen.41.10` la: `Quum` → `Cum`
17. *quum* → *cum*
   **Apply:** `Gen.41.12` la: `quum` → `cum`
18. *quum* → *cum*
   **Apply:** `Gen.41.18` la: `“quum` → `“cum`
19. *quum* → *cum*
   **Apply:** `Gen.41.21` la: `quum` → `cum`
20. *quum* → *cum*
   **Apply:** `Gen.41.46` la: `quum` → `cum`
21. *quum* → *cum*
   **Apply:** `Gen.41.54` la: `quum` → `cum`
22. *quum* → *cum*
   **Apply:** `Gen.42.1` la: `quum` → `cum`
23. *quum* → *cum*
   **Apply:** `Gen.42.21` la: `quum animī` → `cum animī`
24. *quum* → *cum*
   **Apply:** `Gen.42.21` la: `quum ab` → `cum ab`
25. *quum* → *cum*
   **Apply:** `Gen.42.27` la: `quum` → `cum`
26. *quum* → *cum*
   **Apply:** `Gen.42.31` la: `quum` → `cum`
27. *quum* → *cum*
   **Apply:** `Gen.42.35` la: `quum` → `cum`
28. *quum* → *cum*
   **Apply:** `Gen.43.18` la: `quum` → `cum`
29. *quum* → *cum*
   **Apply:** `Gen.43.21` la: `quum` → `cum`
30. *quum* → *cum*
   **Apply:** `Gen.44.3` la: `quum` → `cum`
31. *Quum* → *Cum*
   **Apply:** `Gen.44.19` la: `Quum` → `Cum`
32. *Quumque* → *Cumque*
   **Apply:** `Gen.44.25` la: `Quumque` → `Cumque`
33. *quum* → *cum*
   **Apply:** `Gen.44.27` la: `quum` → `cum`
34. *quum* → *cum*
   **Apply:** `Gen.45.1` la: `quum` → `cum`
35. *Quumque* → *Cumque*
   **Apply:** `Gen.45.4` la: `Quumque` → `Cumque`
36. *quum* → *cum*
   **Apply:** `Gen.45.27` la: `quum` → `cum`
37. *quum* → *cum*
   **Apply:** `Gen.47.13` la: `quum` → `cum`
38. *quumque* → *cumque*
   **Apply:** `Gen.47.28` la: `quumque` → `cumque`
39. *quum* → *cum*
   **Apply:** `Gen.47.30` la: `quum` → `cum`
40. *quum* → *cum*
   **Apply:** `Gen.48.7` la: `quum` → `cum`
41. *quumque* → *cumque*
   **Apply:** `Gen.48.10` la: `quumque` → `cumque`
42. *quum* → *cum*
   **Apply:** `Gen.48.13` la: `quum` → `cum`
43. *quum* → *cum*
   **Apply:** `Gen.49.23` la: `quum` → `cum`
44. *Quumque* → *Cumque*
   **Apply:** `Gen.50.6` la: `Quumque` → `Cumque`
45. *quum* → *cum*
   **Apply:** `Gen.50.15` la: `quum` → `cum`
46. *quum* → *cum*
   **Apply:** `Gen.50.18` la: `quum` → `cum`
47. *quum* → *cum*
   **Apply:** `Gen.50.25` la: `quum` → `cum`
48. *quum* → *cum*
   **Apply:** `Exod.2.2` la: `quum` → `cum`
49. *quum* → *cum*
   **Apply:** `Exod.2.3` la: `quum` → `cum`
50. *quum* → *cum*
   **Apply:** `Exod.2.11` la: `quum` → `cum`
51. *quum* → *cum*
   **Apply:** `Exod.2.12` la: `quum` → `cum`
52. *quum* → *cum*
   **Apply:** `Exod.2.15` la: `quum` → `cum`
53. *quum* → *cum*
   **Apply:** `Exod.2.17` la: `quum` → `cum`
54. *Quum* → *Cum*
   **Apply:** `Exod.3.1` la: `Quum` → `Cum`
55. *Quum* → *Cum*
   **Apply:** `Exod.3.7` la: `“Quum` → `“Cum`
56. *Quumque* → *Cumque*
   **Apply:** `Exod.4.3` la: `Quumque` → `Cumque`
57. *quum* → *cum*
   **Apply:** `Exod.4.4` la: `quum` → `cum`
58. *Quum* → *Cum*
   **Apply:** `Exod.4.21` la: `“Quum` → `“Cum`
59. *Quumque* → *Cumque*
   **Apply:** `Exod.4.28` la: `Quumque` → `Cumque`
60. *quum* → *cum*
   **Apply:** `Exod.5.13` la: `quum` → `cum`
61. *quum* → *cum*
   **Apply:** `Exod.5.20` la: `quum` → `cum`
62. *quum* → *cum*
   **Apply:** `Exod.6.30` la: `quum` → `cum`
63. *quum* → *cum*
   **Apply:** `Exod.7.5` la: `quum` → `cum`
64. *quum* → *cum*
   **Apply:** `Exod.7.7` la: `quum` → `cum`
65. *quum* → *cum*
   **Apply:** `Exod.7.17` la: `quum` → `cum`
66. *quum* → *cum*
   **Apply:** `Exod.7.20` la: `quum Mōsēs` → `cum Mōsēs`
67. *quumque* → *cumque*
   **Apply:** `Exod.7.20` la: `quumque` → `cumque`
68. *quum* → *cum*
   **Apply:** `Exod.7.22` la: `quum` → `cum`
69. *quum* → *cum*
   **Apply:** `Exod.8.18` la: `quum` → `cum`
70. *quum* → *cum*
   **Apply:** `Exod.9.7` la: `quum` → `cum`
71. *quum* → *cum*
   **Apply:** `Exod.9.10` la: `quum` → `cum`
72. *Quum* → *Cum*
   **Apply:** `Exod.9.26` la: `Quum` → `Cum`
73. *quum* → *cum*
   **Apply:** `Exod.10.13` la: `quum` → `cum`
74. *quum* → *cum*
   **Apply:** `Exod.10.20` la: `quum` → `cum`
75. *quum* → *cum*
   **Apply:** `Exod.10.23` la: `quum` → `cum`
76. *Quum* → *Cum*
   **Apply:** `Exod.11.7` la: `Quum` → `Cum`
77. *quum* → *cum*
   **Apply:** `Exod.12.23` la: `quum` → `cum`
78. *Quumque* → *Cumque*
   **Apply:** `Exod.12.25` la: `Quumque` → `Cumque`
79. *quum* → *cum*
   **Apply:** `Exod.12.27` la: `quum` → `cum`
80. *Quumque* → *Cumque*
   **Apply:** `Exod.12.28` la: `Quumque` → `Cumque`
81. *Quum* → *Cum*
   **Apply:** `Exod.13.5` la: `Quum` → `Cum`
82. *quum* → *cum*
   **Apply:** `Exod.13.8` la: `quum` → `cum`
83. *quum* → *cum*
   **Apply:** `Exod.13.19` la: `(quum` → `(cum`
84. *quum* → *cum*
   **Apply:** `Exod.14.21` la: `quum` → `cum`
85. *quum* → *cum*
   **Apply:** `Exod.14.27` la: `quum` → `cum`
86. *Quum* → *Cum*
   **Apply:** `Exod.14.29` la: `Quum` → `Cum`
87. *quum* → *cum*
   **Apply:** `Exod.14.30` la: `quum` → `cum`
88. *quum* → *cum*
   **Apply:** `Exod.15.19` la: `quum` → `cum`
89. *quum* → *cum*
   **Apply:** `Exod.16.3` la: `quum ōllīs` → `cum ōllīs`
90. *quum* → *cum*
   **Apply:** `Exod.16.3` la: `quum pānem` → `cum pānem`
91. *Quum* → *Cum*
   **Apply:** `Exod.16.8` la: `“Quum` → `“Cum`
92. *quum* → *cum*
   **Apply:** `Exod.16.18` la: `quum` → `cum`
93. *quum* → *cum*
   **Apply:** `Exod.16.20` la: `quum` → `cum`
94. *quum* → *cum*
   **Apply:** `Exod.16.22` la: `quum` → `cum`
95. *quum* → *cum*
   **Apply:** `Exod.16.24` la: `quum` → `cum`
96. *quum* → *cum*
   **Apply:** `Exod.17.1` la: `quum` → `cum`
97. *quum* → *cum*
   **Apply:** `Exod.17.2` la: `quum` → `cum`
98. *quum* → *cum*
   **Apply:** `Exod.17.12` la: `quum` → `cum`
99. *quumque* → *cumque*
   **Apply:** `Exod.18.7` la: `quumque` → `cumque`
100. *quum* → *cum*
   **Apply:** `Exod.18.13` la: `quum` → `cum`
101. *quum* → *cum*
   **Apply:** `Exod.19.8` la: `quum` → `cum`
102. *Quum* → *Cum*
   **Apply:** `Exod.19.13` la: `Quum` → `Cum`
103. *Quum* → *Cum*
   **Apply:** `Exod.19.20` la: `Quum` → `Cum`
104. *quum* → *cum*
   **Apply:** `Exod.20.11` la: `quum` → `cum`
105. *quum* → *cum*
   **Apply:** `Acts.1.15` la: `quum` → `cum`
106. *quum* → *cum*
   **Apply:** `Acts.2.1` la: `quum` → `cum`
107. *quum* → *cum*
   **Apply:** `Acts.2.30` la: `quum` → `cum`
108. *Quumque* → *Cumque*
   **Apply:** `Acts.3.5` la: `Quumque` → `Cumque`
109. *quum* → *cum*
   **Apply:** `Acts.3.13` la: `quum` → `cum`
110. *quum* → *cum*
   **Apply:** `Acts.3.20` la: `quum` → `cum`
111. *quum* → *cum*
   **Apply:** `Acts.5.23` la: `quum` → `cum`
112. *Quumque* → *Cumque*
   **Apply:** `Acts.6.9` la: `Quumque` → `Cumque`
113. *quum* → *cum*
   **Apply:** `Acts.7.2` la: `quum` → `cum`
114. *quum* → *cum*
   **Apply:** `Acts.7.5` la: `quum` → `cum`
115. *quum* → *cum*
   **Apply:** `Acts.7.15` la: `quum` → `cum`
116. *Quumque* → *Cumque*
   **Apply:** `Acts.7.24` la: `Quumque` → `Cumque`
117. *quum* → *cum*
   **Apply:** `Acts.7.45` la: `quum` → `cum`
118. *quum* → *cum*
   **Apply:** `Acts.8.6` la: `quum,` → `cum,`
119. *Quum* → *Cum*
   **Apply:** `Acts.8.12` la: `Quum` → `Cum`
120. *quum* → *cum*
   **Apply:** `Acts.8.33` la: `quum` → `cum`
121. *Quumque* → *Cumque*
   **Apply:** `Acts.8.36` la: `Quumque` → `Cumque`
122. *quum* → *cum*
   **Apply:** `Acts.9.24` la: `quum` → `cum`
123. *quum* → *cum*
   **Apply:** `Acts.9.39` la: `quum` → `cum`
124. *Quumque* → *Cumque*
   **Apply:** `Acts.10.17` la: `Quumque` → `Cumque`
125. *quum* → *cum*
   **Apply:** `Acts.10.30` la: `quum,` → `cum,`
126. *quum* → *cum*
   **Apply:** `Acts.10.39` la: `quum` → `cum`
127. *quum* → *cum*
   **Apply:** `Acts.12.3` la: `(quum` → `(cum`
128. *Quum* → *Cum*
   **Apply:** `Acts.12.6` la: `Quum` → `Cum`
129. *quum* → *cum*
   **Apply:** `Acts.12.19` la: `quum` → `cum`
130. *quum* → *cum*
   **Apply:** `Acts.13.3` la: `quum` → `cum`
131. *quum* → *cum*
   **Apply:** `Acts.13.25` la: `quum` → `cum`
132. *Quumque* → *Cumque*
   **Apply:** `Acts.14.5` la: `Quumque` → `Cumque`
133. *quum* → *cum*
   **Apply:** `Acts.15.2` la: `quum` → `cum`
134. *quum* → *cum*
   **Apply:** `Acts.15.9` la: `quum` → `cum`
135. *quum* → *cum*
   **Apply:** `Acts.15.24` la: `quum` → `cum`
136. *quum* → *cum*
   **Apply:** `Acts.16.20` la: `quum` → `cum`
137. *quum* → *cum*
   **Apply:** `Acts.16.22` la: `quum` → `cum`
138. *Quum* → *Cum*
   **Apply:** `Acts.17.23` la: `Quum` → `Cum`
139. *quum* → *cum*
   **Apply:** `Acts.17.24` la: `quum` → `cum`
140. *quum* → *cum*
   **Apply:** `Acts.17.25` la: `quum` → `cum`
141. *Quumque* → *Cumque*
   **Apply:** `Acts.17.26` la: `Quumque` → `Cumque`
142. *Quum* → *Cum*
   **Apply:** `Acts.17.28` la: `Quum` → `Cum`
143. *Quumque* → *Cumque*
   **Apply:** `Acts.18.6` la: `Quumque` → `Cumque`
144. *quum* → *cum*
   **Apply:** `Acts.18.14` la: `quum` → `cum`
145. *quum* → *cum*
   **Apply:** `Acts.18.18` la: `quum` → `cum`
146. *quum* → *cum*
   **Apply:** `Acts.19.2` la: `quum` → `cum`
147. *Quumque* → *Cumque*
   **Apply:** `Acts.19.6` la: `Quumque` → `Cumque`
148. *quum* → *cum*
   **Apply:** `Acts.19.34` la: `quum` → `cum`
149. *quum* → *cum*
   **Apply:** `Acts.19.36` la: `quum` → `cum`
150. *quum* → *cum*
   **Apply:** `Acts.19.40` la: `quum` → `cum`
151. *Quumque* → *Cumque*
   **Apply:** `Acts.20.8` la: `Quumque` → `Cumque`
152. *quum* → *cum*
   **Apply:** `Acts.21.34` la: `quum` → `cum`
153. *Quumque* → *Cumque*
   **Apply:** `Acts.21.40` la: `Quumque` → `Cumque`
154. *quum* → *cum*
   **Apply:** `Acts.22.11` la: `quum` → `cum`
155. *quum* → *cum*
   **Apply:** `Acts.22.20` la: `quum` → `cum`
156. *quum* → *cum*
   **Apply:** `Acts.22.29` la: `quum` → `cum`
157. *quum* → *cum*
   **Apply:** `Acts.23.27` la: `quum` → `cum`
158. *Quum* → *Cum*
   **Apply:** `Acts.23.30` la: `Quum` → `Cum`
159. *quum* → *cum*
   **Apply:** `Acts.24.10` la: `quum` → `cum`
160. *Quum* → *Cum*
   **Apply:** `Acts.24.18` la: `Quum` → `Cum`
161. *Quum* → *Cum*
   **Apply:** `Acts.24.22` la: `“Quum` → `“Cum`
162. *Quum* → *Cum*
   **Apply:** `Acts.25.17` la: `Quum` → `Cum`
163. *quum* → *cum*
   **Apply:** `Acts.25.18` la: `quum` → `cum`
164. *quum* → *cum*
   **Apply:** `Acts.25.25` la: `quum` → `cum`
165. *quum* → *cum*
   **Apply:** `Acts.27.9` la: `quum` → `cum`
166. *quum* → *cum*
   **Apply:** `Acts.27.15` la: `quum` → `cum`
167. *Quumque* → *Cumque*
   **Apply:** `Acts.27.16` la: `Quumque` → `Cumque`
168. *Quum* → *Cum*
   **Apply:** `Acts.27.21` la: `Quum` → `Cum`
169. *quum* → *cum*
   **Apply:** `Acts.27.27` la: `quum` → `cum`
170. *quum* → *cum*
   **Apply:** `Acts.27.30` la: `quum` → `cum`
171. *quum* → *cum*
   **Apply:** `Acts.27.33` la: `“quum` → `“cum`
172. *Quum* → *Cum*
   **Apply:** `Acts.28.3` la: `Quum` → `Cum`
173. *quum* → *cum*
   **Apply:** `Acts.28.15` la: `quum` → `cum`
174. *Quumque* → *Cumque*
   **Apply:** `Acts.28.25` la: `Quumque` → `Cumque`
175. *quum* → *cum*
   **Apply:** `Rom.1.16` la: `quum` → `cum`
176. *quum* → *cum*
   **Apply:** `Rom.1.19` la: `quum` → `cum`
177. *quum* → *cum*
   **Apply:** `Rom.1.32` la: `quum` → `cum`
178. *quum* → *cum*
   **Apply:** `Rom.2.1` la: `quum` → `cum`
179. *quum* → *cum*
   **Apply:** `Rom.2.10` la: `quum` → `cum`
180. *Quum* → *Cum*
   **Apply:** `Rom.2.14` la: `Quum` → `Cum`
181. *quum* → *cum*
   **Apply:** `Rom.4.10` la: `habitam? quum in` → `habitam? cum in`
182. *quum* → *cum*
   **Apply:** `Rom.4.10` la: `an quum in` → `an cum in`
183. *quum* → *cum*
   **Apply:** `Rom.5.6` la: `quum` → `cum`
184. *quum* → *cum*
   **Apply:** `Rom.5.7` la: `quum` → `cum`
185. *quum* → *cum*
   **Apply:** `Rom.5.8` la: `quum` → `cum`
186. *quum* → *cum*
   **Apply:** `Rom.5.10` la: `quum` → `cum`
187. *quum* → *cum*
   **Apply:** `Rom.6.14` la: `quum` → `cum`
188. *quum* → *cum*
   **Apply:** `Rom.6.17` la: `quum` → `cum`
189. *quum* → *cum*
   **Apply:** `Rom.6.20` la: `quum` → `cum`
190. *Quum* → *Cum*
   **Apply:** `Rom.7.5` la: `Quum` → `Cum`
191. *Quum* → *Cum*
   **Apply:** `Rom.9.9` la: `“Quum` → `“Cum`
192. *quum* → *cum*
   **Apply:** `Rom.10.12` la: `quum` → `cum`
193. *quum* → *cum*
   **Apply:** `Rom.10.18` la: `quum` → `cum`
194. *quum* → *cum*
   **Apply:** `Rom.13.4` la: `quum` → `cum`
195. *quum* → *cum*
   **Apply:** `Rom.13.11` la: `quum sciāmus,` → `cum sciāmus,`
196. *quum* → *cum*
   **Apply:** `Rom.13.11` la: `quum crēdidimus.` → `cum crēdidimus.`
197. *quum* → *cum*
   **Apply:** `Rom.14.3` la: `quum` → `cum`
198. *quum* → *cum*
   **Apply:** `Rom.14.10` la: `quum` → `cum`
199. *quum* → *cum*
   **Apply:** `Rom.15.23` la: `quum` → `cum`
200. *quum* → *cum*
   **Apply:** `Rom.15.29` la: `quum` → `cum`
201. *quum* → *cum*
   **Apply:** `Rom.16.2` la: `quum` → `cum`
202. *quum* → *cum*
   **Apply:** `1Cor.2.1` la: `quum` → `cum`
203. *quum* → *cum*
   **Apply:** `1Cor.3.3` la: `quum` → `cum`
204. *Quum* → *Cum*
   **Apply:** `1Cor.3.4` la: `Quum` → `Cum`
205. *Quum* → *Cum*
   **Apply:** `1Cor.4.13` la: `Quum` → `Cum`
206. *quum* → *cum*
   **Apply:** `1Cor.5.12` la: `quum` → `cum`
207. *quum* → *cum*
   **Apply:** `1Cor.7.14` la: `quum` → `cum`
208. *quum* → *cum*
   **Apply:** `1Cor.7.22` la: `quum` → `cum`
209. *quum* → *cum*
   **Apply:** `1Cor.9.16` la: `quum` → `cum`
210. *Quum* → *Cum*
   **Apply:** `1Cor.9.19` la: `Quum` → `Cum`
211. *quum* → *cum*
   **Apply:** `1Cor.9.27` la: `quum` → `cum`
212. *quum* → *cum*
   **Apply:** `1Cor.11.7` la: `quum` → `cum`
213. *Quum* → *Cum*
   **Apply:** `1Cor.11.9` la: `Quum` → `Cum`
214. *quum* → *cum*
   **Apply:** `1Cor.11.20` la: `quum` → `cum`
215. *quum* → *cum*
   **Apply:** `1Cor.11.21` la: `quum` → `cum`
216. *quum* → *cum*
   **Apply:** `1Cor.11.34` la: `quum` → `cum`
217. *quum* → *cum*
   **Apply:** `1Cor.12.2` la: `quum` → `cum`
218. *quum* → *cum*
   **Apply:** `1Cor.12.4` la: `quum` → `cum`
219. *quum* → *cum*
   **Apply:** `1Cor.12.5` la: `quum` → `cum`
220. *quum* → *cum*
   **Apply:** `1Cor.12.6` la: `quum` → `cum`
221. *quum* → *cum*
   **Apply:** `1Cor.12.12` la: `quum` → `cum`
222. *quum* → *cum*
   **Apply:** `1Cor.12.24` la: `quum` → `cum`
223. *quum* → *cum*
   **Apply:** `1Cor.13.10` la: `quum` → `cum`
224. *quum* → *cum*
   **Apply:** `1Cor.14.2` la: `quum` → `cum`
225. *quum* → *cum*
   **Apply:** `1Cor.14.16` la: `quum,` → `cum,`
226. *quum* → *cum*
   **Apply:** `1Cor.16.2` la: `quum` → `cum`
227. *quum* → *cum*
   **Apply:** `1Cor.16.12` la: `quum` → `cum`
228. *quum* → *cum*
   **Apply:** `2Cor.1.12` la: `quum` → `cum`
229. *Quum* → *Cum*
   **Apply:** `2Cor.2.12` la: `Quum` → `Cum`
230. *quum* → *cum*
   **Apply:** `2Cor.5.6` la: `quum` → `cum`
231. *quum* → *cum*
   **Apply:** `2Cor.5.19` la: `quum` → `cum`
232. *quum* → *cum*
   **Apply:** `2Cor.5.20` la: `quum` → `cum`
233. *quum* → *cum*
   **Apply:** `2Cor.6.9` la: `quum` → `cum`
234. *quum* → *cum*
   **Apply:** `2Cor.6.10` la: `quum` → `cum`
235. *quum* → *cum*
   **Apply:** `2Cor.7.5` la: `quum` → `cum`
236. *quum* → *cum*
   **Apply:** `2Cor.8.9` la: `quum` → `cum`
237. *quum* → *cum*
   **Apply:** `2Cor.8.22` la: `quum` → `cum`
238. *Quum* → *Cum*
   **Apply:** `2Cor.9.9` la: `“Quum` → `“Cum`
239. *quum* → *cum*
   **Apply:** `2Cor.10.6` la: `quum` → `cum`
240. *quum* → *cum*
   **Apply:** `2Cor.11.14` la: `quum` → `cum`
241. *quum* → *cum*
   **Apply:** `2Cor.12.11` la: `quum` → `cum`
242. *quum* → *cum*
   **Apply:** `2Cor.12.20` la: `quum` → `cum`
243. *quum* → *cum*
   **Apply:** `2Cor.13.9` la: `quum` → `cum`
