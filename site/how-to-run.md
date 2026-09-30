---
title: How to Run the Notebooks
short_title: How to Run
description: Three ways to run every LS100 notebook — locally, in Google Colab, or in GitHub Codespaces.
---

Every notebook in this course can be run three ways. Each notebook page has buttons for all
three in its download panel. Pick whichever fits your situation.

All the required packages for this course are listed in the [`requirements.txt`](https://github.com/Souvik-Mandal-Harvard/Computational-Behavioral-Sciences_LS100_Harvard/blob/main/requirements.txt) file. Please download it and keep it in the root directory of your project.

## 💻 Download and run locally

Best if you want to work offline on your own machine and keep your files locally.

1. Install Python. See [Computation Guide 01 · Getting Started with Python](../LS100_00B_Python-Fundamentals/LS100_module-00B_content-01_Guide-01_Getting-Started-with-Python_LastUpdated-20260601.md) for macOS and Windows instructions.
2. Follow [Local setup: Python + venv + Jupyter](#local-setup) to create a virtual environment, install the course packages, and launch Jupyter. The short version (macOS; the guide also covers Windows and Anaconda):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install -r requirements.txt
   jupyter notebook
   ```
3. Open the downloaded `.ipynb` from the Jupyter file browser.

## ☁️ Open in Google Colab

Best for a zero-install browser session with a free GPU (recommended for the GPU-based
pose-estimation notebooks). Click **Open in Colab** on any notebook page. Colab opens the
notebook straight from this repository — no setup required. Save a copy to your own Google
Drive to keep your edits.

## 🧰 GitHub Codespaces

Best for a full, pre-configured cloud dev environment. Click **Open in GitHub Codespaces** on
any notebook page (or from the repository). The included `.devcontainer/` installs Python and
all dependencies automatically, so the environment is ready to run.

:::{note}
The GPU-based notebooks (YOLOv8 batch/single-video pose estimation) are designed for Colab's
free GPU. The CPU notebooks run fine locally or in Codespaces.
:::
