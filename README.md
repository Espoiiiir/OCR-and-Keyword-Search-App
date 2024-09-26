# OCR-and-Keyword-Search-App
This is a Streamlit application that performs Optical Character Recognition (OCR) on uploaded images and allows users to search for keywords within the extracted text.

## Features

- Upload an image (JPG, JPEG, PNG)
- Perform OCR to extract text from the image
- Search for keywords within the extracted text
- Highlight found keywords

## Installation
1. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Ensure Tesseract is installed**:
    - Download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract).
    - Ensure the `tesseract.exe` path is correctly set in the code.

## Usage

1. **Run the Streamlit app**:
    ```sh
    streamlit run app.py
    ```

2. **Upload an image**:
    - Use the file uploader to upload an image (JPG, JPEG, PNG).

3. **Extract and search text**:
    - The app will display the extracted text.
    - Enter a keyword to search within the extracted text.

## Troubleshooting

- Ensure the `hin.traineddata` and `eng.traineddata` files are correctly placed in the `tessdata` directory of your Tesseract installation.
- Use the `--oem 1` option to disable the Cube model and use the LSTM OCR Engine Mode.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
