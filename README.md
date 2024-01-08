# EasyOCR

# OCR with EasyOCR

This Python script performs Optical Character Recognition (OCR) on an image using the EasyOCR library. It detects text regions, draws bounding boxes around them, and displays the results.

## Requirements

Make sure you have the following dependencies installed:

- OpenCV (`opencv-python`)
- Matplotlib (`matplotlib`)
- EasyOCR (`easyocr`)
- PyTorch (`torch`)

Install the dependencies using:

```bash
pip install -r requirements.txt

## Usage

 - Place the image you want to analyze in the same directory as the script.
 - Run the script:

```bash
 python ocr_script.py
 
 - The script will display the image with bounding boxes around detected text regions.

## Explanation
 - The script uses OpenCV to load the image, EasyOCR for text recognition, and Matplotlib for visualizing the results. Detected text regions are highlighted with blue rectangles.
 - Feel free to modify the script to suit your specific OCR requirements.

## Acknowledgments
 - EasyOCR - A comprehensive OCR library for Python.