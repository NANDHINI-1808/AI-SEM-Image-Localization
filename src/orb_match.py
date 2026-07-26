import cv2
import numpy as np


# Load images

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


# ORB detector

orb = cv2.ORB_create(
    nfeatures=5000,
    scaleFactor=1.2,
    nlevels=8
)


# Detect features

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
    print("No features detected!")
    exit()



# Feature matching

bf = cv2.BFMatcher(
    cv2.NORM_HAMMING,
    crossCheck=True
)


matches = bf.match(
    des1,
    des2
)


# Sort by quality

matches = sorted(
    matches,
    key=lambda x: x.distance
)


print("Total matches:", len(matches))



# Select good matches

good_matches = matches[:10]


if len(good_matches) < 5:
    print("Not enough good matches!")
    exit()



# Get matched points

src_points = []
dst_points = []


for m in good_matches:

    src_points.append(
        kp1[m.queryIdx].pt
    )

    dst_points.append(
        kp2[m.trainIdx].pt
    )


src_points = np.float32(src_points)
dst_points = np.float32(dst_points)



# RANSAC filtering

if len(src_points) >= 4:

    matrix, mask = cv2.findHomography(
        src_points,
        dst_points,
        cv2.RANSAC,
        5.0
    )


    if mask is not None:

        inliers = []

        for i in range(len(mask)):

            if mask[i]:
                inliers.append(
                    dst_points[i]
                )


        if len(inliers) > 0:

            inliers = np.array(inliers)

            center_x = int(
                np.median(
                    inliers[:,0]
                )
            )

            center_y = int(
                np.median(
                    inliers[:,1]
                )
            )

        else:

            center_x = int(
                np.median(dst_points[:,0])
            )

            center_y = int(
                np.median(dst_points[:,1])
            )


else:

    center_x = int(
        np.median(dst_points[:,0])
    )

    center_y = int(
        np.median(dst_points[:,1])
    )



print("---------------------")
print("ORB Predicted Center:")
print(center_x, center_y)
print("---------------------")



# Draw matches

result = cv2.drawMatches(
    reference,
    kp1,
    search,
    kp2,
    good_matches,
    None,
    flags=2
)



cv2.imwrite(
    "dataset/orb_result.png",
    result
)


print("Saved: dataset/orb_result.png")