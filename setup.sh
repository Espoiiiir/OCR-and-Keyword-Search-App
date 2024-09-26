#!/bin/bash

# Update package list and install Tesseract
sudo apt-get update
sudo apt-get install -y tesseract-ocr

# Install additional language data files if needed
sudo apt-get install -y tesseract-ocr-eng tesseract-ocr-hin
