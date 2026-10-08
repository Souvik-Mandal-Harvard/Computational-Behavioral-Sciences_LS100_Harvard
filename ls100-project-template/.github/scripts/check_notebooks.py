"""Reproducibility check for LS100 projects.

Runs on GitHub after every push. Messages are written for students who are
new to coding, so each failure says what went wrong and how to fix it.

Rules
-----
* A notebook whose file name contains "GPU" (any capitalization) is a GPU
  notebook. It ran in Colab, so it is NOT re-run here. We only check that it
  was saved *with* its outputs (proof that it was run).
* Every other notebook is run from top to bottom in a fresh Python session,
  exactly like "Restart & Run All". It must finish without errors.
* Notebooks must use relative paths such as data/raw/file.csv, not paths that
  only exist on one computer (/Users/..., C:\\..., /content/drive/...).
* Optional: .github/expected-outputs.txt lists files that must exist (for
  example the keypoint CSVs produced in Colab) and the columns they need.
"""

from __future__ import annotations

import csv
import os
import re
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError, CellTimeoutError

REPO = Path(__file__).resolve().parents[2]
EXPECTED_OUTPUTS = REPO / ".github" / "expected-outputs.txt"
CELL_TIMEOUT_SECONDS = 600

# Paths that only exist on one person's computer or inside a Colab session.
MACHINE_SPECIFIC_PATH = re.compile(
    r"""["'](?:/Users/|/home/|/content/|[A-Za-z]:[\\/])"""
)

results: list[tuple[str, str, str]] = []  # (status, item, message)


def report(status: str, item: str, message: str) -> None:
    results.append((status, item, message))
    icon = {"PASS": "✅", "SKIP": "⏭️", "FAIL": "❌"}[status]
    print(f"{icon} {item}: {message}")


def find_notebooks() -> list[Path]:
    notebooks = []
    for path in sorted(REPO.rglob("*.ipynb")):
        parts = path.relative_to(REPO).parts
        if any(p.startswith(".") for p in parts):  # .ipynb_checkpoints, .github, ...
            continue
        notebooks.append(path)
    return notebooks


def is_gpu_notebook(path: Path) -> bool:
    return "gpu" in path.name.lower()


def code_cells(nb) -> list:
    return [c for c in nb.cells if c.cell_type == "code" and c.source.strip()]


def check_gpu_notebook(path: Path, nb) -> None:
    name = str(path.relative_to(REPO))
    cells = code_cells(nb)
    ran = [c for c in cells if c.get("outputs") or c.get("execution_count")]
    if cells and not ran:
        report(
            "FAIL", name,
            "This GPU notebook was saved without any outputs, so it looks like it "
            "was never run. Run it in Colab (Runtime → Run all), then save it to "
            "GitHub again with File → Save a copy in GitHub.",
        )
    else:
        report("SKIP", name, "GPU notebook: not re-run here (it needs Colab). Saved outputs found.")


def check_paths(path: Path, nb) -> bool:
    name = str(path.relative_to(REPO))
    for i, cell in enumerate(nb.cells, start=1):
        if cell.cell_type != "code":
            continue
        match = MACHINE_SPECIFIC_PATH.search(cell.source)
        if "drive.mount" in cell.source or (match and "/content/" in match.group(0)):
            report(
                "FAIL", name,
                f"Cell {i} uses Google Drive or Colab paths, which don't exist outside "
                "Colab. If this notebook needs a GPU, add 'GPU' to its file name (e.g. "
                "02_pose-estimation_GPU.ipynb). Otherwise, put the data in data/raw/ "
                "and use a relative path such as 'data/raw/my_data.csv'.",
            )
            return False
        if match:
            found = match.group(0)[1:]
            report(
                "FAIL", name,
                f"Cell {i} uses a path that only works on one computer (starts with "
                f"'{found}'). Use a path relative to the assignment folder instead, "
                f"for example 'data/raw/my_data.csv'.",
            )
            return False
    return True


def run_notebook(path: Path, nb) -> None:
    name = str(path.relative_to(REPO))
    client = NotebookClient(
        nb,
        timeout=CELL_TIMEOUT_SECONDS,
        kernel_name="python3",
        resources={"metadata": {"path": str(path.parent)}},
    )
    try:
        client.execute()
    except CellTimeoutError:
        report(
            "FAIL", name,
            f"A cell took longer than {CELL_TIMEOUT_SECONDS // 60} minutes. If this step "
            "needs a GPU, run it in Colab and put 'GPU' in the notebook's file name.",
        )
    except CellExecutionError as err:
        cell_no = next(
            (i for i, c in enumerate(nb.cells, start=1)
             if c.cell_type == "code" and any(o.get("output_type") == "error" for o in c.get("outputs", []))),
            "?",
        )
        error_line = f"{err.ename}: {err.evalue}"
        hint = ""
        if err.ename in ("FileNotFoundError", "OSError"):
            hint = (" Check that the file is committed to GitHub (not only on your "
                    "computer or in Colab) and that the path is spelled exactly right.")
        elif err.ename in ("ModuleNotFoundError", "ImportError"):
            hint = " This package is not in requirements.txt. Ask the teaching team to add it."
        elif err.ename == "NameError":
            hint = (" A variable is used before the cell that creates it. Your cells "
                    "probably ran out of order — try Restart & Run All yourself.")
        report(
            "FAIL", name,
            f"The notebook stopped with an error in cell {cell_no} → {error_line}.{hint}",
        )
    else:
        report("PASS", name, "Ran from top to bottom without errors (Restart & Run All).")


def check_expected_outputs() -> None:
    if not EXPECTED_OUTPUTS.exists():
        return
    for raw in EXPECTED_OUTPUTS.read_text().splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        file_part, _, cols_part = line.partition(":")
        rel = file_part.strip()
        required = [c.strip() for c in cols_part.split(",") if c.strip()]
        target = REPO / rel
        if not target.exists():
            report(
                "FAIL", rel,
                "This file is missing. If it comes from a Colab (GPU) notebook, "
                "download it from Colab and upload it to this folder on GitHub.",
            )
            continue
        if required and target.suffix.lower() == ".csv":
            with target.open(newline="", encoding="utf-8-sig") as f:
                header = [h.strip() for h in next(csv.reader(f), [])]
            missing = [c for c in required if c not in header]
            if missing:
                report("FAIL", rel, f"Missing column(s): {', '.join(missing)}.")
                continue
        report("PASS", rel, "Found" + (" with the required columns." if required else "."))


def write_summary() -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    icons = {"PASS": "✅ Pass", "SKIP": "⏭️ Skipped (GPU)", "FAIL": "❌ Needs fixing"}
    lines = ["## Reproducibility check", "", "| Result | File | Details |", "| --- | --- | --- |"]
    for status, item, message in results:
        lines.append(f"| {icons[status]} | `{item}` | {message.replace('|', '/')} |")
    if any(s == "FAIL" for s, _, _ in results):
        lines += ["", "Fix the ❌ items, commit, and push again — this check re-runs automatically."]
    with open(summary_path, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main() -> int:
    notebooks = find_notebooks()
    if not notebooks:
        report("FAIL", "(repository)", "No notebook (.ipynb) found. Did you upload or commit it?")
    for path in notebooks:
        nb = nbformat.read(path, as_version=4)
        if is_gpu_notebook(path):
            check_gpu_notebook(path, nb)
        elif check_paths(path, nb):
            run_notebook(path, nb)
    check_expected_outputs()
    write_summary()
    return 1 if any(s == "FAIL" for s, _, _ in results) else 0


if __name__ == "__main__":
    sys.exit(main())
