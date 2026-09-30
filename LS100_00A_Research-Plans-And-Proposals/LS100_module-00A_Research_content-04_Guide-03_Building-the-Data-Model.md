---
subtitle: 'LS100 — Module 00A · Research Plans & Proposals'
title: 'Building the Data Model: From Raw Data to Analysis-Ready Tables'
short_title: 'Guide 03: Data Model'
exports:
  - format: pdf
    template: lapreprint-typst
    output: exports/LS100_module-00A_Research_content-04_Guide-03_Building-the-Data-Model_LastUpdated-20260930.pdf
    id: rg03-pdf
downloads:
  - id: rg03-pdf
    title: Download the article (PDF)
---
*Authored by* **Souvik Mandal, Ph.D.**

*Project Leader & Instructor, Computational Behavioral Sciences, LS100, FAS, Harvard University* | LinkedIn ID: [souvik-mandal-phd](https://www.linkedin.com/in/souvik-mandal-phd)

---

A **data model** is the blueprint of how your data is organized at every step between the sensor and the statistical test. *Converting the Problem to a Research Framework* (Section 5) explains why you need one. This guide is the procedure for building it.

## The three stages of data

Every LS100 project moves data through the same three stages:

| Stage | What it is | One row is |
|---|---|---|
| **Primary** | What the sensor recorded (video, audio, logs). Never edited. | not a table — one file per recording |
| **Secondary** | What a model or algorithm extracts from one primary file. | one unit of extraction (a frame, a time window, an event) |
| **Tertiary** | Analysis-ready variables derived from the secondary data. | one unit of analysis |

You will describe this flow in three passes, each more concrete than the last: **conceptual** (a diagram), **logical** (table schemas), and **physical** (folders, files, and Python).

## Assignment 02: What you hand in

One Jupyter notebook that contains the diagram, the schemas, and the folder layout in Markdown cells, followed by code that takes **one** primary file and produces its **secondary dataframe**. Producing the tertiary dataframe as well earns a bonus.

## Pass 1 — Conceptual: draw the flow

No technical detail yet. Name the **entities** your study tracks (participant, session, trial, recording) and draw how data moves between stages. Every arrow must be labelled with the transformation that performs it.

```text
[Entity: participant → session → trial]
              │ record
              ▼
      PRIMARY: one raw file per trial
              │ extract  (model / algorithm)
              ▼
      SECONDARY: one table per raw file
              │ derive + aggregate  (your code)
              ▼
      TERTIARY: one table for the whole study
              │
              ▼
      statistical analysis
```

If you cannot name the transformation on an arrow, you have found a gap in your plan.

## Pass 2 — Logical: write the table schemas

Write one schema for the secondary table and one for the tertiary table, independent of any software. Each column gets one line:

| Column | Type | Unit | Role | Comes from |
|---|---|---|---|---|
| `participant_id` | text | — | ID | file name |
| `<unit_index>` | integer | — | ID | extraction |
| `<feature>` | float | `<unit>` | measure | `<model or formula>` |

Three rules:

1. **IDs on every row.** Each table carries the identifiers of every entity above it, so a row can always be traced back to its participant, session, trial, and raw file.
2. **One row, one meaning.** State it in a sentence under each schema: "one row is one ______."
3. **Every column has a source.** A tertiary column names the secondary columns and the formula that produce it. A column with no source cannot be computed.

Add a separate **metadata table** for attributes recorded by hand (one row per participant or session: condition, date, consented covariates). It joins to the tertiary table through the IDs.

## Pass 3 — Physical: folders, file names, and Python

**Folders.** One folder per stage; data only moves downward.

```text
project/
├── data/
│   ├── 01_primary/      # raw files, read-only
│   ├── 02_secondary/    # one table per raw file
│   ├── 03_tertiary/     # one analysis-ready table
│   └── metadata.csv
└── notebooks/
```

**File names.** Encode the IDs in the name, in a fixed order, separated by underscores: `<participant>_<session>_<trial>.<ext>`. No spaces, no "final", no dates typed by hand. A secondary file keeps the name of the primary file it came from, so the link between them never depends on memory.

**Python skeleton.** Declare the schema in code before writing any extraction logic, then make the notebook check its own output against it.

```python
from pathlib import Path
import pandas as pd

RAW = Path("data/01_primary/P01_S01_T01.mp4")            # one primary file
ids = dict(zip(["participant_id", "session_id", "trial_id"],
               RAW.stem.split("_")))                      # IDs from the file name

SECONDARY_COLS = [*ids, "unit_index", "time_s", "feature_1"]   # your Pass 2 schema

def extract(raw_path: Path) -> list[dict]:
    """Primary → secondary: return one dict per unit of extraction."""
    # the extraction code goes here
    return []

secondary = pd.DataFrame(extract(RAW)).assign(**ids).reindex(columns=SECONDARY_COLS)
assert secondary.columns.tolist() == SECONDARY_COLS

out = Path("data/02_secondary") / f"{RAW.stem}.csv"
out.parent.mkdir(parents=True, exist_ok=True)
secondary.to_csv(out, index=False)
```

For the extraction step, adapt the course notebooks: [pose estimation from one video](https://souvikmandal.info/teaching-learning/ls100/ls100-module-01a-video-data-content-08-stage-02-cv/) for video data, and [audio data foundation](https://souvikmandal.info/teaching-learning/ls100/ls100-module-01b-audio-data-content-01-notebook-00/) for audio data.

**Bonus — tertiary.** Group the secondary dataframe by its IDs, compute the derived variables in your tertiary schema, and save the result to `03_tertiary/`.

## Notebook rules

- Every code cell is preceded by a Markdown cell that states **why** the step is needed and **what** the code does. Write it for a classmate who has not seen your project.
- The notebook runs top to bottom on a fresh kernel, from one raw file, without manual edits between cells.
- Paths are relative to the project folder; nothing points to your personal machine.
- The last cell displays `secondary.head()` and `secondary.shape`, so the output can be checked against your schema at a glance.

:::{dropdown} Submission Checklist

- [ ] Flow diagram with a named transformation on every arrow.

- [ ] Secondary and tertiary schemas, each with a "one row is one ______" sentence.

- [ ] Every table carries the IDs of all entities above it.

- [ ] Folder layout and file-naming pattern stated, and followed by the files you submit.

- [ ] Notebook turns one primary file into a saved secondary dataframe whose columns match the schema.

- [ ] A Markdown cell explaining *why* and *what* sits above every code cell.

- [ ] (Bonus) Tertiary dataframe produced and saved.

:::
