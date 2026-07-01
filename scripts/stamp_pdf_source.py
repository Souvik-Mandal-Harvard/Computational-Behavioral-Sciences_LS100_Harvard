#!/usr/bin/env python3
"""Stamp each generated guide PDF with its source location, rotated along the
left margin: the label "Downloaded from: " followed by the guide's MODULE page
URL as a clickable, #002288, non-underlined link.

Why the module page (not the guide's own slug): MyST auto-generates page slugs
and the exact algorithm/length is not something to guess. Module pages have
short, stable slugs derived from filenames we control, so they never 404.

Usage:  python scripts/stamp_pdf_source.py [root]   (default root: ".")
Env:    PDF_SOURCE_BASE  (default: https://souvikmandal.info/teaching-learning/ls100)
Run AFTER `myst build --pdf` and BEFORE `myst build --html`.
"""
import sys, os, re, glob, io
import yaml
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from reportlab.pdfbase.pdfmetrics import stringWidth

BASE = os.environ.get("PDF_SOURCE_BASE",
                      "https://souvikmandal.info/teaching-learning/ls100").rstrip("/")
FONT, SIZE = "Helvetica", 7
LABEL = "Downloaded from: "
URL_COLOR = Color(0x00 / 255, 0x22 / 255, 0x88 / 255)   # #002288
LABEL_COLOR = Color(0.35, 0.35, 0.35)

def slug(filename):
    return re.sub(r"[^A-Za-z0-9]+", "-",
                  os.path.splitext(os.path.basename(filename))[0]).strip("-").lower()

def frontmatter(md):
    t = open(md, encoding="utf-8").read()
    mo = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    return (yaml.safe_load(mo.group(1)) or {}) if mo else {}

def build_pdf_url_map():
    """From myst.yml TOC: map each export-PDF basename -> its MODULE page URL."""
    try:
        cfg = yaml.safe_load(open("myst.yml"))
    except Exception:
        return {}
    m = {}
    def walk(items):
        for it in items or []:
            f = it.get("file")
            children = it.get("children", [])
            if f and os.path.basename(f).startswith("Module-"):
                mod_url = f"{BASE}/{slug(f)}/"
                for c in children:
                    cf = c.get("file")
                    if cf and cf.endswith(".md") and os.path.exists(cf):
                        for e in frontmatter(cf).get("exports", []):
                            out = e.get("output")
                            if out:
                                m[os.path.basename(out)] = mod_url
            walk(children)
    walk(cfg.get("project", {}).get("toc", []))
    return m

def module_url_from_folder(pdf):
    """Fallback: module URL from the module folder that contains this exports/ dir."""
    mod_folder = os.path.dirname(os.path.dirname(pdf))
    mods = glob.glob(os.path.join(mod_folder, "Module-*.md"))
    return f"{BASE}/{slug(mods[0])}/" if mods else None

def overlay_page(w, h, url):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(w, h))
    c.setFont(FONT, SIZE)
    full_w = stringWidth(LABEL + url, FONT, SIZE)
    label_w = stringWidth(LABEL, FONT, SIZE)
    x = 13.0                    # distance in from the left edge
    y0 = h / 2.0 - full_w / 2.0  # start of the rotated string, along page height
    c.saveState()
    c.translate(x, y0)
    c.rotate(90)
    c.setFillColor(LABEL_COLOR)
    c.drawString(0, 0, LABEL)
    c.setFillColor(URL_COLOR)
    c.drawString(label_w, 0, url)
    c.restoreState()
    # clickable link over just the URL portion (no border => no underline/box)
    c.linkURL(url, (x - SIZE, y0 + label_w, x + 2, y0 + full_w),
              relative=0, thickness=0)
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]

def stamp(path, url):
    reader = PdfReader(path)
    writer = PdfWriter()
    for page in reader.pages:
        page.merge_page(overlay_page(float(page.mediabox.width),
                                     float(page.mediabox.height), url))
        writer.add_page(page)
    with open(path, "wb") as f:
        writer.write(f)

def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    pdfs = sorted(p for p in glob.glob(os.path.join(root, "**", "*.pdf"), recursive=True)
                  if os.path.basename(os.path.dirname(p)) == "exports")
    if not pdfs:
        print(f"No exports/*.pdf found under {root!r}; nothing to stamp.")
        return
    url_map = build_pdf_url_map()
    for pdf in pdfs:
        url = url_map.get(os.path.basename(pdf)) or module_url_from_folder(pdf)
        if not url:
            print("  no URL mapping for", pdf, "— skipped")
            continue
        stamp(pdf, url)
        print("stamped", os.path.basename(pdf), "->", url)

if __name__ == "__main__":
    main()
