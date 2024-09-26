import os
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import streamlit as st

# Set the Tesseract command path based on the environment
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def preprocess_image(image):
    # Convert image to grayscale
    image = image.convert('L')
    # Enhance the image
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    # Apply a filter to remove noise
    image = image.filter(ImageFilter.MedianFilter())
    return image


def ocr_image(image_path):
    img = Image.open(image_path)  
    text = pytesseract.image_to_string(img, lang='eng+hin')  
    return text

def main():
    st.title("OCR and Keyword Search App")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        extracted_text = ocr_image(image).strip()

        st.write("Extracted Text:")
        st.write(extracted_text)

        keyword = st.text_input("Enter keyword to search").strip()

        if keyword:
            if keyword in extracted_text:
                st.markdown(f"**Keyword found:** {keyword}")
                highlighted_text = extracted_text.replace(keyword, f"**{keyword}**")
                st.write(highlighted_text)
            else:
                st.write(f"Keyword '{keyword}' not found")

if __name__ == "__main__":
    main()
