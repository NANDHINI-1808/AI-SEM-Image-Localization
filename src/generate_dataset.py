import cv2
import numpy as np
import random
import os


# Create dataset folder
os.makedirs("dataset", exist_ok=True)


# Create base image
img = np.zeros((1200, 1600), dtype=np.uint8)


# Draw random SEM-like patterns
for i in range(50):
    x1 = random.randint(0, 1500)
    y1 = random.randint(0, 1100)

    x2 = random.randint(0, 1500)
    y2 = random.randint(0, 1100)

    cv2.line(
        img,
        (x1, y1),
        (x2, y2),
        random.randint(100,255),
        2
    )


# Create reference crop

ref_x = random.randint(200,900)
ref_y = random.randint(200,700)

reference = img[
    ref_y:ref_y+200,
    ref_x:ref_x+200
]


# Create search image

search = img.copy()


# Add noise (SEM effect)

noise = np.random.normal(
    0,
    10,
    search.shape
).astype(np.int16)


search = np.clip(
    search.astype(np.int16)+noise,
    0,
    255
).astype(np.uint8)



# -------- Reference Enhancement --------

reference = cv2.GaussianBlur(
    reference,
    (3,3),
    0
)


reference = cv2.Canny(
    reference,
    50,
    150
)


# Resize back for saving
reference = cv2.resize(
    reference,
    (200,200)
)


# -------- Save images --------

cv2.imwrite(
    "dataset/search_image.png",
    search
)


cv2.imwrite(
    "dataset/reference_image.png",
    reference
)


# Save ground truth

center_x = ref_x + 100
center_y = ref_y + 100


with open(
    "dataset/ground_truth.txt",
    "w"
) as f:

    f.write(
        f"{center_x} {center_y}"
    )


print("Dataset Generated Successfully!")
print(
    "Ground Truth:",
    center_x,
    center_y
)