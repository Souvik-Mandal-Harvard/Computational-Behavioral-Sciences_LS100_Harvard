---
title: Module 01A — Video Data
short_title: 01A · Video Data
---

An end-to-end pipeline that turns raw video into quantified, classifiable behavior: video processing, pose estimation (MediaPipe and YOLO), joint angles, derived indices, and sequence-based classification. Work through it in numbered order.

**Prerequisites:** Module 00B (Python Fundamentals)  
**Estimated time:** ~12–18 hours

After this module you can extract body keypoints from video, compute kinematic features, and train a behavior classifier.

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

## Content in this module

:::{toc}
:context: children
:::
