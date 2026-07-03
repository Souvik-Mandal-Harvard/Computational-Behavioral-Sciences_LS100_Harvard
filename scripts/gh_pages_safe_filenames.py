#!/usr/bin/env python3
"""Make a MyST/Remix HTML build servable by GitHub Pages.

GitHub Pages refuses to serve files whose names contain $ [ ] ( ) — but the MyST
book theme (a Remix app) names its route bundles exactly that way
(e.g. `$-HASH.js`, `[sitemap.xml]-HASH.js`, `($project)…$slug[.json]-HASH.js`).
The files deploy fine but 404 when requested, which kills the client-side app
(search, hamburger, download menu).

This script, run AFTER `myst build --html` and BEFORE deploy, renames every such
file to a safe name and rewrites every reference to it (in the manifest, HTML,
JS, JSON, CSS) so the app still finds it.

Usage:  python scripts/gh_pages_safe_filenames.py [build_dir]   (default _build/html)
"""
import os, sys, glob

# character -> safe replacement (all replacements are [A-Za-z0-9_] only)
CHARMAP = {"$": "_dol_", "[": "_lbk_", "]": "_rbk_", "(": "_lpn_", ")": "_rpn_"}
SPECIAL = set(CHARMAP)
# percent-encodings GitHub/browsers may use in references (upper & lower case)
PCTMAP = {"$": ["%24"], "[": ["%5B", "%5b"], "]": ["%5D", "%5d"],
          "(": ["%28"], ")": ["%29"]}
TEXT_EXT = (".html", ".js", ".mjs", ".json", ".css", ".map", ".txt", ".xml", ".xsl")

def safe(name):
    for ch, rep in CHARMAP.items():
        name = name.replace(ch, rep)
    return name

def encoded_forms(name):
    """All percent-encoded spellings of `name` that might appear in references."""
    forms = {name}
    # expand each special char to its encodings, combinatorially but cheaply:
    # start from the raw name and, for each special char present, add a variant
    # where ALL of that char are replaced by each encoding.
    for ch, encs in PCTMAP.items():
        if ch in name:
            new = set()
            for f in forms:
                for e in encs:
                    new.add(f.replace(ch, e))
            forms |= new
    forms.discard(name)  # raw handled separately
    return forms

def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "_build/html"
    # 1) collect files needing a rename (old basename -> new basename)
    renames = []          # (old_path, new_path)
    name_map = {}         # old_basename -> new_basename
    for path in glob.glob(os.path.join(root, "**", "*"), recursive=True):
        if not os.path.isfile(path):
            continue
        base = os.path.basename(path)
        if any(c in base for c in SPECIAL):
            new_base = safe(base)
            name_map[base] = new_base
            renames.append((path, os.path.join(os.path.dirname(path), new_base)))
    if not name_map:
        print("no special-character filenames found; nothing to do.")
        return

    # 2) build the string replacements: raw + all percent-encoded spellings -> safe
    replacements = []
    for old_base, new_base in name_map.items():
        replacements.append((old_base, new_base))
        for enc in encoded_forms(old_base):
            replacements.append((enc, new_base))
    # longest first, so we never rewrite a substring of a longer match
    replacements.sort(key=lambda p: len(p[0]), reverse=True)

    # 3) rewrite references inside every text file (contents first, then rename)
    rewritten = 0
    for path in glob.glob(os.path.join(root, "**", "*"), recursive=True):
        if not (os.path.isfile(path) and path.lower().endswith(TEXT_EXT)):
            continue
        try:
            s = open(path, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            continue
        orig = s
        for old, new in replacements:
            if old in s:
                s = s.replace(old, new)
        if s != orig:
            open(path, "w", encoding="utf-8").write(s)
            rewritten += 1

    # 4) rename the files on disk
    for old_path, new_path in renames:
        os.rename(old_path, new_path)

    # 5) verify nothing special remains
    leftover = [os.path.basename(p) for p in glob.glob(os.path.join(root, "**", "*"), recursive=True)
                if os.path.isfile(p) and any(c in os.path.basename(p) for c in SPECIAL)]
    print(f"renamed {len(renames)} file(s); rewrote references in {rewritten} file(s).")
    print("special-character filenames remaining:", leftover if leftover else "none ✓")

if __name__ == "__main__":
    main()
