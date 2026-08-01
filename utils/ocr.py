import easyocr
import numpy as np

# Load OCR model once
reader = easyocr.Reader(
    ['en'],
    gpu=False
)

def extract_text(image):

    img = np.array(image)

    results = reader.readtext(
        img,
        detail=0,
        paragraph=True
    )

    text = " ".join(results)

    return text
