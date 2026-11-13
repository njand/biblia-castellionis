"""EPUB 3 (with an NCX for older readers and Kindle), following e-liber's package layout: a title page, a
colophon, one XHTML file per book with an anchor at each chapter's drop cap, nav.xhtml and toc.ncx nested book →
chapter. Plain CSS, no script, no web fonts: Kindle-friendly. `macrons=False` writes the edition without macrons.

The zip is reproducible apart from dcterms:modified: fixed file times, mimetype first and stored."""

import html
import uuid
import zipfile

from pipeline import publish, site

FIXED_ZIP_TIME = (2000, 1, 1, 0, 0, 0)

CSS = """body { font-family: serif; line-height: 1.45; margin: 0 .3em; }
h1 { font-weight: normal; text-align: center; font-variant: small-caps; margin: 1.5em 0 1em; line-height: 1.3; }
h1 span.mt1, h1 span.mt2 { display: block; }
h1 span.mt2 { font-size: .55em; letter-spacing: .06em; }
p { margin: 0; text-indent: 1.2em; text-align: justify; }
p.first, p.m, p.nb { text-indent: 0; }
p.argumentum { font-style: italic; text-indent: 0; margin: 1em 0 .5em; }
p.cls { font-style: italic; text-indent: 0; font-size: .9em; margin-top: 1em; }
sup.fn { font-size: .6em; line-height: 0; font-style: italic; }
sup.fn a { text-decoration: none; }
aside.fn { font-size: .8em; margin: .2em 0 0; }
aside.fn p { text-indent: 0; margin: 0; }
p.d { font-style: italic; text-indent: 0; margin: .5em 0; }
div.poem { margin: .4em 0; }
div.q1, div.q2, div.q3 { margin-left: 2em; text-indent: -1em; }
div.q2 { margin-left: 3.5em; }
div.q3 { margin-left: 5em; }
div.b { height: .6em; }
span.c { float: left; font-size: 3em; line-height: .9; margin: .05em .12em 0 0; }
div.chapter { clear: both; margin-top: .8em; }
sup.v { font-size: .6em; line-height: 0; vertical-align: super; }
i.qt { font-style: italic; }
.title { text-align: center; margin-top: 30%; }
.title .series { font-size: 2em; font-variant: small-caps; text-indent: 0; text-align: center; }
.title p { text-indent: 0; text-align: center; margin: .4em 0; }
.colophon p { text-indent: 0; text-align: left; margin: .6em 0; font-size: .85em; }
.colophon ul { font-size: .85em; }
"""


def xhtml(title, body, lang="la"):
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{lang}" lang="{lang}">
<head>
<meta charset="utf-8"/>
<title>{html.escape(title)}</title>
<link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
{body}
</body>
</html>
"""


def book_xhtml(book, filt):
    parts = [site.title_h1(book, filt)]
    for chapter in book.chapters:
        parts.append(f'<div class="chapter">\n'
                     + site.chapter_html(chapter, lambda n, c=chapter.number: f"c{c}v{n}", f"c{chapter.number}",
                                         filt, verse_link=False)
                     + "\n</div>")
    return xhtml(filt(book.short), "\n".join(parts))


def title_xhtml(title, version, filt):
    edition = f'<p>{site.esc(version)}</p>' if version else ""
    return xhtml(filt(title), f"""<div class="title">
<p class="series">Biblia Sacra</p>
<p>ex</p>
<p>{site.esc(filt("Sebastiānī Castelliōnis"))}</p>
<p>{site.esc(filt("interpretātiōne"))}</p>
<p>&#160;</p>
<p>{site.esc(filt(title))}</p>
{edition}
</div>""")


def colophon_xhtml(selected, filt=lambda text: text, macrons=True):
    info = {key: filt(value) if isinstance(value, str) else value
            for key, value in publish.credits(selected, macrons).items()}

    def link(url):                      # on a line of its own, shown without "https://"
        return f'<br/><a href="{html.escape(url)}">{site.esc(publish.short_url(url))}</a>'

    return xhtml(info["title"], f"""<div class="colophon">
<h1>{site.esc(info["title"])}</h1>
<p>{site.esc(info["about"])}</p>
<p>{site.esc(info["bases"])}</p>
<p>{site.esc(info["edited"])}</p>
<p>{site.esc(info["licence"])}{link(info["licence_url"])}</p>
<p>{site.esc(info["wikisource"])}</p>
<p>{site.esc(info["wikisource_list_lead"])}{link(info["wikisource_list_url"])}</p>
<p>{site.esc(info["source_lead"])}{link(info["repository"])}</p>
</div>""")


def nav_xhtml(selected, filt):
    items = []
    for index, book in enumerate(selected, 1):
        chapters = "".join(f'<li><a href="book{index}.xhtml#c{c.number}">{c.number}</a></li>' for c in book.chapters)
        items.append(f'<li><a href="book{index}.xhtml">{site.esc(filt(book.short))}</a><ol>{chapters}</ol></li>')
    return xhtml("Index", f"""<nav epub:type="toc" id="toc">
<h1>Index</h1>
<ol>
<li><a href="title.xhtml">{site.esc(filt("Titulus"))}</a></li>
{chr(10).join(items)}
<li><a href="colophon.xhtml">{site.esc(filt(publish.credits(selected)["title"]))}</a></li>
</ol>
</nav>
<nav epub:type="landmarks" id="landmarks" hidden="hidden">
<ol>
<li><a epub:type="titlepage" href="title.xhtml">Titulus</a></li>
<li><a epub:type="bodymatter" href="book1.xhtml">{site.esc(filt(selected[0].short))}</a></li>
</ol>
</nav>""")


def ncx(selected, uid, title, filt):
    points, order = [], 0

    def point(label, src, children=""):
        nonlocal order
        order += 1
        return (f'<navPoint id="np{order}" playOrder="{order}"><navLabel><text>{site.esc(label)}</text></navLabel>'
                f'<content src="{src}"/>{children}</navPoint>')

    points.append(point(filt("Titulus"), "title.xhtml"))
    for index, book in enumerate(selected, 1):
        label = filt(book.short)
        head = point(label, f"book{index}.xhtml")       # numbered before its chapters, as playOrder requires
        children = "".join(point(f"{label} {c.number}", f"book{index}.xhtml#c{c.number}") for c in book.chapters)
        points.append(head.removesuffix("</navPoint>") + children + "</navPoint>")
    points.append(point(filt(publish.credits(selected)["title"]), "colophon.xhtml"))
    return f"""<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="{uid}"/><meta name="dtb:depth" content="2"/></head>
<docTitle><text>{site.esc(title)}</text></docTitle>
<navMap>
{chr(10).join(points)}
</navMap>
</ncx>
"""


def opf(selected, uid, title, modified, files):
    manifest = ['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
                '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
                '<item id="css" href="style.css" media-type="text/css"/>']
    manifest += [f'<item id="{name.split(".")[0]}" href="{name}" media-type="application/xhtml+xml"/>'
                 for name in files]
    spine = "".join(f'<itemref idref="{name.split(".")[0]}"/>' for name in files)
    return f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid" xml:lang="la">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">{uid}</dc:identifier>
<dc:title>{site.esc(title)}</dc:title>
<dc:language>la</dc:language>
<dc:creator>Sebastianus Castellio</dc:creator>
<dc:contributor id="editor">{site.esc(publish.EDITOR)}</dc:contributor>
<meta refines="#editor" property="role" scheme="marc:relators">edt</meta>
<dc:rights>CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/); textus partim ex Vicifonte sumptus, CC BY-SA 4.0</dc:rights>
<dc:source>{publish.REPOSITORY}</dc:source>
<meta property="dcterms:modified">{modified}</meta>
</metadata>
<manifest>
{chr(10).join(manifest)}
</manifest>
<spine toc="ncx">{spine}</spine>
</package>
"""


def write(selected, path, title, version, stamp, macrons=True):
    filt = (lambda text: text) if macrons else publish.strip_macrons
    full_title = f"Biblia Sacra (Castellio): {filt(title)}" + ("" if macrons else " (sine macronibus)")
    uid = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, f"{publish.REPOSITORY}#{path.stem}"))
    contents = {"title.xhtml": title_xhtml(title, version, filt)}
    for index, book in enumerate(selected, 1):
        contents[f"book{index}.xhtml"] = book_xhtml(book, filt)
    contents["colophon.xhtml"] = colophon_xhtml(selected, filt, macrons)
    files = {
        "META-INF/container.xml": """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="EPUB/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>
""",
        "EPUB/content.opf": opf(selected, uid, full_title, stamp.strftime("%Y-%m-%dT%H:%M:%SZ"), list(contents)),
        "EPUB/nav.xhtml": nav_xhtml(selected, filt),
        "EPUB/toc.ncx": ncx(selected, uid, full_title, filt),
        "EPUB/style.css": CSS,
        **{f"EPUB/{name}": text for name, text in contents.items()},
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as epub:
        # The mimetype entry must come first and be stored uncompressed.
        epub.writestr(zipfile.ZipInfo("mimetype", FIXED_ZIP_TIME), "application/epub+zip", zipfile.ZIP_STORED)
        for name, text in files.items():
            epub.writestr(zipfile.ZipInfo(name, FIXED_ZIP_TIME), text.encode("utf-8"), zipfile.ZIP_DEFLATED)
    return path
