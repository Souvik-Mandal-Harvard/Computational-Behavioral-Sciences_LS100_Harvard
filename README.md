# LS100: Computational Behavioral Sciences
### Foundations of Data Science and Applied AI/ML for Conducting Research in Behavioral Sciences

Welcome to the repository for **LS100**, a 4-credit, research-based course "**Computational Behavioral Sciences**" that I teach at Harvard University. The course focuses on learning to conduct research that requires quantifying behavior in humans and other animals using automation, data science, and AI/ML methods.

This repository is the student-facing companion to the lectures I deliver during the course. However, I designed the materials in this repo to be self-sufficient, guiding you from **identifying a research question to framing testable hypotheses, using Python programming for collecting, processing, and analyzing data, and effectively communicating scientific findings**.

All content in this repo is open for non‑commercial use; feel free to learn from it or teach with it.

---

## What you will learn

LS100 follows the full research cycle. By the end of the course, you will be able to:

- Formulate behavior-related questions as testable scientific hypotheses.
- Collect and process video, audio, and other digital data.
- Use and fine-tune open-source AI/ML models (for example, pose estimation, object tracking, and audio embeddings) to extract behavioral metrics.
- Apply statistical analyses to analyze and validate results.
- Train classical ML models, both supervised and unsupervised, to make predictions on new data.
- Communicate findings through visualizations, oral presentations and written reports.
- Use large language models responsibly and effectively in research workflows.

No prior programming experience is required. Module `LS100_00B_Python-Fundamentals` is meant for learners with zero experience with Python programming.

---

## Who this repository is for

- Students enrolled in LS100 and learners interested in using computation to make sense of behavior.
- Learners seeking a data-backed understanding of human or animal movement and vocalization, or of behavioral data drawn from sources such as health portals and web services.
- Instructors seeking non-commercial teaching resources in computational and data science-based approach in ethology, behavioral sciences.

---

## Getting started
There are primarily two types of materials: reading guides (`.md` files) and Python Jupyter notebooks (`.ipynb files`). The materials are to get you started with your research journey, but do not necessarily serve as an end-to-end research project. Learners need to create their own code/ reports/ materials to conduct their own research. To start:

1. **Frame the Research Project** The Guide-01 in the folder **`LS100_00A_Research-Plans-And-Proposals` is meant to make you understand how to frame research plans and research proposals. 
2. Next, read **Computation Guide 01** (in `LS100_00B_Python-Fundamentals`) and set up your Python environment.
3. If you are new to Python programming, start with **`Notebook-01_Data-in-Python_Foundation`**, and follow the notebooks in numeric order.
4. Depending on your data type, choose either the `LS100_01A_Video-data` or the `LS100_01B_Audio-Data` folder, and follow the notebooks in numeric order.
5. Once you have data ready to analyze, work through the notebooks in `LS100_02_Data-Science_Stats` — and use the **Navigational Guide to Statistical Methods** and the **test-selection decision-tree poster** in that same folder to choose the right test.
6. The reading guide **Art of Communicating Science** in `LS100_03_Communication-and-Presentation` gives a comprehensive idea of presenting your findings effectively.

---

## Repository structure

```
Computational-Behavioral-Sciences_LS100_Harvard/
├── LS100_00_Document-00_Module-Description_...pdf   # Course overview
├── LS100_00_Document-01_Curriculum_...pdf           # Course curriculum / weekly timeline
├── LS100_00A_Research-Plans-And-Proposals/          # Framing research questions and proposals
├── LS100_00B_Python-Fundamentals/                   # Reading guides + Notebooks 01–05
├── LS100_01A_Video-data/                            # Video → pose → kinematics → behavior classification
├── LS100_01B_Audio-Data/                            # Digital audio → features → clustering
├── LS100_02_Data-Science_Stats/                     # Statistics notebooks + test-selection guide & poster
├── LS100_03_Communication-and-Presentation/         # Communicating and presenting science
├── LS100_Career-Guide01_Data-Careers.md             # Careers in the data landscape
├── LICENSE
└── README.md
```

The repository is organized to follow the research workflow — from framing a question (`00A`), to Python and data skills (`00B`), to collecting and processing data (`01A` / `01B`), to analysis (`02`), to communication (`03`). Each module folder contains its notebooks (numbered in the recommended order) together with the reading guide(s) relevant to that stage.

---

## Course documents (repository root)

- **Document 00 — Module Description**: a one-page overview of the course.
- **Document 01 — Curriculum**: the topic-by-topic / weekly timeline.
- **Career Guide 01 — Data Careers**: a guide to roles in the data landscape and how course skills map onto them.

---

## Module 00A - Research Plans and Proposals

How to turn an interest into a researchable question and a credible proposal.

- **Research Guide 01 — Writing Research Plans and Proposals**: framing questions, hypotheses, and study design.

---

## Module 00B - Python Fundamentals

A self-contained, five-notebook path from basic Python syntax to object-oriented design framed around behavioral research examples, plus two written companions for setup and terminology.

Reading guides in this folder:

- **Computation Guide 01 — Getting Started with Python** (installation, environments, notebooks)
- **Computation Guide 02 — Essential Python Terminologies and Concepts**

| # | Notebook | What it covers |
| :--- | :--- | :--- |
| 01 | Data in Python - Foundation | Variables, data types, data structures, pandas, NumPy, operators |
| 02 | Data Automation | More pandas/NumPy, conditionals, loops, reusable functions |
| 03 | Data Visualization | matplotlib, seaborn, Plotly; distributions, time series, ethograms, publication-ready figures |
| 04 | Computational Thinking (DSA and Fluency) | Comprehensions, choosing data structures, Big-O intuition, algorithmic patterns, practice problems |
| 05 | Classes and Decorators | Object-oriented design, encapsulation, `@property`, `@dataclass` in a study data-management example |

---

## Module 01A - Video Data

An end‑to‑end pipeline that turns raw video into quantified, classifiable behavior. Work through it in numbered order.

| Stage | Notebook | What it covers |
| :--- | :--- | :--- |
| 00 | Getting Started | Loading and inspecting video frames in Python |
| 01 | Video Processing - Frame Reduction | Lowering frame rate while preserving clip duration |
| 01 | Video Processing - Video Clipping | Generating paired clips from longer recordings |
| 01 | Video Processing - Video Chunker | Splitting a video into fixed-frame-count chunks |
| 02 | Pose Estimation - MediaPipe | Extracting body keypoints from video with MediaPipe |
| 02 | Pose Estimation - YOLO | Pose estimation for biomechanics applications with YOLO |
| 02 | Pose Estimation - YOLOv8 GPU (Colab) | GPU-based keypoint extraction for single files and batches |
| 02 | Training a Custom YOLO Model | Training a model to track custom keypoints or objects (Label Studio to training pipeline) |
| 03 | Extracting Joint Angles | Computing joint angles from MediaPipe and YOLO landmarks |
| 04 | Deriving Indices from Angles | Converting angle time series into biomechanical indices |
| 05 | Sequence-Based Classification | Preparing data for training behavior classification models from pose sequences|
| 05 | Sequence-Based Classification | Training behavior classification models |

---

## Module 01B - Audio Data

From the physics of digital sound to AI-assisted feature extraction and clustering. The folder also includes the companion guide **Introduction to Digital Audio in Python**.

| # | Notebook | What it covers |
| :--- | :--- | :--- |
| 00 | Foundation - Understanding Digital Audio | Building audio from numbers, microphone capture, file I/O, waveforms, and spectrograms |
| 01 | Feature Extraction from Digital Audio | DFT, spectrograms, tempo and beat, musical meter, chords, melody (CREPE-based pitch tracking) |
| 01B | Music Feature Extraction (AI/ML) | Extracting learned audio embeddings from music tracks |
| 02 | Feature Extraction - Batch Process | Running feature extraction across folders of audio files |
| 03 | Digital Audio Clustering | Embeddings to k-means/HDBSCAN with PCA and UMAP visualization |

---

## Module 02 - Data Science and Statistics

Notebooks for analyzing your processed data, plus reference guides for choosing the right test.

| Notebook | What it covers |
| :--- | :--- |
| Classical Statistical Tests | Hypothesis-testing logic, t-tests, ANOVA, correlation, regression, and non-parametric alternatives |
| Intro to Linear Mixed-Effects Models | Why simple t-tests are not enough; fitting and interpreting LMMs for repeated-measures behavioral data |
| Helper - Finding Local Extremum in Data | Trimming time-series data files at a detected event or inflection point |

Reference guides in this folder:

- **Navigational Guide to Statistical Methods** — a dictionary that maps a research question and data features to the appropriate test.
- **Test-Selection Decision-Tree** — a print-ready poster (PDF) and an editable vector source (SVG) for quick at-a-glance test selection.

---

## Module 03 - Communication and Presentation

Turning results into a clear scientific story.

- **Research Guide 02 — The Art of Communicating Science**: structuring talks, designing slides and figures, and presenting findings effectively.

---

## Reading guides at a glance

The written guides live alongside the stage of the workflow they support:

| Guide | Location |
| :--- | :--- |
| Research Guide 01 — Writing Research Plans and Proposals | `LS100_00A_Research-Plans-And-Proposals/` |
| Computation Guide 01 — Getting Started with Python | `LS100_00B_Python-Fundamentals/` |
| Computation Guide 02 — Essential Python Terminologies and Concepts | `LS100_00B_Python-Fundamentals/` |
| Introduction to Digital Audio in Python | `LS100_01B_Audio-Data/` |
| Navigational Guide to Statistical Methods (+ decision-tree poster) | `LS100_02_Data-Science_Stats/` |
| Research Guide 02 — The Art of Communicating Science | `LS100_03_Communication-and-Presentation/` |
| Career Guide 01 — Data Careers | repository root |

---

## Suggested learning path

1. **Frame your study** with Research Guide 01 in `LS100_00A_Research-Plans-And-Proposals`.
2. **Build Python fluency** with Module `LS100_00B_Python-Fundamentals` (Notebooks 01 to 05) and its computation guides.
3. **Choose your data modality**: Module 01A (video/movement), Module 01B (audio/vocalization), or both, and run the processing pipelines.
4. **Analyze your outcomes** with Module 02, using the statistical-methods guide and decision-tree poster to pick the right test.
5. **Communicate your findings** with Research Guide 02 in `LS100_03_Communication-and-Presentation`.

---

## Example project tracks

You are encouraged to design your own question. Common directions include exploring patterns in some data of interest supported with:

- **Movement Analytics** for sports, dance, and rehabilitation: pose tracking to quantify posture, efficiency, and injury risk.
- **Vocal or instrument learning**: by extracting audio features (for example, pitch stability and timing), tracking progress over time, designing wellness soundscape, music therapy, etc.
- **Behavior prediction from video**: by extracting poses, classifying behaviors, and forecasting behavior in novel videos.
- **Forecasting Human Behavior from Digital Traces**: analyzing human activity data gathered from the internet alongside external variables, such as climate trends or economic indicators.

---

## Student expectations

- Work in teams of 2-4, while submitting assignments individually.
- Expected effort: approximately 6-10 hours per week.
- Attend weekly meetings and review assigned materials in advance.
- Present at least one relevant research paper during the semester.
- Participate actively in discussion, peer feedback, and project presentations.

---

## Requirements

- Computer (macOS, Windows, or Linux) with at least 8 GB RAM and internet access.
- Google account (for Colab in GPU-focused notebooks).
- Access to video and/or audio data.
- Prior programming experience is helpful but not required.

---

## Tech stack

| Category | Tools and Libraries |
| :--- | :--- |
| **Language** | Python 3.10+ |
| **Data processing** | pandas, NumPy, SciPy |
| **Visualization** | Matplotlib, seaborn, Plotly |
| **Computer vision** | OpenCV, MediaPipe, Ultralytics (YOLO) |
| **Audio** | librosa, CREPE, audio embedding models |
| **Statistics** | statsmodels |
| **Machine learning** | scikit-learn, PyTorch, HDBSCAN, UMAP |
| **Environment** | Jupyter Notebook, Google Colab, Anaconda, GitHub Codespaces |

---

## How to use and cite this repository

**How to use it.** The materials are free to use for learning and non-commercial teaching:

- **Learners:** follow the [Suggested learning path](#suggested-learning-path) above. You can run the notebooks three ways — download and run locally, open them in Google Colab, or fork the repository and work in GitHub Codespaces.
- **Instructors:** you are welcome to adopt or adapt any module, notebook, or reading guide for your own non-commercial teaching. Attribution is appreciated (see below).
- **Researchers:** the video, audio, and statistics pipelines are designed to be reused on your own behavioral data.

**How to cite it.** If these materials support your teaching or research, please cite them:

> Mandal, S. (2026). *LS100: Computational Behavioral Sciences — Foundations of Data Science and Applied AI/ML for Conducting Research in Behavioral Sciences* [Course materials]. Harvard University. GitHub repository: https://github.com/Souvik-Mandal-Harvard/Computational-Behavioral-Sciences_LS100_Harvard

BibTeX:

```bibtex
@misc{mandal2026ls100,
  author       = {Mandal, Souvik},
  title        = {{LS100: Computational Behavioral Sciences --- Foundations of Data Science
                  and Applied AI/ML for Conducting Research in Behavioral Sciences}},
  year         = {2026},
  howpublished = {Course materials, Harvard University},
  note         = {GitHub repository},
  url          = {https://github.com/Souvik-Mandal-Harvard/Computational-Behavioral-Sciences_LS100_Harvard}
}
```

---


## License and use

These materials are licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)** — see [LICENSE](LICENSE). You are free to **share and adapt** them for **non-commercial** purposes, provided you give **attribution**. For commercial use, please contact the author.

*LS100 - Computational Behavioral Sciences, Harvard University*
