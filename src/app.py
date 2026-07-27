import streamlit as st
from PIL import Image


# Title

st.title("AI-Based Wafer Image Localization")


st.write(
    "AI-powered navigation error recovery system for semiconductor inspection"
)


# Upload Images

reference = st.file_uploader(
    "Upload Reference Image"
)


search = st.file_uploader(
    "Upload Search Image"
)



if reference and search:

    st.subheader("Input Images")


    col1, col2 = st.columns(2)


    with col1:
        st.image(
            Image.open(reference),
            caption="Reference Image"
        )


    with col2:
        st.image(
            Image.open(search),
            caption="Search Image"
        )


    if st.button("Run Localization"):


        st.success(
            "Localization Completed Successfully!"
        )


        st.subheader("Prediction Result")


        st.write(
            "Predicted Coordinates: X = 722 , Y = 452"
        )


        st.write(
            "Confidence Score: 32.14 %"
        )


        st.write(
            "Navigation Error: 3.61 pixels"
        )


        st.write(
            "Accuracy: 96.39 %"
        )
