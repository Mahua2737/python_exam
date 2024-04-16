from PIL import Image
import io
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from image_processing import process_image
from text import text_analysis


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

    images = {
        "Image 1": "image1.jpg",
        "Image 2": "image2.jpg",
        "Image 3": "image3.jpg",
        "Image 4": "image4.jpg",
    }

    selected_image = st.selectbox("Choose an image...", list(images.keys()))

    image_path = images[selected_image]
    image = Image.open(image_path)
    processed_image = process_image(image)
    st.image(processed_image, caption="Uploaded Image", use_column_width=True)

elif selected_option == "Text Analysis":
    st.write("# Text Analysis")

    text_result = text_analysis(data)
    st.write(text_result)
