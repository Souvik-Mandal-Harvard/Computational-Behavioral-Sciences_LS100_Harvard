#!/usr/bin/env python3
"""Regenerate each notebook's run-buttons (Open in Colab / Open in GitHub
Codespaces / Download notebook) from its CURRENT path, so the links stay correct
after any rename.

The buttons live in the notebook's JSON `metadata.downloads` (not a visible
cell), so nothing shows when the notebook is opened in Jupyter/GitHub/Colab.
Only `downloads` is touched — `short_title` and everything else are preserved.

Run in CI BEFORE `myst build`. Changes are made only on the CI checkout, never
committed — so the deployed site is always self-correcting.

Usage:  python scripts/refresh_run_buttons.py [root]   (default ".")
Env:    RUN_BTN_OWNER, RUN_BTN_REPO, RUN_BTN_BRANCH (defaults below)
"""
import json, glob, os, sys

OWNER  = os.environ.get("RUN_BTN_OWNER", "Souvik-Mandal-Harvard")
REPO   = os.environ.get("RUN_BTN_REPO",  "Computational-Behavioral-Sciences_LS100_Harvard")
BRANCH = os.environ.get("RUN_BTN_BRANCH", "main")
CODESPACES = f"https://codespaces.new/{OWNER}/{REPO}?devcontainer_path=.devcontainer%2Fdevcontainer.json"

def refresh(nb):
    relpath = nb.replace("\\", "/").lstrip("./")
    base = os.path.basename(nb)
    colab = f"https://colab.research.google.com/github/{OWNER}/{REPO}/blob/{BRANCH}/{relpath}"
    d = json.load(open(nb, encoding="utf-8"))
    md = d.setdefault("metadata", {})
    md["downloads"] = [
        {"url": colab, "title": "Open in Colab"},
        {"url": CODESPACES, "title": "Open in GitHub Codespaces"},
        {"file": base, "title": "Download notebook"},
    ]
    json.dump(d, open(nb, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    n = 0
    for nb in sorted(glob.glob(os.path.join(root, "**", "*.ipynb"), recursive=True)):
        if "/.ipynb_checkpoints/" in nb.replace("\\", "/"): continue
        refresh(nb); n += 1
        print("refreshed run-buttons:", nb)
    print(f"done: {n} notebook(s)")

if __name__ == "__main__":
    main()
