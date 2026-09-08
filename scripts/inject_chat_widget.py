#!/usr/bin/env python3
"""Publish the course-search widget and add it to every built page.

Run AFTER `myst build --html` and after embed_chat_index.mjs. MyST has no
configuration option for injecting custom JavaScript (only `site.options.style`
for CSS), so the widget is added by rewriting the built HTML here - the same
post-build approach gh_pages_safe_filenames.py already uses.

Copies site/_static/ls100-chat.{js,css} into <build>/ls100-chat/ and inserts a
stylesheet link and a deferred script tag before </body> on every page.

Asset URLs are absolute and include BASE_URL, because pages sit at different
depths (/index.html and /some-slug/index.html) and the widget derives the site
root from its own script URL.

Usage:  python3 scripts/inject_chat_widget.py [build_dir] [static_dir]
        (defaults: _build/html, site/_static)
"""
import os
import shutil
import sys

MARKER = "ls100-chat/ls100-chat.js"      # presence means this page is already done
ASSET_DIR = "ls100-chat"
ASSETS = ("ls100-chat.js", "ls100-chat.css")


def snippet(base_url):
    prefix = f"{base_url}/{ASSET_DIR}" if base_url else f"/{ASSET_DIR}"
    return (
        f'<link rel="stylesheet" href="{prefix}/ls100-chat.css">\n'
        f'<script src="{prefix}/ls100-chat.js" defer></script>\n'
    )


def is_page(path, build_dir):
    """True for real site pages, not the theme's hashed build artefacts."""
    rel = os.path.relpath(path, build_dir)
    return not rel.startswith("build" + os.sep)


def main():
    build_dir = sys.argv[1] if len(sys.argv) > 1 else "_build/html"
    static_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.join("site", "_static")
    base_url = (os.environ.get("BASE_URL") or "").rstrip("/")

    if not os.path.isdir(build_dir):
        sys.exit(f"build directory not found: {build_dir}")

    target = os.path.join(build_dir, ASSET_DIR)
    os.makedirs(target, exist_ok=True)
    for asset in ASSETS:
        src = os.path.join(static_dir, asset)
        if not os.path.isfile(src):
            sys.exit(f"missing widget asset: {src}")
        shutil.copy2(src, os.path.join(target, asset))
    print(f"published widget assets to {target}")

    if not os.path.isfile(os.path.join(target, "index.json")):
        print("  ! index.json not found - run build_chat_index.py and "
              "embed_chat_index.mjs, or the widget will load with no data")

    tag = snippet(base_url)
    injected = skipped = 0
    for dirpath, _dirnames, filenames in os.walk(build_dir):
        for name in filenames:
            if not name.endswith(".html"):
                continue
            path = os.path.join(dirpath, name)
            if not is_page(path, build_dir):
                continue
            try:
                with open(path, encoding="utf-8") as fh:
                    html = fh.read()
            except (OSError, UnicodeDecodeError):
                continue
            if MARKER in html:
                skipped += 1
                continue
            if "</body>" not in html:
                continue
            head, sep, tail = html.rpartition("</body>")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(head + tag + sep + tail)
            injected += 1

    print(f"injected widget into {injected} page(s)"
          + (f"; {skipped} already had it" if skipped else ""))


if __name__ == "__main__":
    main()
