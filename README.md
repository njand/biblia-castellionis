# Biblia Sacra ex Sebastiani Castellionis Interpretatione

This project aims to digitally transcribe Sebastian Castellio's Latin translation of the Bible. The text has been updated to adhere to modern Latin orthographic standards in accordance with the 2016 edition of the Gaffiot Latin dictionary, including the use of macrons to distinguish between long and short vowels. Each directory contains the files in a specified format, such as EPUB or LaTeX.

## Project Goals

The primary objectives of this edition of the Castellio Latin Bible are:

1. To provide a useful resource for intermediate-level Latin learners
2. To update the formatting to make the book more easily readable for advanced Latin users

The Castellio translation is deemed an exceptional resource for intermediate Latin learners for several reasons:

* Familiarity: Many Latin students are familiar with the Bible. Therefore, this material will be generally comprehensible even if they don't understand 100% of the vocabulary or syntax.
* Length: The text contains over a half million words, providing ample material for learners to practice.
* Classical style: The Vulgate Bible may be less suitable for learners primarily interested in learning to read Classical-era Latin texts, as much of its vocabulary and syntax are very distinct from Classical standards. The Castellio translation will better assist students in acquainting themselves with idiomatic Classical Latinitas.

There are already many PDF scans of 16th-18th century editions of the Bible available, however, they are less suitable due to imperfections in the printing or scanning processes, decay of the originals, and unfamiliar abbreviations and spellings. Advanced Latin readers may not be overly impeded by these features, but they will hopefully still find their reading experience improved by the format of this edition, whether they are reading for scholarly interest, devotion, or pleasure.

### Orthography

Castellio naturally followed Renaissance conventions for spelling and abbreviations, which may be less familiar to students who are accustomed to reading modern editions of Latin works. Some of these spellings are not indicative of their Classical pronunciation, such as "cœlum" for "cælum" or "accerso" for "arcesso". This project follows the 2016 edition of the Gaffiot Latin dictionary as an orthographic standard because it is based on the latest scholarly research on how Latin was pronounced in the Classical era. In addition, this standard should feel more familiar to modern readers, although it does differ from common introductory textbooks in a few respects, such as its use of 'j' for consonantal 'i' and 'æ' to distinguish between the diphthong and disyllable. Finally, the inclusion of macrons not only aids in pronunciation, but it also serves to disambiguate some lexical and morphological forms.

### Formatting

This project seeks to emulate modern Bible formatting conventions by segmenting the text into paragraphs with verses indicated by superscript numbers. Poetry is displayed in stanza form, and quotations are italicized. The punctuation is occasionally updated to adhere to modern expectations and improve clarity. These conventions make extensive reading more comfortable, while still allowing the reader to correlate verses with other translations. This edition does not currently include marginal notes or scriptural commentaries.


## Sebastian Castellio

Sebastian Castellio (né Sébastien Châteillon) was a 16th century Protestant theologian. In addition to his native French, he was highly skilled in Hebrew, Greek, and Latin. Castellio preached alongside John Calvin in Geneva for a few years, but they eventually had a falling out, owing in part to Castellio's staunch support for religious tolerance. He undertook this Latin translation of the Bible in the 1540s to provide a Protestant alternative to the Catholic Vulgate Bible, publishing the first edition in 1551. In contrast to the Late Latin style of the Vulgate Bible and (in his view) the overly literal Latin translations of other Protestant translators, in this translation he strives to render the sacred text in idiomatic Classical Latin as if it originally had been written by native Latin speakers.

Theodore Beza, a fellow French Protestant who produced his own translation of the New Testament in 1556, was the most vehement critic of Castellio's translation, attacking it on doctrinal and stylistic grounds. Castellio published a response to Beza's criticism in 1562, defending his translation in most points, although conceding a few errors. Among Beza's quibbles was that Castellio had overly-latinized certain terms to remove their specific theological meanings, including "βαπτίζω" and "ἄγγελος". These terms were traditionally translated to Latin as "baptizō" and "angelus", but Castellio had eschewed tradition and gone translated them as "lavō" and "genius". Beza claimed that these word choices revealed that Castellio considered the holy to be mundane, for instance classifying baptism as no more meaningful than a generic washing. Castellio rejects this argument, considering it an ultimately meaningless difference in terms to refer to the same concepts. He doesn't strictly adhere to a Ciceronian standard of Latin authenticity, so he doesn't care if theologians use the Greek loanwords for technical writing, but he thinks that the pure Latin forms can suitably convey the meaning of the original Hebrew and Greek texts. Nevertheless, subsequent editions of Castellio's Latin Bible have switched some of these terms for their Ecclesiastical variants, including "baptizō" and "angelus". This project hews more closely to the later editions and transcribes the updated variants.

## Sources

I have consulted several PDF versions of different editions of this text, including the following:

* 1726-27 Edition - [Volumes 1-2](https://books.google.com/books?id=1EBbAAAAQAAJ), [Volumes 3-4](https://books.google.com/books?id=40BbAAAAQAAJ): Split into multiple volumes, this edition splits the text into verses and includes chapter headers, but no marginal notes or commentary. I generally follow the versification of this edition, except when I notice that it differs from modern Bible editions.
* [1697 Edition](https://books.google.com/books?id=wc1QkYeThIwC): Contains the entire Old and New Testament, extensive commentary, and Castellio's impassioned response to Theodore Beza's criticisms.
* [1553 Novum Testamentum](https://books.google.com/books?id=rFtSAAAAcAAJ): This is a much earlier edition, and it only contains the New Testament with limited marginal notes and no versification.

Most of my transcriptions are based on the latest (1726-1727) edition, except where the scan is unclear or the reading implausible, which cause me to consult the earlier editions.

N.B. This project is intended to create a reader's edition, not a critical edition of the original versions of the text. As such, there is no detailed record of changes or sources for each part of the transcription.


## Additional Resources

For further reading on Sebastian Castellio and his Latin Bible translation, I recommend:

* @book{guggisberg2017sebastian,
  title={Sebastian Castellio, 1515--1563: humanist and defender of religious toleration in a confessional age},
  author={Guggisberg, Hans R},
  year={2017},
  publisher={Routledge}
}

* @incollection{eskhult2012latin,
  title={Latin Bible Translations in the Protestant Reformation: Historical Contexts, Philological Justification, and the Impact of Classical Rhetoric on the Conception of Translation Methods},
  author={Eskhult, Josef},
  booktitle={Shaping the Bible in the Reformation},
  pages={167--185},
  year={2012},
  publisher={Brill}
}

* @article{gomez2015qui,
  title={Qui parle encore de S bastien Castellion?; Does anybody still talk about Sebastian Castellio?},
  author={Gomez-Geraud, Marie-Christine},
  journal={Australian Journal of French Studies},
  volume={52},
  number={3},
  pages={261--272},
  year={2015}
}

* @incollection{zahnd2017tolerant,
  title={Tolerant Humanists? Nikolaus Zurkinden and the Debate between Calvin, Castellio, and Beza},
  author={Zahnd, Ueli},
  booktitle={Crossing Traditions: Essays on the Reformation and Intellectual History},
  pages={370--385},
  year={2017},
  publisher={Brill}
}

For simple summaries of Bible stories in Latin:
* [Epitome Historiæ Sacræ](https://books.google.com/books?id=oxc-AQAAMAAJ) by Charles François Lhomond
* Or a [modern edition](https://www.amazon.com/Epitome-Historiae-Sacrae-Christi-Narratione/dp/1585104256) with some additional New Testament stories, formatted with marginal notes in the style of "Lingua Latina per se Illustrata"
