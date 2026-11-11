# Text Files

This directory contains the plain text files in their various stages of processing.

* [/OCR](https://github.com/njand/biblia-castellionis/tree/main/TXT/1%20-%20OCR) contains the raw OCR output from Google Books (very low quality, but it does speed up the process somewhat.)
* [/Post-Corrected](https://github.com/njand/biblia-castellionis/tree/main/TXT/2%20-%20Post-Corrected) contains the corrected version of the OCR files.
* [/Edited](https://github.com/njand/biblia-castellionis/tree/main/TXT/3%20-%20Edited) contains the files with additional updates to spelling and formatting.

These are the earlier manual stages of the 1726–27 edition. The edition itself is now made from the USFM master in
[`text/`](../text), and the plain text with and without macrons is generated with the other downloads (see the
[releases](https://github.com/njand/biblia-castellionis/releases)); the pipeline reads these files as witnesses.
