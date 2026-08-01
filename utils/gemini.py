from config import client, MODEL_NAME
from utils.ocr import extract_text

# ==========================================
# Scan Medicine Image
# ==========================================

def analyze_medicine_image(image):

    # Extract text using OCR
    ocr_text = extract_text(image)

    prompt = f"""
You are an expert pharmacist.

OCR Text:
{ocr_text}

Analyze BOTH the uploaded medicine image and the OCR text.

Return ONLY valid JSON.

The JSON format must be EXACTLY like this:

{{
    "medicine_name": "",
    "active_ingredient": "",
    "manufacturer": "",
    "strength": "",
    "uses": "",
    "dosage": "",
    "side_effects": "",
    "drug_interactions": "",
    "pregnancy": "",
    "storage": "",
    "summary": ""
}}

Rules:
- Return ONLY JSON.
- Do NOT use Markdown.
- Do NOT use code blocks.
- If you are not confident, write "Unknown".
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, image]
    )

    return response.text


# ==========================================
# Medicine Search
# ==========================================

def search_medicine(name):

    prompt = f"""
You are a licensed pharmacist.

Provide detailed information about:

{name}

Return in Markdown with:

## 💊 Medicine Name

## 🧪 Generic Name

## 🩺 Uses

## 💉 Typical Dosage

## ⚠️ Common Side Effects

## 🚫 Warnings

## 🔄 Drug Interactions

## 🍺 Alcohol Interaction

## 🤰 Pregnancy

## 🤱 Breastfeeding

## 📦 Storage

## 📝 Summary
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


# ==========================================
# Drug Interaction Checker
# ==========================================

def drug_interaction(medicine1, medicine2):

    prompt = f"""
You are an experienced clinical pharmacist.

Check the interaction between:

Medicine 1:
{medicine1}

Medicine 2:
{medicine2}

Return in Markdown:

## 🚦 Risk Level

## 📖 Interaction Summary

## ⚠️ Possible Side Effects

## 💊 Recommendation

## 🚑 When to Consult a Doctor
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


# ==========================================
# AI Health Chat
# ==========================================

def health_chat(question):

    prompt = f"""
You are PillVision AI.

You are a friendly healthcare assistant.

Answer ONLY healthcare and medicine-related questions.

Question:
{question}

Return your answer in Markdown with these headings:

## 💡 Answer

## 📖 Explanation

## ⚠️ Important Advice

## 👨‍⚕️ When to Consult a Doctor

If the question is not related to healthcare or medicines, politely explain that you can only answer healthcare-related questions.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text
