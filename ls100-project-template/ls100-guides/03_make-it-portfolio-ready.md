# Guide 3 · Make Your Project Portfolio-Ready

*Authored by* **Souvik Mandal, Ph.D.**

*Project Leader & Instructor, Computational Behavioral Sciences, LS100, FAS, Harvard University* | Linkedin ID: [souvik-mandal-phd](https://www.linkedin.com/in/souvik-mandal-phd)

---

A recruiter, hiring manager or admissions reader will usually spend **under two minutes** on
your repository. In that time they want to see three things:

1. **What you did and found**, in plain language, at the top of the README.
2. **That it's real and it works:** clean notebooks, a green reproducibility badge, sensible
   structure.
3. **How you think:** clear reasoning, honest limitations, careful handling of data.

This guide walks you through getting there. Do it at the end of the course, once your
instructor says repositories can be made public.

## Step 1 · Write the README

Your `README.md` already has the sections you need. Fill in every placeholder in *italics*.

- **Title:** name the finding, not the course. *"Dual-task walking shortens stride length"*
  beats *"LS100 Project"*.
- **One-sentence summary** right under the title: question, method, result.
- **Your best figure** near the top. People look at images before they read.
- **Results with numbers:** sample size, effect size, test used. Vague claims ("there was a
  difference") are less convincing than "*reaction time rose by 52 ms on average, t(3) = 9.1,
  p = .003*".
- **Limitations:** two or three honest sentences. This signals scientific maturity.
- **About:** your name, LinkedIn and GitHub links.

**Fix the badges:** in the README, replace `OWNER/REPO` (it appears twice) with your username
and repository name, e.g. `jdoe/gait-dual-task-analysis`. Then the badge shows your project's
real reproducibility status, and the Codespaces button opens *your* project.

**License:** open `LICENSE` and replace `<YEAR>` and `<YOUR NAME>`. The MIT License lets others
reuse your code with credit, which is the most common choice for portfolio projects.

## Step 2 · Clean up the notebooks

A notebook in a portfolio is a **report that runs**, not a scratchpad.

- Start each notebook with a Markdown cell: a title and two or three sentences on what it does.
- Add a short Markdown heading before each section ("Load data", "Compute joint angles", …).
- Delete scratch cells, commented-out experiments, and huge printouts of whole tables (use
  `.head()`).
- Give every plot a title, axis labels with units, and a legend where needed.
- Finish with a short Markdown cell summarizing what the notebook found.
- **Restart & Run All**, then commit, so the saved outputs match the code.

> [!TIP]
> Read your notebook on GitHub, not in Codespaces. That's what visitors will see.

## Step 3 · Check your data before going public

Behavioral data usually comes from people. Once a repository is public, assume anything in it
can be copied and kept forever, even if you delete it later.

Go through this list before you change the visibility:

- [ ] **No names, emails, student IDs, birth dates, or other identifiers** in any file,
      including notebook outputs. Use codes like `P01`.
- [ ] **No videos, photos or audio of participants.** Keypoint coordinates and extracted
      features are usually fine. Faces and voices are not.
- [ ] **The consent form allows public sharing** of what you are sharing. If you're unsure,
      ask the teaching team. If it doesn't allow sharing, remove the data files (see below)
      and describe the data in words instead.
- [ ] **Public datasets are credited** with a link and their license.
- [ ] **`data/raw/README.md` is filled in**: source, consent, what's shared, what isn't.

**If some data can't be shared,** keep the analysis public and the data private:

1. Add the file names to `.gitignore` (e.g. `data/raw/participants_full.csv`).
2. Delete them from the repository (on GitHub: open the file → **⋯ → Delete file**).
3. Explain in `data/raw/README.md` that the data is available on request or not shareable.

> [!WARNING]
> Deleting a file removes it from the current version, but it **stays in the commit history**.
> If identifiable data was ever committed, don't make the repository public. Ask the teaching
> team, who can help you start a clean copy.

## Step 4 · Tidy the repository

- **Remove course scaffolding (optional):** you can delete the `ls100-guides/` folder. The
  README credits the course either way.
- **Remove template leftovers:** if you didn't use the example reaction-time data, delete
  `data/raw/example_reaction_times.csv`, `data/processed/mean_reaction_times.csv` and
  `figures/reaction_times.png`, and update the README's figure.
- **Check the green ✓** on your latest commit.

## Step 5 · Make it public and easy to find

1. **Settings → General → Danger Zone → Change visibility → Make public.** Only do this once
   your instructor says the course allows it, and after Step 3.
2. On your repository page, click the ⚙️ next to **About** (top right):
   - Add a one-line **description**.
   - Add **topics**, e.g. `python`, `data-science`, `pose-estimation`, `behavioral-science`,
     `computer-vision`, `statistics`. These make your project searchable.
3. **Pin it to your profile:** on your GitHub profile page, click **Customize your pins** and
   select this repository.
4. **(Optional) Add a profile README:** create a public repository named exactly like your
   username (e.g. `jdoe/jdoe`). Its README appears at the top of your GitHub profile, where
   you can introduce yourself and link your projects.

## Step 6 · Share it

- **Résumé:** under *Projects*, give the project title, one line on the result, and the
  repository link.
- **LinkedIn:** add it under **Projects** (or **Featured**), with the link and your best figure.
- **Applications and interviews:** be ready to walk through the pipeline in two minutes:
  question → data → GPU step → analysis → result → limitation.

## Final checklist

- [ ] README: title, one-line summary, figure, question, data, approach, results,
      limitations, about.
- [ ] Badges show your `username/repository`, and the reproducibility badge is green.
- [ ] `LICENSE` has your name and the year.
- [ ] Notebooks read like reports and were last run top to bottom.
- [ ] Data checked: no identifiable information, consent respected, `data/raw/README.md` complete.
- [ ] Repository is public, with a description and topics, and pinned to your profile.
