import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from image_processing import process_image
from text import text_analysis


# Load data
@st.cache
def load_data():
    data = pd.read_csv("WomensClothingE-CommerceReviews.csv")
    return data


data = load_data()

menu_options = ["3D plot", "Image processing", "Text Analysis"]
selected_option = st.sidebar.selectbox("Menu", menu_options)


if selected_option == "3D plot":
    st.write("# 3D Plot")
    fig = px.scatter_3d(
        data, x="Age", y="Rating", z="Positive Feedback Count", opacity=0.7
    )
    st.plotly_chart(fig)

elif selected_option == "Image processing":
    st.write("# Image Processing")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = process_image(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

elif selected_option == "Text Analysis":
    st.write("# Text Analysis")

    text_result = text_analysis(data)
    st.write(text_result)
