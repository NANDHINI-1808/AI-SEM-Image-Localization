# AI-SEM Image Localization

## 🚀 Project Overview

AI-SEM Image Localization is an AI-based image matching and localization system that predicts the position of a search image inside a reference image.

The project combines computer vision techniques with AI-based feature analysis to achieve accurate image localization. It is designed for navigation recovery and image-based position estimation problems.

---

## 🎯 Problem Statement

Given:

* A reference image
* A search image captured from an unknown location

The system identifies where the search image belongs inside the reference image and predicts the exact center coordinates.

---

## 💡 Proposed Solution

The system uses a hybrid localization approach:

1. Feature Detection using ORB (Oriented FAST and Rotated BRIEF)
2. Feature Matching using descriptor comparison
3. Good Match Filtering using Lowe's Ratio Test
4. RANSAC-based Outlier Removal
5. AI-assisted Feature Processing
6. Coordinate Prediction

The final model combines traditional computer vision and AI techniques for robust localization.

---

## 🏗️ System Workflow

```
Input Images
     |
     ↓
Feature Extraction (ORB)
     |
     ↓
Feature Matching
     |
     ↓
Good Match Filtering
     |
     ↓
RANSAC Verification
     |
     ↓
Hybrid Localization
     |
     ↓
Predicted Position Coordinates
```

---

## 🧠 Technologies Used

### Programming Language

* Python

### Computer Vision

* OpenCV
* ORB Feature Detector
* BFMatcher
* RANSAC Algorithm

### AI / Deep Learning

* PyTorch
* Torchvision

### Data Processing

* NumPy
* Matplotlib

### Development Tools

* VS Code
* Google Colab
* GitHub

---

## 📂 Project Structure

```
AI-SEM-Image-Localization

│
├── dataset/
│   ├── reference_image.png
│   ├── search_image.png
│   ├── ground_truth.txt
│   └── result images
│
├── src/
│   ├── generate_dataset.py
│   ├── orb_match.py
│   ├── localization.py
│   ├── hybrid_localization.py
│   ├── accuracy_test.py
│   ├── ai_feature.py
│   └── train_model.py
│
├── README.md
└── .gitignore
```

---

## 📊 Performance Results

### Hybrid Localization Accuracy Test

| Metric                     | Result     |
| -------------------------- | ---------- |
| Successful Tests           | 19 / 20    |
| Average Error              | 2.2 Pixels |
| Accuracy (<10 Pixel Error) | 100%       |

The system achieved high localization accuracy with low prediction error.

---

## 🖥️ How to Run

### 1. Clone Repository

```bash
git clone https://github.com/NANDHINI-1808/AI-SEM-Image-Localization.git
```

### 2. Install Dependencies

```bash
pip install opencv-python numpy matplotlib torch torchvision
```

### 3. Generate Dataset

```bash
python src/generate_dataset.py
```

### 4. Run Hybrid Localization

```bash
python src/hybrid_localization.py
```

### 5. Test Accuracy

```bash
python src/accuracy_test.py
```

---

## 📌 Output

The system generates:

* Predicted coordinates
* Matching score
* Localization result image
* Accuracy evaluation report

Example:

```
Final Prediction:
601 504

Matching Score:
0.404

Accuracy:
100%
```

---

## 🌟 Applications

* Autonomous navigation systems
* Satellite image localization
* Medical image alignment
* Industrial inspection
* Robot navigation
* Recovery of lost image positions

---

## 🔮 Future Improvements

* Add deep learning-based feature extraction
* Real-time camera localization
* Deploy as a web application
* Add GPS and sensor integration
* Improve robustness for different image conditions

---

## 👩‍💻 Author

**Nandhini**

AI-SEM Image Localization Project
