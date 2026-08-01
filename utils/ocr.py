import easyocr
import numpy as np

# Load OCR model once
reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image):
    """
    Extract text from uploaded PIL image.
    """

    img = np.array(image)

    results = reader.readtext(img)

    text = " ".join([item[1] for item in results])

    return text
