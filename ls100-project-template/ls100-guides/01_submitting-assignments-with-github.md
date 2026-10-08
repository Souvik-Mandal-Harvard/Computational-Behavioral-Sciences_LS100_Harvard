# Guide 1 · Start Your Project and Submit It with GitHub

*Authored by* **Souvik Mandal, Ph.D.**

*Project Leader & Instructor, Computational Behavioral Sciences, LS100, FAS, Harvard University* | Linkedin ID: [souvik-mandal-phd](https://www.linkedin.com/in/souvik-mandal-phd)

---

In LS100 you don't email notebooks. Your project lives in **your own repository on GitHub**: an
online project folder that belongs to you, not to the course. You submit by saving your work
there. When the course ends, you keep it, polish it, and share it with employers and graduate
programs as evidence of what you can do.

**You don't need to know Git to follow this guide.** Everything is done by clicking buttons.

> [!TIP]
> **The whole routine in one line:** open your repo in Codespaces → work in the notebook →
> **Restart & Run All** → **Commit** → **Sync** → check for the green ✓.

## Six words you need

| Word | What it means |
| --- | --- |
| **Repository** (repo) | A project folder that lives on GitHub. Your project gets its own repo, in your account. |
| **Template** | A starter repo. You make your own copy of it with one click. |
| **Commit** | A save point with a short note, like "Added reaction-time plot". You can always go back to it. |
| **Push / Sync** | Upload your commits to GitHub. **Until you sync, nobody (including your instructor) can see your work.** |
| **Codespace** | A ready-to-use computer in your browser, with Python, Jupyter and all course packages installed. |
| **Check (✓ / ✗)** | After every sync, GitHub automatically re-runs your notebooks. Green ✓ means they ran without errors. |

## Part A · One-time setup

### A1 · Create a GitHub account

Sign up at [github.com/signup](https://github.com/signup).

- **Choose your username carefully.** It appears in every link you share with an employer.
  Something like `jdoe` or `jane-doe-data` works. Avoid joke names.
- Add your name and a photo in **Settings → Public profile**. A complete profile looks more
  credible when someone clicks through from your résumé.

**Recommended:** apply for the free [GitHub Student Developer Pack](https://education.github.com/pack)
with your school email. It includes extra Codespaces hours.

### A2 · Create your project repository from the LS100 template

1. Open the template: **[github.com/Souvik-Mandal-Harvard/ls100-project-template](https://github.com/Souvik-Mandal-Harvard/ls100-project-template)**.
2. Click the green **Use this template** button → **Create a new repository**.
3. Fill in the form:
   - **Owner:** your own username, so the project belongs to you.
   - **Repository name:** describe the project, not the course. `gait-dual-task-analysis` is
     good. `ls100-assignment-3` is not. You can rename it later in **Settings**.
   - **Description:** one sentence, e.g. *"Pose-estimation analysis of walking under cognitive load."*
   - **Visibility:** choose **Private** for now. You'll make it public after the course ends
     (see [Guide 3](03_make-it-portfolio-ready.md)).
4. Click **Create repository**.

<!-- screenshot: "Use this template" → "Create a new repository" form -->

### A3 · Give your instructor access

Because the repository is private, you need to invite the teaching team:

1. In your repository, open **Settings → Collaborators → Add people**.
2. Enter the teaching team's GitHub username(s) (posted on the course page) and click **Add**.

### A4 · Submit your repository link

Copy your repository's address (for example `https://github.com/jdoe/gait-dual-task-analysis`)
and submit it where your instructor asks, such as the course's assignment page. You only do
this once. After that, the teaching team always sees your latest synced work.

## Part B · Every work session

### B1 · Open your repo in Codespaces

On your repository page:

1. Click the green **<> Code** button.
2. Choose the **Codespaces** tab.
3. The first time, click **Create codespace on main**. After that, click your existing
   codespace in the same list to reopen it.

The first launch takes a few minutes while the course packages install.

<!-- screenshot: Code button → Codespaces tab → Create codespace on main -->

### B2 · Work in the notebook

1. In the **Explorer** panel on the left, click the notebook (e.g. `01_analysis.ipynb`).
2. The first time, click **Select Kernel** (top right) → **Python Environments** → choose
   **Python 3.11** (`/usr/local/bin/python`).
3. Run a cell with the ▶ button next to it, or press **Shift + Enter**.

Keep the folder organized:

- Load data from `data/raw/`, and never edit those files.
- Save tables you create to `data/processed/`.
- Save plots to `figures/`.
- Always use **relative paths** such as `"data/raw/survey.csv"`. A path like
  `"/Users/yourname/Downloads/survey.csv"` only works on your computer, and the check will
  flag it.
- Number notebooks in the order they run: `01_...`, `02_...`. Put **`GPU`** in the name of any
  notebook that needs Google Colab (see [Guide 2](02_gpu-steps-with-colab.md)).

### B3 · Restart & Run All

While you work, you run cells in whatever order you like, and a notebook can end up working
only because of something you ran earlier and then deleted. Before you finish, prove that it
works from scratch:

1. Click **Restart** in the notebook toolbar (this clears Python's memory).
2. Click **Run All**.
3. Scroll through and make sure every cell finished without a red error.

This is the most important habit in this course. It's also exactly what the automatic check
does, so if it passes for you, it will almost always pass on GitHub.

### B4 · Commit and sync

1. Save the notebook (**Ctrl + S**, or **Cmd + S** on a Mac).
2. Click the **Source Control** icon on the far-left bar. It looks like three dots
   connected by lines, and shows a number badge when you have changes.
3. Type a short message describing what you did, e.g. *"Cleaned data and added condition plot"*.
4. Click **Commit**, then **Sync Changes**.

Commit often. Clear messages matter: your commit history is part of your portfolio, because
it shows how you worked.

<!-- screenshot: Source Control panel with message box, Commit and Sync Changes buttons -->

### B5 · Check for the green ✓

Open your repository page on GitHub. Next to your latest commit message you'll see:

- 🟡 **a yellow dot**: the check is still running (usually 1–5 minutes).
- ✅ **a green check**: your notebooks ran from top to bottom.
- ❌ **a red cross**: something needs fixing. Click it → **Details**, then scroll to the
  summary table, which explains the problem in plain language.

Fix the issue, then commit and sync again. The check re-runs automatically.

### B6 · Stop your codespace

When you're done, **<> Code → Codespaces → ⋯ → Stop codespace**. Your free hours only count
down while a codespace is running. Codespaces also stop on their own after a period of
inactivity, and unused ones are eventually deleted. **Always sync before you leave**, because
anything not synced is lost.

## When the check shows ❌

| The message says… | What happened | How to fix it |
| --- | --- | --- |
| *uses a path that only works on one computer* | You used a path like `/Users/...` or `C:\...` | Change it to `data/raw/<file name>` |
| *uses Google Drive or Colab paths* | A notebook made for Colab isn't marked as a GPU notebook | Add `GPU` to its file name, or move its data into `data/raw/` |
| *FileNotFoundError* | The notebook needs a file that isn't in the repository | Upload the file to the right folder, and check the spelling (capital letters matter) |
| *NameError … used before the cell that creates it* | Cells only worked in the order you ran them by hand | Do **Restart & Run All**, then fix the first cell that errors |
| *ModuleNotFoundError* | A package isn't in `requirements.txt` | Ask the teaching team, and don't install it yourself |
| *GPU notebook was saved without any outputs* | You saved from Colab before running it | See [Guide 2](02_gpu-steps-with-colab.md) |
| *This file is missing* | A required output file hasn't been uploaded | Upload it to the folder named in the message |

## Uploading a file without Codespaces

To add a file, such as a CSV you downloaded from Colab:

1. On your repository page, open the folder it belongs in (e.g. `data/processed`).
2. Click **Add file → Upload files**.
3. Drag the file in, write a short message, and click **Commit changes**.

If you have a codespace open, click **Sync Changes** there afterwards, so it picks up the new
file before you keep working.

## Good to know

- **Never upload videos or photos of people.** They're too large for GitHub, and they identify
  participants. Keep them in Google Drive, and describe where they are in `data/raw/README.md`.
- **Feedback** from the teaching team arrives as comments on your commits or as **Issues** in
  your repository. You'll get a GitHub notification by email.
- **Keep your repository private until the course ends.** Making it public earlier lets
  classmates see your work.

## Prefer working on your own computer?

You can, with **[GitHub Desktop](https://desktop.github.com/)**, which uses the same buttons and
the same ideas:

1. Install GitHub Desktop and sign in.
2. On your repository page, click **<> Code → Open with GitHub Desktop**, then **Clone**.
3. Set up Python and Jupyter as described in the course's
   [How to Run the Notebooks](https://souvikmandal.info/teaching-learning/ls100/how-to-run)
   page, and work in the cloned folder.
4. In GitHub Desktop, type a summary, click **Commit to main**, then click **Push origin**.

Everything else, including Restart & Run All and the ✓ check, is the same.
