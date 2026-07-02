#!/usr/bin/env python3
"""Insert (or refresh) a git-derived "Last updated" stamp on each article,
just under the title/byline.

The date is the last Git commit that touched the file (`git log -1 --format=%cs`).
Run in CI BEFORE `myst build`. Requires full history: use actions/checkout with
`fetch-depth: 0`. Changes are made only on the CI checkout, never committed.

- Markdown guides (.md): a `_Last updated: …_` line at the top of the body.
- Notebooks (.ipynb): a dedicated markdown cell right after the title/byline cell.

Both are idempotent (a marker comment lets re-runs replace rather than stack).
Scope: reading guides (.md, excluding nav/module/README) and all course notebooks.

Usage:  python scripts/inject_last_updated.py [root]   (default ".")
"""
import subprocess, glob, re, os, sys, json

MARKER = "<!--last-updated-->"
LINE_RE = re.compile(r"(?m)^_Last updated:.*?" + re.escape(MARKER) + r"[ \t]*\n?")

def git_date(path):
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", path],
                             capture_output=True, text=True).stdout.strip()
        return out or None
    except Exception:
        return None

def stamp_text(date):
    return f"_Last updated: {date}_ {MARKER}"

# ---------- Markdown ----------
def is_article_md(md):
    p = md.replace("\\", "/").lstrip("./")
    base = os.path.basename(p)
    if p.startswith("site/"): return False
    if base.startswith("Module-"): return False
    if base.lower() == "readme.md": return False
    return True

def process_md(md):
    date = git_date(md)
    if not date: return False
    t = open(md, encoding="utf-8").read()
    m = re.match(r"^(---\n.*?\n---\n)(.*)$", t, re.S)
    if not m: return False
    fm, body = m.group(1), m.group(2)
    body = LINE_RE.sub("", body).lstrip("\n")
    open(md, "w", encoding="utf-8").write(f"{fm}\n{stamp_text(date)}\n\n{body}")
    return True

# ---------- Notebooks ----------
def process_ipynb(path):
    date = git_date(path)
    if not date: return False
    d = json.load(open(path, encoding="utf-8"))
    cells = d.get("cells", [])
    stamp_cell_source = [stamp_text(date) + "\n"]

    # 1) refresh an existing stamp cell in place
    for c in cells:
        if c.get("cell_type") == "markdown" and MARKER in "".join(c.get("source", [])):
            c["source"] = stamp_cell_source
            json.dump(d, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
            return True

    # 2) insert a new stamp cell right after the title/byline cell
    idx = None
    for i, c in enumerate(cells):                       # prefer: after the byline cell
        if c.get("cell_type") == "markdown" and "Authored by" in "".join(c.get("source", [])):
            idx = i + 1; break
    if idx is None:                                     # else: after the first H1 cell
        for i, c in enumerate(cells):
            if c.get("cell_type") == "markdown" and "".join(c.get("source", [])).lstrip().startswith("# "):
                idx = i + 1; break
    if idx is None:                                     # else: after the frontmatter cell
        idx = min(1, len(cells))
    cells.insert(idx, {"cell_type": "markdown", "metadata": {}, "source": stamp_cell_source})
    d["cells"] = cells
    json.dump(d, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return True

def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    n = 0
    for md in sorted(glob.glob(os.path.join(root, "**", "*.md"), recursive=True)):
        if is_article_md(md) and process_md(md):
            print("md  stamped:", md, "->", git_date(md)); n += 1
    for nb in sorted(glob.glob(os.path.join(root, "**", "*.ipynb"), recursive=True)):
        if "/.ipynb_checkpoints/" in nb.replace("\\", "/"): continue
        if process_ipynb(nb):
            print("nb  stamped:", nb, "->", git_date(nb)); n += 1
    print(f"done: {n} article(s) stamped")

if __name__ == "__main__":
    main()
