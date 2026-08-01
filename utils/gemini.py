from config import client, MODEL_NAME

# ==========================================
# Scan Medicine Image
# ==========================================

def analyze_medicine_image(image):

    prompt = """
You are an expert pharmacist.

Analyze the uploaded medicine image.

Return the answer in Markdown using these headings:

## 💊 Medicine Name
## 🧪 Active Ingredient
## 🏥 Manufacturer
## 💉 Strength
## 🩺 Uses
## 💊 Typical Dosage
## ⚠️ Common Side Effects
## 🔄 Drug Interactions
## 🤰 Pregnancy Safety
## 🍺 Alcohol Interaction
## 📦 Storage
## 📝 Summary

If you cannot confidently identify the medicine, clearly say so.
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

Medicine 1: {medicine1}

Medicine 2: {medicine2}

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
