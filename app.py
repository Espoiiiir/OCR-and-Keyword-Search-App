import os
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import streamlit as st

# Set the Tesseract command path based on the environment
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

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
        # Perform OCR using Tesseract
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
        trocr_extracted_text = perform_trocr_ocr(image).strip()

        st.write("Extracted Text (Tesseract):")
        st.write(extracted_text)

        st.write("Extracted Text (TrOCR):")
        st.write(trocr_extracted_text)

        keyword = st.text_input("Enter keyword to search").strip()

        if keyword:
            if keyword in extracted_text:
                st.markdown(f"**Keyword found in Tesseract output:** {keyword}")
                highlighted_text = extracted_text.replace(keyword, f"**{keyword}**")
                st.write(highlighted_text)
            else:
                st.write(f"Keyword '{keyword}' not found in Tesseract output")

            if keyword in trocr_extracted_text:
                st.markdown(f"**Keyword found in TrOCR output:** {keyword}")
                highlighted_text = trocr_extracted_text.replace(keyword, f"**{keyword}**")
                st.write(highlighted_text)
            else:
                st.write(f"Keyword '{keyword}' not found in TrOCR output")

if __name__ == "__main__":
    main()


