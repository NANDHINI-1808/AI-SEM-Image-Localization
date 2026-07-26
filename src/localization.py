import cv2
import numpy as np


# =========================
# Load Images
# =========================

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


# =========================
# ORB Detector
# =========================

orb = cv2.ORB_create(
    nfeatures=5000,
    scaleFactor=1.2,
    nlevels=8
)


kp1, des1 = orb.detectAndCompute(
    reference,
    None
)

kp2, des2 = orb.detectAndCompute(
    search,
    None
)


print("Reference points:", len(kp1))
print("Search points:", len(kp2))


if des1 is None or des2 is None:
    print("ORB cannot find features")
    exit()



# =========================
# Feature Matching
# =========================

bf = cv2.BFMatcher(
    cv2.NORM_HAMMING,
    crossCheck=False
)


matches = bf.knnMatch(
    des1,
    des2,
    k=2
)



# Lowe Ratio Test

good = []

for m, n in matches:

    if m.distance < 0.85 * n.distance:
        good.append(m)



print("Good matches:", len(good))


if len(good) < 6:
    print("Not enough matches")
    exit()



# =========================
# Extract Points
# =========================

src_pts = np.float32(
    [
        kp1[m.queryIdx].pt
        for m in good
    ]
).reshape(-1,1,2)


dst_pts = np.float32(
    [
        kp2[m.trainIdx].pt
        for m in good
    ]
).reshape(-1,1,2)



# =========================
# Homography + RANSAC
# =========================

H, mask = cv2.findHomography(
    src_pts,
    dst_pts,
    cv2.RANSAC,
    3.0
)


if H is None:
    print("Homography failed")
    exit()



# Count correct matches

inliers = mask.ravel().tolist().count(1)

print("RANSAC Inliers:", inliers)



# =========================
# Transform Reference Area
# =========================

h, w = reference.shape


corners = np.float32(
    [
        [0,0],
        [w,0],
        [w,h],
        [0,h]
    ]
).reshape(-1,1,2)



new_corners = cv2.perspectiveTransform(
    corners,
    H
)



# =========================
# Calculate Center
# =========================

center = np.mean(
    new_corners,
    axis=0
)


center_x = int(center[0][0])
center_y = int(center[0][1])


print("----------------------")
print("Predicted Center:")
print(center_x, center_y)
print("----------------------")



# =========================
# Draw Result
# =========================

result = cv2.cvtColor(
    search,
    cv2.COLOR_GRAY2BGR
)


# Draw detected box

cv2.polylines(
    result,
    [np.int32(new_corners)],
    True,
    (0,255,0),
    3
)


# Draw center point

cv2.circle(
    result,
    (center_x, center_y),
    8,
    (0,0,255),
    -1
)



# Save

cv2.imwrite(
    "dataset/localization_result.png",
    result
)


print("Saved localization_result.png")