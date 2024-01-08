import cv2
import matplotlib.pyplot as plt
import easyocr

# Load the image using OpenCV
image = cv2.imread('balance.jpeg')

# Initialize the EasyOCR Reader with English language support and GPU acceleration
read = easyocr.Reader(lang_list=['en'], gpu=True)

# Perform OCR on the image
result = read.readtext(image)

# Process the OCR results
for res in result:
    # Unpack the result tuple into bounding box, text, and score
    bbox, text, score = res

    # Draw a rectangle around the detected text on the image
    cv2.rectangle(image, bbox[0], bbox[2], (255, 0, 0), 5)
    print(bbox)

# Display the image with detected text
plt.imshow(image)
plt.show()
