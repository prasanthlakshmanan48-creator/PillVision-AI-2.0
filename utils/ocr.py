import easyocr
import numpy as np
import cv2

# Load OCR model only once
reader = easyocr.Reader(["en"], gpu=False)

def preprocess_image(image):

    img = np.array(image)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (3,3), 0)

    gray = cv2.equalizeHist(gray)

    _, thresh = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return thresh


def extract_text(image):

    processed = preprocess_image(image)

    result = reader.readtext(
        processed,
        detail=0,
        paragraph=True
    )

    text = " ".join(result)

    if text.strip()=="":
        text="No readable text detected."

    return text
