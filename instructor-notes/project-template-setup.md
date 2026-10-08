# Instructor notes: LS100 project template

`ls100-project-template/` (on `main` in the course repo) contains everything students need:
starter notebook, folder structure, guides, reproducibility check and Codespaces setup.
Students create **their own repository** from it, in their personal GitHub account, so they
keep the project after the course and can show it to employers.

Students only touch Markdown and `.ipynb` files. The rest (`.github/`, `.devcontainer/`,
`requirements.txt`, `.gitignore`) is infrastructure they never need to edit.

## How students get it

GitHub can't create a repository from a sub-folder, so the folder is **mirrored** into a
standalone template repository by `.github/workflows/sync-project-template.yml`. Edit the
folder here; every push to `main` that touches it updates the template repo automatically.

```
course repo (main)                          template repo                  student repos
ls100-project-template/  ── sync workflow ──▶  ls100-project-template  ── "Use this template" ──▶  jdoe/gait-analysis
```

## One-time setup

1. **Create the template repo:** a new **public**, empty repository
   `Souvik-Mandal-Harvard/ls100-project-template`. Under **Settings → General**, tick
   **Template repository**. (If you use a different name or owner, update `TEMPLATE_REPO` in
   the sync workflow and the links in `ls100-guides/01_submitting-assignments-with-github.md`
   and the template `README.md`.)
2. **Create a deploy key** on your computer:
   ```bash
   ssh-keygen -t ed25519 -C "ls100-template-sync" -f ls100_template_key -N ""
   ```
   - Template repo → **Settings → Deploy keys → Add deploy key**: paste
     `ls100_template_key.pub`, and tick **Allow write access**.
   - Course repo → **Settings → Secrets and variables → Actions → New repository secret**:
     name `TEMPLATE_REPO_DEPLOY_KEY`, value = contents of `ls100_template_key` (the private key).
   - Delete both key files from your computer afterwards.
3. **Run the sync once:** course repo → **Actions → Sync project template → Run workflow**.
   Check that the template repo now has the files, including `.github/` and `.devcontainer/`.
4. **Verify the reproducibility check** passes on the template repo (**Actions** tab, green ✓).
5. Post on the course page: the template link, and the GitHub username(s) students should add
   as collaborators.

## Each semester / project

- **Starter content:** replace `01_analysis.ipynb` and `data/raw/example_reaction_times.csv`
  with the project's starter notebook(s) and data, or keep the example as a model.
  If you change the example, re-run the notebook so the committed outputs, `figures/` and
  `data/processed/` match the README's figure.
- **GPU notebooks:** any notebook that needs Colab must have `GPU` in its file name, e.g.
  `02_pose-estimation_GPU.ipynb`. The check skips re-running these but requires saved outputs.
- **Packages:** trim `requirements.txt` to what the project needs. Use
  `opencv-python-headless` (not `opencv-python`) on GitHub's machines.
- **Required outputs:** list files students must produce in Colab, with required CSV columns,
  in `.github/expected-outputs.txt`.
- **Fallback:** provide precomputed GPU outputs (e.g. keypoint CSVs for the course videos) so a
  failed Colab run never blocks the analysis stages.

## Collecting and grading work

Student repositories are in their own accounts, so GitHub Classroom isn't used.

| Need | How |
| --- | --- |
| Access | Students keep repos **private** during the course and add the teaching team as **collaborators** (Guide 1, step A3). |
| Submission | Students submit their repo link once (e.g. on Canvas). |
| Deadline | Commit dates come from the student's machine, so they aren't proof of submission time. For each deadline, have students submit the link to their latest commit (repo page → commit history → copy the commit's URL). The submission system timestamps it, and the commit's contents can't change afterwards. |
| Reproducibility | Green ✓ next to the graded commit means every non-GPU notebook ran top to bottom in a fresh session. |
| GPU notebooks | Read their saved outputs on GitHub. The check fails if they were saved without outputs. |
| Feedback | Comment directly on a commit (line comments are supported), or open an **Issue** in the student's repo. Students get an email notification. |
| Integrity | Repos stay private until grades are final. Then students follow Guide 3 to go public. |

## What the reproducibility check does

`.github/workflows/reproducibility-check.yml` runs `.github/scripts/check_notebooks.py` on
every push to a student repo:

- Notebooks whose file name contains `GPU` are not re-run, but must contain saved outputs.
- Every other notebook is executed in a fresh kernel, with 10 minutes allowed per cell.
- Code with machine-specific paths (`/Users/…`, `C:\…`) or Colab/Drive paths fails with an
  explanation, which catches the most common "works on my computer" problem.
- Errors include beginner-oriented hints (missing file, missing package, out-of-order cells).
- Results appear as a plain-language table on the run's summary page.

It also powers the README badge, which works as a visible signal of reproducibility in
students' portfolios.

## Privacy

Students' projects often contain human-participant data. Guide 3 has a checklist to complete
before going public (no identifiers, no faces or voices, consent allows sharing), and the
template's `.gitignore` blocks videos by default. Remind students that deleting a file doesn't
remove it from Git history. A repo that ever contained identifiable data should not be made
public. Help the student start a clean copy instead.
