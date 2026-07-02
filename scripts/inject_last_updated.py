#!/usr/bin/env python3
"""Insert (or refresh) a git-derived "Last updated" line at the top of each
article's body, just under the title/date block.

The date is the last Git commit that touched the file (`git log -1 --format=%cs`).
Run in CI BEFORE `myst build`. Requires full history: use actions/checkout with
`fetch-depth: 0`. Changes are made only on the CI checkout, never committed.

Scope: article pages only — the reading guides. Skips navigation pages (site/),
module overview pages (Module-*.md) and README.

Usage:  python scripts/inject_last_updated.py [root]   (default ".")
"""
import subprocess, glob, re, os, sys

MARKER = "<!--last-updated-->"
LINE_RE = re.compile(r"(?m)^_Last updated:.*?" + re.escape(MARKER) + r"[ \t]*\n?")

def git_date(path):
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", path],
                             capture_output=True, text=True).stdout.strip()
        return out or None
    except Exception:
        return None

def is_article(md):
    p = md.replace("\\", "/").lstrip("./")
    base = os.path.basename(p)
    if p.startswith("site/"): return False
    if base.startswith("Module-"): return False
    if base.lower() == "readme.md": return False
    return True

def process(md):
    date = git_date(md)
    if not date:
        return False
    t = open(md, encoding="utf-8").read()
    m = re.match(r"^(---\n.*?\n---\n)(.*)$", t, re.S)
    if not m:
        return False
    fm, body = m.group(1), m.group(2)
    body = LINE_RE.sub("", body).lstrip("\n")          # drop any previous stamp
    line = f"_Last updated: {date}_ {MARKER}"
    open(md, "w", encoding="utf-8").write(f"{fm}\n{line}\n\n{body}")
    return True

def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    n = 0
    for md in sorted(glob.glob(os.path.join(root, "**", "*.md"), recursive=True)):
        if is_article(md) and process(md):
            print("stamped last-updated:", md, "->", git_date(md))
            n += 1
    print(f"done: {n} article(s) stamped")

if __name__ == "__main__":
    main()
