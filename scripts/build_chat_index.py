#!/usr/bin/env python3
"""Collect and chunk the LS100 course text for the site's semantic-search widget.

Run AFTER `myst build --html` and BEFORE `embed_chat_index.mjs`.

Text and URLs come from MyST's own search index (`myst.search.json`), which the
HTML build already writes. That file chunks every page by heading and records the
exact deployed URL — including the `#anchor` — for each chunk, so a search result
can never link to a page that the build did not actually produce. Page kind
(guide / notebook / site page) comes from each page's `location`, the original
source path.

The two course PDFs at the repository root are handled separately: they are not
part of the MyST table of contents, so the build never publishes them. They are
copied into the build here so their chunks have a real URL to point at.

URLs are stored site-root-relative with any base prefix stripped; the widget
prepends the site root it discovers at runtime. That keeps the index valid
whether the site is served from `/` or from `/teaching-learning/ls100`.

Usage:  python3 scripts/build_chat_index.py [build_dir] [repo_root]
        (defaults: _build/html, the current directory)
"""
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone

OUT_DIR = "ls100-chat"          # created inside the build directory
PDF_DIR = "course-documents"    # where root PDFs get published
MIN_CHARS = 80                  # drop fragments too short to be a useful result
MAX_CHARS = 900                 # embedding model sees ~256 tokens; keep under it
OVERLAP = 150                   # carry context across a split boundary

# The same byline opens nearly every page. Left in place it makes every page's
# first chunk look alike to the embedder, blunting ranking and consuming window.
BYLINE = re.compile(
    r"^\s*(Authored by\b.*|.*Project Leader & Instructor.*|.*Linkedin ID.*"
    r"|souvik-mandal-phd|LS100 READING GUIDE|Souvik Mandal,? Ph\.?D\.?,?)\s*$",
    re.I,
)


def strip_byline(text):
    """Drop leading byline/frontmatter lines, keeping the real content."""
    lines = text.split("\n")
    start = 0
    for i, line in enumerate(lines):
        if not line.strip() or BYLINE.match(line):
            start = i + 1
        else:
            break
    return "\n".join(lines[start:]).strip()


def load_slug_kinds(build_dir):
    """Map each page slug to a content kind, using the page's source path."""
    kinds = {}
    for name in os.listdir(build_dir):
        if not name.endswith(".json") or name.startswith("myst."):
            continue
        try:
            with open(os.path.join(build_dir, name), encoding="utf-8") as fh:
                page = json.load(fh)
        except (OSError, ValueError):
            continue
        slug, location = page.get("slug"), page.get("location") or ""
        if not slug:
            continue
        if location.endswith(".ipynb"):
            kind = "notebook"
        elif "/site/" in location:
            kind = "page"
        elif re.search(r"guide", location, re.I):
            kind = "guide"
        else:
            kind = "page"
        kinds[slug] = kind
    return kinds


def clean(text):
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_long(text, max_chars=MAX_CHARS, overlap=OVERLAP):
    """Split on paragraph, then sentence, boundaries so no tail is lost.

    Records run to 25k characters; the embedding model would silently truncate
    anything past its window, making the remainder unsearchable.
    """
    text = clean(text)
    if len(text) <= max_chars:
        return [text] if text else []

    pieces, current = [], ""
    units = [u for u in re.split(r"\n\n+", text) if u.strip()]
    for unit in units:
        if len(unit) > max_chars:                      # a single huge paragraph
            sentences = re.split(r"(?<=[.!?])\s+", unit)
            for sentence in sentences:
                # A single sentence can still exceed the window (tables, long
                # code lines); hard-cut it so no tail becomes unsearchable.
                while len(sentence) > max_chars:
                    if current:
                        pieces.append(current.strip())
                        current = ""
                    pieces.append(sentence[:max_chars].strip())
                    sentence = sentence[max_chars - overlap:]
                if len(current) + len(sentence) + 1 > max_chars and current:
                    pieces.append(current.strip())
                    current = current[-overlap:] if overlap < len(current) else ""
                current += (" " if current else "") + sentence
        else:
            if len(current) + len(unit) + 2 > max_chars and current:
                pieces.append(current.strip())
                current = current[-overlap:] if overlap < len(current) else ""
            current += ("\n\n" if current else "") + unit
    if current.strip():
        pieces.append(current.strip())
    return [p for p in pieces if len(p) >= MIN_CHARS]


def breadcrumb(hierarchy):
    levels = [hierarchy.get(f"lvl{i}") for i in range(1, 6)]
    return [l for l in levels if l]


def from_search_index(build_dir, base_url):
    path = os.path.join(build_dir, "myst.search.json")
    with open(path, encoding="utf-8") as fh:
        records = json.load(fh)["records"]

    kinds = load_slug_kinds(build_dir)
    chunks = []
    for record in records:
        if record.get("type") != "content":
            continue
        content = strip_byline((record.get("content") or "").strip())
        if len(content) < MIN_CHARS:
            continue

        url = record.get("url") or "/"
        if base_url and url.startswith(base_url):
            url = url[len(base_url):] or "/"
        slug = url.lstrip("/").split("#")[0].split("/")[0]

        crumbs = breadcrumb(record.get("hierarchy") or {})
        title = crumbs[0] if crumbs else slug
        section = " › ".join(crumbs[1:]) if len(crumbs) > 1 else ""

        for piece in split_long(content):
            chunks.append({
                "url": url,
                "title": title,
                "section": section,
                "kind": kinds.get(slug, "page"),
                "text": piece,
            })
    return chunks


def from_pdfs(build_dir, repo_root, base_url):
    """Extract the root course PDFs and publish them so their links resolve."""
    pdfs = sorted(
        f for f in os.listdir(repo_root)
        if f.lower().endswith(".pdf") and f.startswith("LS100_")
    )
    if not pdfs:
        return []
    try:
        from pypdf import PdfReader
    except ImportError:
        print("  ! pypdf not installed - skipping PDFs (pip install pypdf)")
        return []

    target = os.path.join(build_dir, PDF_DIR)
    os.makedirs(target, exist_ok=True)
    chunks = []
    for name in pdfs:
        shutil.copy2(os.path.join(repo_root, name), os.path.join(target, name))
        title = re.sub(r"^LS100_\d+_Document-\d+_", "", name)
        title = re.sub(r"_LastUpdated.*$", "", title).replace("_", " ").replace("-", " ")
        try:
            reader = PdfReader(os.path.join(repo_root, name))
        except Exception as exc:                       # noqa: BLE001 - report, continue
            print(f"  ! could not read {name}: {exc}")
            continue
        for page_no, page in enumerate(reader.pages, start=1):
            try:
                text = page.extract_text() or ""
            except Exception:                          # noqa: BLE001
                continue
            for piece in split_long(text):
                chunks.append({
                    # #page= is honoured by browser PDF viewers
                    "url": f"/{PDF_DIR}/{name}#page={page_no}",
                    "title": title.strip(),
                    "section": f"page {page_no}",
                    "kind": "pdf",
                    "text": piece,
                })
        print(f"  · {name} -> published + indexed")
    return chunks


def main():
    build_dir = sys.argv[1] if len(sys.argv) > 1 else "_build/html"
    repo_root = sys.argv[2] if len(sys.argv) > 2 else "."
    base_url = (os.environ.get("BASE_URL") or "").rstrip("/")

    if not os.path.isdir(build_dir):
        sys.exit(f"build directory not found: {build_dir} (run `myst build --html` first)")

    print(f"building chat index from {build_dir}")
    chunks = from_search_index(build_dir, base_url)
    print(f"  · {len(chunks)} chunks from site pages")
    pdf_chunks = from_pdfs(build_dir, repo_root, base_url)
    chunks += pdf_chunks
    print(f"  · {len(pdf_chunks)} chunks from course PDFs")

    for i, chunk in enumerate(chunks):
        chunk["id"] = i

    out_dir = os.path.join(build_dir, OUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "chunks.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump({
            "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "count": len(chunks),
            "chunks": chunks,
        }, fh, ensure_ascii=False)

    kinds = {}
    for chunk in chunks:
        kinds[chunk["kind"]] = kinds.get(chunk["kind"], 0) + 1
    print(f"wrote {out_path}  ({len(chunks)} chunks: {kinds})")


if __name__ == "__main__":
    main()
