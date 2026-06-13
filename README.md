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

No prior programming experience is required. Module `LS100_00_Python-Fundamentals` is meant for learners with zero experience with Python programming.

---

## Who this repository is for

- Students enrolled in LS100 and learners interested in using computation to make sense of behavior.
- Learners seeking a data-backed understanding of human or animal movement and vocalization, or of behavioral data drawn from sources such as health portals and web services.
- Instructors seeking non-commercial teaching resources in computational and data science-based approach in ethology, behavioral sciences.

---

## Getting started
There are primarily two types of materials: Reading guides and Python Jupyter notebooks. The materials are to get you started with your research journey, but do not necessarily serve as an end-to-end research project. Learners need to create their own code/ reports/ materials to conduct their own research. To start:

1. Open **LS100_Guides-and-Readings -> Research Guide 01** to understand how to frame research plans and research proposals.
2. Next, read the **Computation Guide 01** and set up your Python environment.
3. If you are new to Python Programming, start with **Module 00, Notebook 01**. Follow notebooks in numeric order.
4. Depending on your data type, choose either the `LS100_01A_Video-data` or the `LS100_01B_Audio-data` folder, and follow the notebooks in numeric order.
5. Once you have data ready to analyze, check the notebooks in the `LS100_02_Data-Science_Stats` folder.
6. The reading guide `Art-of-Communicating-Science` in the "LS100_Guides-and-Readings" folder gives a comprehensive idea of presenting your findings effectively.

---

## Repository structure

```
Computational-Behavioral-Sciences_LS100_Harvard/
├── LS100_00_Python-Fundamentals/   # Notebooks 01–05: learn Python for research, from scratch
├── LS100_01A_Video-data/           # Video → pose → kinematics → behavior classification
├── LS100_01B_Audio-Data/           # Digital audio → features → clustering
├── LS100_02_Data-Science_Stats/    # Statistics and data-wrangling helpers
├── LS100_Guides-and-Readings/                  # Written guides (Python, research, communication)
├── LS100_Document-00_Module-Description_Computational-Behavior-Science_LastUpdated-20250529.pdf
├── LICENSE
└── README.md
```

Each module folder contains Jupyter notebooks numbered in the recommended order.

---

## Module 00 - Python Fundamentals

A self-contained, five-notebook path from basic Python syntax to object-oriented design framed around behavioral research examples.

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
| 02 | Pose Estimation - YOLO GPU (Colab) | GPU-based keypoint extraction for single files and batches |
| 02 | Training a Custom YOLO Model | Training a model to track custom keypoints or objects (Label Studio to training pipeline) |
| 03 | Extracting Joint Angles | Computing joint angles from MediaPipe and keypoint landmarks |
| 04 | Deriving Indices from Angles | Converting angle time series into biomechanical indices |
| 05A / 05B | Sequence-Based Classification | Preparing pose sequences and training behavior classification models |

---

## Module 01B - Audio Data

From the physics of digital sound to AI-assisted feature extraction and clustering.

| # | Notebook | What it covers |
| :--- | :--- | :--- |
| 00 | Foundation - Understanding Digital Audio | Building audio from numbers, microphone capture, file I/O, waveforms, and spectrograms |
| 01 | Feature Extraction from Digital Audio | DFT, spectrograms, tempo and beat, musical meter, chords, melody (CREPE-based pitch tracking) |
| 01B | Music Feature Extraction (AI/ML) | Extracting learned audio embeddings from music tracks |
| 02 | Feature Extraction - Batch Process | Running feature extraction across folders of audio files |
| 03 | Digital Audio Clustering | Embeddings to k-means/HDBSCAN with PCA and UMAP visualization |

---

## Module 02 - Data Science and Statistics

| Notebook | What it covers |
| :--- | :--- |
| Classical Statistical Tests | Introduction to data analysis | 
| Intro to Linear Mixed-Effects Models | Why simple t-tests are not enough; fitting and interpreting LMMs for repeated-measures behavioral data |
| Helper - Finding Local Extremum in Data | Trimming time-series data files at a detected event or inflection point |

---

## LS100_Guides-and-Readings

Written companions to the notebooks:

- **Document 00 - Module Description** (course overview)
- **Document 01 - Curriculum** (14-week timeline)
- **Computation Guide 01 - Getting Started with Python** (installation, environments, notebooks)
- **Computation Guide 02 - Essential Python Terminologies and Concepts**
- **Research Guide 01 - Writing Research Plans and Proposals**
- **Research Guide 02 - The Art of Communicating Science**

---

## Suggested learning path

1. **Start with Module 00** to build Python fluency (Notebooks 01 to 05).
2. **Choose your data modality**: Module 01A (video/movement), Module 01B (audio/vocalization), or both.
3. **Quantify and model behavior** using the video/audio pipelines.
4. **Use Module 02** to analyze outcomes with statistical methods.
5. **Read the guides in LS100_Guides-and-Readings** to strengthen research design and scientific communication.

---

## Example project tracks

You are encouraged to design your own question. Common directions include exploring patterns in some data of interest supported with:

- **Movement Analytics** for sports, dance, and rehabilitation: pose tracking to quantify posture, efficiency, and injury risk.
- **Vocal or instrument learning**: extracting audio features (for example, pitch stability and timing), tracking progress over time, designing soundscape wellness, music therapy, etc.
- **Behavior prediction from video**: extracting poses, classifying behaviors, and forecasting behavior in novel videos.

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


## License and use

Released for non-commercial use. See [LICENSE](LICENSE).

You are welcome to use these materials for learning and non-commercial teaching. Attribution is appreciated.

*LS100 - Computational Behavioral Sciences, Harvard University*
