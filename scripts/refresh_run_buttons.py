#!/usr/bin/env python3
"""Keep each notebook's run-links correct and prominent, from its CURRENT path.

Two things, both derived from the notebook's path so they survive renames:
  1. metadata.downloads — the "Download" panel entries (Colab / Codespaces / file).
  2. a visible badge row at the top of the page — "Open in Colab" and
     "Open in GitHub Codespaces" badges, so novices don't miss them under the panel.

Run in CI BEFORE `myst build`. Changes are made only on the CI checkout, never
committed — the committed .ipynb files stay clean; the website gets the badges.

Usage:  python scripts/refresh_run_buttons.py [root]   (default ".")
Env:    RUN_BTN_OWNER, RUN_BTN_REPO, RUN_BTN_BRANCH (defaults below)
"""
import json, glob, os, sys

OWNER  = os.environ.get("RUN_BTN_OWNER", "Souvik-Mandal-Harvard")
REPO   = os.environ.get("RUN_BTN_REPO",  "Computational-Behavioral-Sciences_LS100_Harvard")
BRANCH = os.environ.get("RUN_BTN_BRANCH", "main")
CODESPACES = f"https://codespaces.new/{OWNER}/{REPO}?devcontainer_path=.devcontainer%2Fdevcontainer.json"
BADGE_MARKER = "<!--run-badges-->"

def colab_url(relpath):
    return f"https://colab.research.google.com/github/{OWNER}/{REPO}/blob/{BRANCH}/{relpath}"

def badge_source(relpath):
    colab = colab_url(relpath)
    return [
        f"[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab}) "
        f"[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)]({CODESPACES})\n",
        f"{BADGE_MARKER}\n",
    ]

def refresh(nb):
    relpath = nb.replace("\\", "/").lstrip("./")
    base = os.path.basename(nb)
    d = json.load(open(nb, encoding="utf-8"))
    cells = d.get("cells", [])

    # 1) download panel entries (in hidden metadata)
    md = d.setdefault("metadata", {})
    md["downloads"] = [
        {"url": colab_url(relpath), "title": "Open in Colab"},
        {"url": CODESPACES, "title": "Open in GitHub Codespaces"},
        {"file": base, "title": "Download notebook"},
    ]

    # 2) visible badge row near the top — refresh in place, else insert after the
    #    title/byline cell (falling back to the first H1 cell, else the top).
    for c in cells:
        if c.get("cell_type") == "markdown" and BADGE_MARKER in "".join(c.get("source", [])):
            c["source"] = badge_source(relpath)
            break
    else:
        idx = None
        for i, c in enumerate(cells):
            if c.get("cell_type") == "markdown" and "Authored by" in "".join(c.get("source", [])):
                idx = i + 1; break
        if idx is None:
            for i, c in enumerate(cells):
                if c.get("cell_type") == "markdown" and "".join(c.get("source", [])).lstrip().startswith("# "):
                    idx = i + 1; break
        if idx is None:
            idx = 0
        cells.insert(idx, {"cell_type": "markdown", "metadata": {}, "source": badge_source(relpath)})
    d["cells"] = cells

    json.dump(d, open(nb, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    n = 0
    for nb in sorted(glob.glob(os.path.join(root, "**", "*.ipynb"), recursive=True)):
        if "/.ipynb_checkpoints/" in nb.replace("\\", "/"): continue
        refresh(nb); n += 1
        print("refreshed run-buttons + badges:", nb)
    print(f"done: {n} notebook(s)")

if __name__ == "__main__":
    main()
