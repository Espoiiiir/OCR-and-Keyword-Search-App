import os
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import streamlit as st

# Ensure Tesseract is installed and set the path if necessary
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image):
    # Convert image to grayscale
    image = image.convert('L')
    # Enhance the image
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    # Apply a filter to remove noise
    image = image.filter(ImageFilter.MedianFilter())
    return image

def perform_ocr(image):
    try:
        # Preprocess the image
        image = preprocess_image(image)
        # Perform OCR using Tesseract with LSTM OCR Engine Mode
        extracted_text = pytesseract.image_to_string(image, lang='eng+hin')
        return extracted_text
    except pytesseract.TesseractError as e:
        st.error(f"Tesseract OCR error: {e}")
        return ""

def main():
    st.title("OCR and Keyword Search App")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        extracted_text = perform_ocr(image).strip()

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
