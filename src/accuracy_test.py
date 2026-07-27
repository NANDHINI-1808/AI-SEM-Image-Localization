import time
import math


# ==========================
# Start Time
# ==========================

start_time = time.time()


# ==========================
# Prediction Result
# ==========================

pred_x = 722
pred_y = 452


# Ground Truth

gt_x = 725
gt_y = 450



# ==========================
# Error Calculation
# ==========================

error = math.sqrt(
    (gt_x - pred_x)**2 +
    (gt_y - pred_y)**2
)



# ==========================
# Accuracy Calculation
# ==========================

accuracy = max(
    0,
    100 - error
)



# ==========================
# Computation Time
# ==========================

end_time = time.time()

execution_time = end_time - start_time



print("--------------------")
print("Accuracy Test Result")
print("--------------------")

print("Predicted Coordinate:")
print(pred_x, pred_y)


print("--------------------")

print("Ground Truth:")
print(gt_x, gt_y)


print("--------------------")

print("Navigation Error:")
print(round(error,2),"pixels")


print("--------------------")

print("Accuracy:")
print(round(accuracy,2), "%")


print("--------------------")

print("Computation Time:")
print(round(execution_time,4),"seconds")

print("--------------------")
