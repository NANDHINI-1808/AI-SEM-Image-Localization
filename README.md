# AI-Powered Navigation-Error Recovery for Wafer Inspection using SEM Image Localization

## Overview

Semiconductor wafer inspection requires extremely precise positioning to ensure that inspection tools return to the exact same location repeatedly.

In real-world semiconductor manufacturing environments, small navigation errors occur due to thermal expansion, vibration, and mechanical stage drift. These errors accumulate over time and may cause the inspection tool to land several pixels away from the intended position.

This project presents an AI-powered SEM image localization system that recovers the correct inspection position by locating where a reference SEM image pattern appears inside a larger search image.

The system identifies the matching region, predicts the center coordinates `(x, y)`, and evaluates localization accuracy using multiple test cases.

---

# Problem Statement

Modern wafer inspection tools need nanometer-level positioning accuracy. However, repeated movements introduce small errors due to:

- Thermal expansion
- Mechanical drift
- Vibration from the environment
- Stage positioning errors

Because semiconductor layouts contain highly repetitive structures, the incorrect location may look very similar to the correct location.

Traditional template matching methods face challenges such as:

- Highly periodic wafer patterns
- Similar repeated structures
- Scale differences between images
- Sensor noise variations

The objective of this project is to develop an intelligent localization system that can:

- Find the reference SEM pattern inside the search image
- Recover the correct inspection position after navigation errors
- Predict the center coordinates of the matching region
- Achieve accurate and reliable localization

---

# Proposed Solution

The proposed system uses computer vision-based localization techniques to recover the correct wafer inspection position.

The complete pipeline includes:

- Synthetic SEM dataset generation
- Image preprocessing
- ORB feature extraction
- Feature matching
- RANSAC filtering
- Location estimation
- Accuracy evaluation

---

# Workflow

```
                Input SEM Images

          Reference Image + Search Image
                         |
                         v

              Image Preprocessing
                         |
                         v

             Feature Extraction
              (ORB Algorithm)
                         |
                         v

              Feature Matching
                         |
                         v

              RANSAC Filtering
        (Remove Incorrect Matches)
                         |
                         v

            Localization Estimation
                         |
                         v

          Center Coordinate Prediction
                    (X, Y)
                         |
                         v

             Accuracy Evaluation
                         |
                         v

                Final Result
       Recovered Inspection Position
```

---

# Methodology

## 1. Synthetic Dataset Generation

Due to confidentiality restrictions, real semiconductor wafer images are not publicly available.

Therefore, a synthetic SEM dataset is generated to simulate realistic inspection conditions.

The generated dataset contains:

- Reference images
- Search images
- Different target positions
- Ground truth coordinates

The generated images simulate wafer-like repetitive patterns for testing the localization algorithm.

---

## 2. Image Feature Extraction

ORB (Oriented FAST and Rotated BRIEF) algorithm is used to extract important features from SEM images.

The extracted features include:

- Key points
- Feature descriptors
- Local image patterns

These features help identify the similarity between reference and search images.

---

## 3. Feature Matching

The extracted features from the reference image are compared with features from the search image.

The system finds possible matching regions based on feature similarity.

---

## 4. RANSAC Filtering

RANSAC (Random Sample Consensus) algorithm is applied to improve matching accuracy.

It helps to:

- Remove incorrect feature matches
- Reduce false detections
- Select reliable matching points

---

## 5. Localization Prediction

After filtering the correct matches, the system estimates the location of the reference pattern inside the search image.

The final output is the center coordinate of the detected region.

Example:

```
Final Prediction:

X = 722
Y = 452
```

---

## 6. Accuracy Evaluation

The predicted coordinates are compared with the ground truth coordinates.

The system calculates:

- Pixel error
- Average localization error
- Accuracy percentage

This helps measure the performance of the localization system.

---

# System Architecture

```
                 SEM Images

        Reference Image     Search Image

                  |
                  v

          Feature Extraction

                  |
                  v

            ORB Matching

                  |
                  v

           RANSAC Filtering

                  |
                  v

        Matching Region Detection

                  |
                  v

        Coordinate Prediction

                  |
                  v

          Accuracy Evaluation

                  |
                  v

              Final Output
```

---

# Technologies Used

## Programming Language

- Python

## Libraries

- OpenCV
- NumPy
- Matplotlib
- PyTorch

## Computer Vision Techniques

- ORB Feature Detection
- Feature Matching
- RANSAC Algorithm
- Image Localization

---

# Project Structure

```
AI-SEM-Image-Localization
│
├── dataset
│   ├── reference_image.png
│   ├── search_image.png
│   ├── ground_truth.txt
│   ├── hybrid_result.png
│   ├── localization_result.png
│   └── match_result.png
│
├── src
│   ├── generate_dataset.py
│   ├── orb_match.py
│   ├── find_match.py
│   ├── localization.py
│   ├── hybrid_localization.py
│   ├── accuracy_test.py
│   └── train_model.py
│
├── assets
│   ├── accuracy.png
│   ├── hybrid_result.png
│   └── result.png
│
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/NANDHINI-1808/AI-SEM-Image-Localization.git
```

Navigate into the project folder:

```bash
cd AI-SEM-Image-Localization
```

Install required libraries:

```bash
pip install opencv-python numpy matplotlib torch torchvision
```

---

# Execution

## Generate Dataset

```bash
python src/generate_dataset.py
```

This generates:

- Reference SEM image
- Search SEM image
- Ground truth coordinates

---

## Run Localization Algorithm

```bash
python src/hybrid_localization.py
```

The system performs:

- Image loading
- Feature extraction
- Feature matching
- RANSAC filtering
- Coordinate prediction

Example output:

```
Images loaded successfully!

Reference points: 499
Search points: 5000

Good matches: 28
RANSAC Inliers: 9

Final Prediction:

722 452

Matching Score:
0.382
```

---

## Run Accuracy Test

```bash
python src/accuracy_test.py
```

The system evaluates multiple test samples by comparing predicted coordinates with actual ground truth coordinates.

---

# Results

The system was tested using multiple synthetic SEM image samples.

Performance:

```
Successful Tests: 18 / 20

Average Error: 2.16 pixels

Accuracy (<10 pixel error): 100%
```

The results show that the proposed AI-based localization approach can accurately recover the inspection position with very low localization error.

---

# Output Visualization

The system generates:

- Feature matching results
- Localization result images
- Accuracy evaluation reports

Example outputs:

- Hybrid localization result
- Accuracy graph
- Final prediction visualization

---

# Applications

This project can be applied in:

- Semiconductor wafer inspection
- Navigation error recovery systems
- Automated defect inspection
- Industrial computer vision
- Microscopy image analysis
- Precision manufacturing

---

# Future Improvements

Future enhancements include:

- Deep learning-based feature extraction
- CNN/Transformer-based image matching
- Real wafer SEM dataset integration
- Sub-pixel localization accuracy improvement
- Real-time inspection tool deployment

---

# Conclusion

This project demonstrates an AI-powered solution for wafer inspection navigation-error recovery using SEM image localization.

By combining feature extraction, feature matching, RANSAC filtering, and coordinate prediction, the system can identify the correct inspection location even in challenging repetitive semiconductor patterns.

The achieved low localization error demonstrates that the proposed approach provides accurate and reliable position recovery for wafer inspection applications.

---

# Author

**Nandhini M**

AI-SEM Image Localization Project
