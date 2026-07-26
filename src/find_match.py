import cv2

# Load images
search = cv2.imread("dataset/search_image.png", 0)
reference = cv2.imread("dataset/reference_image.png", 0)

# Check images loaded correctly
if search is None or reference is None:
    print("Error: Images not found!")
    print("Check dataset folder names.")
    exit()

print("Images loaded successfully!")

# Template Matching
result = cv2.matchTemplate(
    search,
    reference,
    cv2.TM_CCOEFF_NORMED
)

# Find best match location
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Reference image size
h, w = reference.shape

# Calculate center point
center_x = max_loc[0] + w // 2
center_y = max_loc[1] + h // 2

# Display results
print("Matching Score:", max_val)
print("Predicted Center:", center_x, center_y)


# Draw rectangle on matched area
search_color = cv2.imread("dataset/search_image.png")

top_left = max_loc
bottom_right = (
    max_loc[0] + w,
    max_loc[1] + h
)

cv2.rectangle(
    search_color,
    top_left,
    bottom_right,
    (0, 255, 0),
    3
)

# Save result image
cv2.imwrite(
    "dataset/match_result.png",
    search_color
)

print("Result saved: dataset/match_result.png")