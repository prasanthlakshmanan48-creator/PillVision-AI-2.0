import easyocr
import numpy as np
import cv2

# Load OCR model once
reader = easyocr.Reader(
    ['en'],
    gpu=False
)

def preprocess_image(image):
    """
    Improve image quality before OCR.
    """

    # Convert PIL Image to NumPy array
    img = np.array(image)

    # Convert RGB to BGR (OpenCV format)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    # Increase contrast
    gray = cv2.equalizeHist(gray)

    # Binary threshold
    _, thresh = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return thresh


def extract_text(image):
    """
    Extract text from medicine image using OCR.
    """

    processed = preprocess_image(image)

    results = reader.readtext(
        processed,
        detail=0,
        paragraph=True,
        text_threshold=0.4,
        low_text=0.3,
        link_threshold=0.3
    )

    text = " ".join(results)

    if text.strip() == "":
        text = "No readable text detected."

    return text
