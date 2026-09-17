<div align="center">

# 🚘 YOLOv8 Real-Time Vehicle & Object Counter

![YOLOv8](https://img.shields.io/badge/Model-YOLOv8n-00FFFF?style=for-the-badge&logo=ultralytics&logoColor=black)
![OpenCV](https://img.shields.io/badge/Computer_Vision-OpenCV-FF00FF?style=for-the-badge&logo=opencv&logoColor=white)
![Google Colab](https://img.shields.io/badge/Platform-Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-00FF00?style=for-the-badge)

<p align="center">
  <b>A Cyberpunk-styled HUD Computer Vision pipeline built for Google Colab. Detects, counts, and verifies target object density using deep learning.</b>
</p>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AND-SHAL-0813/vehicle-object-counter-yolov8/blob/main/vehicle_object_counter_yolov8.ipynb)

</div>

---
#### Key Project Objectives:
1. **Automated Recognition:** Accurately detect and classify target object categories (cars, buses, trucks, pedestrians).
2. **Interactive Verification:** Compare real-time AI object detection tallies against user-specified expected counts.
3. **Visual Output HUD:** Draw high-contrast bounding boxes, corner target crosshairs, confidence ratings, and status indicators directly onto image frames.
4. **Structured Output Logging:** Persist categorical counts, verification status flags (`MATCHED` / `DEVIATION`), and timestamps to disk.
5. **Zero Local Configuration:** Build a fully functioning workflow requiring zero local installation or terminal manipulation.
---
## ⚡ Key Highlights

* **Zero Terminal / Cloud Native:** Runs 100% inside Google Colab—no C++ build tools, local environments, or terminal commands needed.
* **Cyberpunk HUD Renderer:** Overlays dark-glass status banners, neon bounding boxes, target corner crosshairs, and live metric indicators.
* **Expected vs. Actual Verification:** Compares user-defined target object counts against real-time AI detections to calculate status flags (`MATCHED` or `DEVIATION`).
* **Automated Data Export:** Logs detection category counts and verification metrics to `outputs/vehicle_counts.csv`.

---

## 📂 Repository Architecture

```text
vehicle-object-counter-yolov8/
|
├── README.md
├── main.py
├── requirements.txt
├── vehicle-object-counter-yolov8.ipynb
├── LICENCE

```
---
###  PROJECT METADATA
* **Project Title:** Real-Time Vehicle and Object Counter using YOLOv8
* **Framework / Model:** Ultralytics YOLOv8 (Nano Architecture)
* **Core Libraries:** OpenCV, Pandas, Matplotlib, NumPy
* **Deployment Platform:** Google Colab (T4 GPU Accelerated)
* **Version Control:** Public GitHub Repository
* **Submission Date:** September 18, 2026


---
###  PROBLEM STATEMENT & OBJECTIVES
Manual traffic auditing and object density verification are labor-intensive and prone to human error. Modern intelligent transportation systems require light, cloud-deployable computer vision solutions that can process visual inputs with minimal latency.

---
###  5-CELL COLAB WORKFLOW

The implementation follows a modular 5-cell structure inside Google Colab:

| Cell | Stage Name | Technical Function |
| :---: | :--- | :--- |
| **01** | **Environment Setup** | Installs `ultralytics`, `opencv-python-headless`, `pandas`, and dependencies. |
| **02** | **Workspace Setup** | Builds programmatic workspace directories (`inputs/`, `outputs/`) and pulls sample test images. |
| **03** | **Interactive Input** | Captures user-entered expected object density value via Colab input prompts. |
| **04** | **Raw Image Display** | Renders original raw test photo inside the notebook prior to deep learning execution. |
| **05** | **AI HUD Processing** | Executes YOLOv8 inference, applies transmissive Cyberpunk HUD graphics, renders final image, and exports CSV logs. |

---

###  IMPLEMENTATION DETAILS

####  Deep Learning Model (YOLOv8)
The system leverages the **YOLOv8 Nano (`yolov8n.pt`)** lightweight convolutional network. YOLOv8 processes image features in a single forward pass, providing high speed and accuracy suited for cloud GPU acceleration (T4 GPU).
---
####  Cyberpunk Visual HUD
To enhance visual legibility and evaluation presentation, OpenCV routines generate:
* **Neon Bounding Boxes:** Electric cyan and magenta bounding boxes with transmissive alpha fills.
* **Target Corner Crosshairs:** High-precision corner notches on all detected objects.
* **Status Badge Banner:** Dark glass top banner showing `EXPECTED` vs. `ACTUAL AI DETECTED` metrics along with dynamic status flags (`[MATCHED]` or `[DEVIATION]`).
---
#### OUTPUT
---

## 📸 Vision Processing Results

---

### 📸 Vision Processing Results

<div align="center">

| 1. Original Input Image | 2. Cyberpunk HUD Detection Output |
| :---: | :---: |
| <a href="https://drive.google.com/file/d/1bbq423wlg8D3OAdZNaBq_LJkjPcGeS4s/view?usp=sharing" target="_blank"><img src="https://drive.google.com/thumbnail?id=1bbq423wlg8D3OAdZNaBq_LJkjPcGeS4s&sz=w1000" width="400" alt="Original Input Image"/></a> | <a href="https://drive.google.com/file/d/1BIXNAjxvu_shhK4tnoNX-A6Juvo5Ifg4/view?usp=sharing" target="_blank"><img src="https://drive.google.com/thumbnail?id=1BIXNAjxvu_shhK4tnoNX-A6Juvo5Ifg4&sz=w1000" width="400" alt="HUD Processed Image"/></a> |

</div>


---
####  Automated Data Logging
Output data is written directly to `outputs/vehicle_counts.csv`. The output schema records:
* `Expected_Count`: Target integer entered in Cell 3.
* `Actual_Detected_Count`: Total bounding box instances isolated by YOLOv8.
* `Status`: Verification flag (`MATCHED` if expected equals actual, otherwise `DEVIATION`).
* `Category`: Object class tag (e.g., `car`, `bus`, `person`).
* `Count`: Total items detected per individual category.
* `Timestamp`: Execution timestamp.


---

### Author

**Made by Shalini Anand**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AND-SHAL-0813)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shalini-anand0813)
