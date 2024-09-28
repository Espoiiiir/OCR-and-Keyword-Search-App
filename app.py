import os
from PIL import Image, ImageEnhance, ImageFilter
import streamlit as st
from pytesseract import image_to_string

def preprocess_image(image):
    # Convert image to grayscale
    image = image.convert('L')
    # Enhance the image
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    # Apply a filter to remove noise
    image = image.filter(ImageFilter.MedianFilter())
    return image

def main():
    st.title("OCR and Keyword Search App")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        extracted_text = pytesseract.image_to_string(uploaded_file).strip()  # Using ocr_image function

        st.write("Extracted Text (OCR):")
        st.write(extracted_text)

        keyword = st.text_input("Enter keyword to search").strip()

        if keyword:
            if keyword in extracted_text:
                st.markdown(f"**Keyword found in OCR output:** {keyword}")
                highlighted_text = extracted_text.replace(keyword, f"**{keyword}**")
                st.write(highlighted_text)
            else:
                st.write(f"Keyword '{keyword}' not found in OCR output")

if __name__ == "__main__":
    main()
