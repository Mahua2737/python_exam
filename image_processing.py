from PIL import Image
import io
import streamlit as st


def process_image(image):
    st.write("Original Image:")
    st.image(image, caption="Original Image", use_column_width=True)

    techniques = ["Resize", "Grayscale", "Crop", "Rotation"]
    selected_techniques = st.multiselect("Select techniques to apply:", techniques)

    for technique in selected_techniques:
        if technique == "Resize":
            width = st.slider("Width", 1, 1000, 300)
            height = st.slider("Height", 1, 1000, 300)
            image = image.resize((width, height))

        elif technique == "Grayscale":
            image = image.convert("L")

        elif technique == "Crop":
            left, top, right, bottom = st.slider(
                "Select area to crop", 0, image.width, (0, 0, image.width, image.height)
            )
            image = image.crop((left, top, right, bottom))

        elif technique == "Rotation":
            angle = st.slider("Angle", -180, 180, 0)
            image = image.rotate(angle)

        st.write(f"Applied {technique}:")

    return image
