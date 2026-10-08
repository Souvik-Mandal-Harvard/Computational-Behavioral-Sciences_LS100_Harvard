# Guide 2 · Running GPU Steps in Colab and Saving Results to GitHub

*Authored by* **Souvik Mandal, Ph.D.**

*Project Leader & Instructor, Computational Behavioral Sciences, LS100, FAS, Harvard University* | Linkedin ID: [souvik-mandal-phd](https://www.linkedin.com/in/souvik-mandal-phd)

---

Some steps in LS100, such as extracting body keypoints from video with YOLO or training a
custom model, need a **GPU**: a processor that does many calculations at once. Codespaces
doesn't have one, but **Google Colab** offers a GPU for free.

So a project that needs a GPU is split into two parts:

```mermaid
flowchart LR
    A["Videos<br/>in Google Drive"] --> B["GPU notebook<br/>in Colab"]
    B --> C["Small output files<br/>e.g. keypoints.csv"]
    C --> D["data/processed/<br/>in your GitHub repo"]
    D --> E["Analysis notebooks<br/>in Codespaces"]
```

The heavy step runs once in Colab and produces **small files** (like a CSV of keypoints).
Everything after that starts from those files and runs in Codespaces as usual. This split
between a compute-heavy step and an analysis step is how real research pipelines are built,
and it's worth describing in your README.

> [!NOTE]
> **Which notebooks are GPU notebooks?** Any notebook with **`GPU`** in its file name, such
> as `02_pose-estimation_GPU.ipynb`. The automatic check doesn't re-run these (GitHub's
> machines have no GPU). Instead it checks that you saved them **with their outputs**, as
> proof that they ran.

Read [Guide 1](01_submitting-assignments-with-github.md) first. This guide builds on it.

## Before you start: sync and close Codespaces

If you've been working in a codespace, **commit and sync** there first. Your repository then
has one up-to-date version, and Colab won't save over anything. Work in Codespaces *or*
Colab, not both at once.

## Step 1 · Put your videos in Google Drive

Videos are too large for GitHub, and they usually show identifiable people. Upload them to a
folder in your Google Drive, for example `My Drive/LS100/my-project/videos/`. Note that folder
in `data/raw/README.md` under *What is NOT shared, and where it lives*.

## Step 2 · Open the GPU notebook from your repository in Colab

1. Go to [colab.research.google.com](https://colab.research.google.com).
2. **File → Open notebook → GitHub** tab.
3. Tick **Include private repos**. Your repository is private, so it won't appear otherwise.
4. The first time, GitHub asks you to authorize Colab. Click **Authorize**.
5. Pick your repository, then the GPU notebook.

<!-- screenshot: Colab "Open notebook" → GitHub tab with "Include private repos" ticked -->

## Step 3 · Turn on the GPU

**Runtime → Change runtime type → Hardware accelerator: GPU** (e.g. *T4 GPU*) → **Save**.

To confirm it worked, run a cell with `!nvidia-smi`. You should see a table describing the GPU.

## Step 4 · Connect Google Drive and run

The notebook has a cell that connects your Drive:

```python
from google.colab import drive
drive.mount("/content/drive")
```

Run it and allow access. Then set the paths at the top of the notebook to your videos folder,
and **save the outputs to Drive too**:

```python
VIDEO_DIR  = "/content/drive/MyDrive/LS100/my-project/videos"
OUTPUT_DIR = "/content/drive/MyDrive/LS100/my-project/outputs"
```

> [!WARNING]
> Files saved only inside Colab (the folder panel on the left, outside `drive/`) **disappear
> when the session ends**. Always write results to your Drive folder.

Now run everything: **Runtime → Run all**. Keep the tab open. Free Colab sessions disconnect
if left idle, and they have time limits.

## Step 5 · Save the notebook back to GitHub

When the run has finished and you can see the outputs:

1. **File → Save a copy in GitHub**.
2. Choose your **repository** and the **main** branch.
3. Keep the **file path exactly the same** as the original, with `GPU` still in the name, so
   it replaces the old version instead of creating a second copy.
4. Write a short commit message, e.g. *"Ran pose estimation on 6 videos"*, and click **OK**.

This both commits and pushes, so there's no separate sync step.

<!-- screenshot: "Copy to GitHub" dialog with repository, branch, file path and commit message -->

## Step 6 · Put the output files in your repository

1. In Google Drive, open your outputs folder and **download** the CSV file(s).
2. On your GitHub repository page, open **`data/processed`** → **Add file → Upload files**.
3. Drag the files in, write a message, and click **Commit changes**.

Only upload **small result files** (CSVs, plots). Never upload videos or model files
(`.mp4`, `.pt`). The repository is set up to refuse most of them anyway.

## Step 7 · Continue in Codespaces

Open your codespace and click **Sync Changes** first. This downloads the notebook and CSVs
you just added. Then continue with the next (non-GPU) notebook. It reads the results
with a relative path:

```python
keypoints = pd.read_csv("data/processed/keypoints.csv")
```

From here on, follow the normal routine: Restart & Run All → Commit → Sync → green ✓.

## If something goes wrong

| Problem | What to do |
| --- | --- |
| *"Cannot connect to GPU backend"* or no GPU available | Free GPUs are shared, so try again later. If you're close to the deadline, use the **precomputed output files** provided by the teaching team and continue with the analysis. You won't lose credit for the later steps. |
| The session disconnected halfway | Your earlier outputs are safe in Drive (if you followed Step 4). Reconnect, re-run the setup cells, and process only the videos that are missing. |
| My repository doesn't appear in Colab | Tick **Include private repos**. If it still doesn't appear, open [github.com/settings/applications](https://github.com/settings/applications), check that *Colaboratory* is authorized, and try again. |
| The check says the GPU notebook *was saved without any outputs* | You saved before running. Run it in Colab, then repeat Step 5. |
| The check says a later notebook can't find `data/processed/...` | Step 6 was skipped, or the file name differs. Names are case-sensitive. |
| Codespaces says it can't sync because of conflicts | You edited the same notebook in both places. Ask the teaching team for help rather than forcing anything, since this is easy to fix together. |

> [!TIP]
> **Other free GPU options:** [Kaggle Notebooks](https://www.kaggle.com/code) also offer a free
> weekly GPU quota and work much like Colab. Ask the teaching team before using them, because
> saving to GitHub works differently there.
