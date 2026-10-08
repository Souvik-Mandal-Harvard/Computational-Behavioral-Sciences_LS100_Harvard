# Data statement

<!-- Fill this in before you make the repository public. Behavioral data often comes from
     people, so treat this page as seriously as your methods section.
     Guide: ls100-guides/03_make-it-portfolio-ready.md → "Check your data before going public". -->

**Source:** _Who collected the data, when, and how (e.g. "Recorded by me with a phone camera
at 30 fps", "Public dataset: <name and link>", "Provided by the LS100 teaching team")._

**Participants and consent:** _How many participants, and what they agreed to. Only share data
in this repository if the consent form allows it. Write "No human participants" if that applies._

**What is shared here:**

- [ ] _e.g. Anonymized tables (participant IDs like P01, no names, emails or birth dates)_
- [ ] _e.g. Keypoint coordinates extracted from video (no images or video)_

**What is NOT shared, and where it lives:** _e.g. "Raw videos show participants' faces and
are kept in a private Google Drive folder. They are excluded from this repository."_

**Files:**

| File | Description | Columns |
| --- | --- | --- |
| `example_reaction_times.csv` | _Example data from the template. Replace it with your own._ | `participant`, `condition`, `trial`, `reaction_time_ms` |

**Rule:** files in this folder are never edited. Notebooks load them and write any changes to
`data/processed/`.
