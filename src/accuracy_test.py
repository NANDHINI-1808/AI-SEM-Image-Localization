import subprocess
import os
import numpy as np


errors = []

total_tests = 20


print("----------------------")
print("HYBRID LOCALIZATION ACCURACY TEST")
print("----------------------")


for i in range(total_tests):

    print("\nTest:", i+1)

    # Generate new dataset
    subprocess.run(
        ["python", "src/generate_dataset.py"],
        stdout=subprocess.DEVNULL
    )


    # Read Ground Truth
    with open("dataset/ground_truth.txt", "r") as file:
        data = file.read().split()

    gt_x = int(data[0])
    gt_y = int(data[1])


    # Run hybrid localization
    result = subprocess.run(
        ["python", "src/hybrid_localization.py"],
        capture_output=True,
        text=True
    )


    output = result.stdout


    prediction = None


    for line in output.split("\n"):

        if "Final Prediction:" in line:
            index = output.split("\n").index(line)

            values = output.split("\n")[index+1].split()

            if len(values)==2:
                prediction = values


    if prediction:

        pred_x = int(prediction[0])
        pred_y = int(prediction[1])


        error = np.sqrt(
            (gt_x-pred_x)**2 +
            (gt_y-pred_y)**2
        )


        errors.append(error)


        print(
            "Ground Truth:",
            gt_x,
            gt_y
        )

        print(
            "Prediction:",
            pred_x,
            pred_y
        )

        print(
            "Error:",
            round(error,2),
            "pixels"
        )

    else:

        print("Prediction failed")


print("\n====================")

print(
    "Successful Tests:",
    len(errors),
    "/",
    total_tests
)


if len(errors)>0:

    avg_error = sum(errors)/len(errors)

    accuracy = (
        len([e for e in errors if e < 10])
        /
        len(errors)
    )*100


    print(
        "Average Error:",
        round(avg_error,2),
        "pixels"
    )

    print(
        "Accuracy (<10 pixel error):",
        round(accuracy,2),
        "%"
    )


print("====================")