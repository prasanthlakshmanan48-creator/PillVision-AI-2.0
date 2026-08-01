from config import client, MODEL_NAME
from utils.ocr import extract_text

# ==========================================
# Scan Medicine Image
# ==========================================

def analyze_medicine_image(image):

    try:

        ocr_text = extract_text(image)

        prompt = f"""
You are an expert pharmacist.

OCR detected text:

{ocr_text}

Analyze BOTH the uploaded medicine image and the OCR text.

Identify the medicine.

Return ONLY valid JSON.

JSON format:

{{
  "medicine_name":"",
  "active_ingredient":"",
  "manufacturer":"",
  "strength":"",
  "uses":"",
  "dosage":"",
  "side_effects":"",
  "drug_interactions":"",
  "pregnancy":"",
  "alcohol_interaction":"",
  "storage":"",
  "summary":""
}}

Rules:

- Return ONLY JSON.
- No Markdown.
- No explanation.
- If unknown, write "Unknown".
"""

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[prompt, image]
        )

        return response.text

    except Exception as e:

        return f"""
{{
"medicine_name":"Error",
"active_ingredient":"Unknown",
"manufacturer":"Unknown",
"strength":"Unknown",
"uses":"Unknown",
"dosage":"Unknown",
"side_effects":"Unknown",
"drug_interactions":"Unknown",
"pregnancy":"Unknown",
"alcohol_interaction":"Unknown",
"storage":"Unknown",
"summary":"{str(e)}"
}}
"""


# ==========================================
# Medicine Search
# ==========================================

def search_medicine(name):

    prompt = f"""
You are an expert pharmacist.

Medicine:

{name}

Provide accurate information.

Return in Markdown.

## 💊 Medicine Name

## 🧪 Generic Name

## 🏭 Manufacturer

## 🩺 Uses

## 💉 Dosage

## ⚠️ Side Effects

## 🚫 Warnings

## 🔄 Drug Interactions

## 🍺 Alcohol Interaction

## 🤰 Pregnancy

## 🤱 Breastfeeding

## 📦 Storage

## 💰 Approximate Price

## 📝 Summary
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


# ==========================================
# Drug Interaction
# ==========================================

def drug_interaction(medicine1, medicine2):

    prompt = f"""
You are a clinical pharmacist.

Medicine 1:
{medicine1}

Medicine 2:
{medicine2}

Return in Markdown.

## 🚦 Risk Level

(Low / Moderate / High)

## 📖 Interaction

## ⚠️ Possible Effects

## 💊 Recommendation

## 🚑 When to Consult Doctor
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

Answer ONLY medicine and healthcare questions.

Question:

{question}

Return in Markdown.

## 💡 Answer

## 📖 Explanation

## ⚠️ Important Advice

## 👨‍⚕️ When to See a Doctor

If the question is unrelated to healthcare,
politely refuse.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text
