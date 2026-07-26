import cv2
import numpy as np


# ==========================
# Load Images
# ==========================

reference = cv2.imread(
    "dataset/reference_image.png",
    0
)

search = cv2.imread(
    "dataset/search_image.png",
    0
)


if reference is None or search is None:
    print("Images not found!")
    exit()


print("Images loaded successfully!")


# ==========================
# ORB Feature Detection
# ==========================

orb = cv2.ORB_create(
    nfeatures=5000
)


kp1, des1 = orb.detectAndCompute(
    reference,
    None
)


kp2, des2 = orb.detectAndCompute(
    search,
    None
)


if des1 is None or des2 is None:
    print("No features detected!")
    exit()


print("Reference points:", len(kp1))
print("Search points:", len(kp2))


# ==========================
# Feature Matching
# ==========================

bf = cv2.BFMatcher(
    cv2.NORM_HAMMING
)


matches = bf.knnMatch(
    des1,
    des2,
    k=2
)


good_matches = []


for m, n in matches:

    if m.distance < 0.85 * n.distance:
        good_matches.append(m)


print("Good matches:", len(good_matches))


if len(good_matches) < 6:
    print("Not enough matches")
    exit()



# ==========================
# Homography Calculation
# ==========================

src_pts = np.float32(
    [
        kp1[m.queryIdx].pt
        for m in good_matches
    ]
).reshape(-1,1,2)



dst_pts = np.float32(
    [
        kp2[m.trainIdx].pt
        for m in good_matches
    ]
).reshape(-1,1,2)



H, mask = cv2.findHomography(
    src_pts,
    dst_pts,
    cv2.RANSAC,
    5.0
)



if H is None:
    print("Homography failed")
    exit()



inliers = np.sum(mask)

print("RANSAC Inliers:", inliers)



# ==========================
# ORB Rough Location
# ==========================

h, w = reference.shape


reference_center = np.float32(
    [
        [
            [w/2, h/2]
        ]
    ]
)


rough_center = cv2.perspectiveTransform(
    reference_center,
    H
)


rough_x = int(
    rough_center[0][0][0]
)

rough_y = int(
    rough_center[0][0][1]
)


print("--------------------")
print("ORB Rough Center:")
print(rough_x, rough_y)
print("--------------------")



# ==========================
# Template Matching Refinement
# ==========================

result = cv2.matchTemplate(
    search,
    reference,
    cv2.TM_CCOEFF_NORMED
)


min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(
    result
)


final_x = max_loc[0] + w//2
final_y = max_loc[1] + h//2



print("--------------------")
print("Final Prediction:")
print(final_x, final_y)
print("--------------------")

print(
    "Matching Score:",
    max_val
)



# ==========================
# Visualization
# ==========================


output = cv2.cvtColor(
    search,
    cv2.COLOR_GRAY2BGR
)



# Draw center point

cv2.circle(
    output,
    (final_x, final_y),
    10,
    (0,0,255),
    -1
)



# Draw bounding box

cv2.rectangle(
    output,
    (
        final_x-50,
        final_y-50
    ),
    (
        final_x+50,
        final_y+50
    ),
    (0,255,0),
    3
)



# Coordinate text

coordinate_text = (
    f"X:{final_x} Y:{final_y}"
)


cv2.putText(
    output,
    coordinate_text,
    (
        final_x-100,
        final_y-70
    ),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255,255,255),
    2
)



# Score text

score_text = (
    f"Score:{max_val:.2f}"
)


cv2.putText(
    output,
    score_text,
    (50,50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255,255,255),
    2
)



# Save result

cv2.imwrite(
    "dataset/hybrid_result.png",
    output
)


print("--------------------")
print("Saved:")
print("dataset/hybrid_result.png")
print("--------------------")