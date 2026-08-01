from config import client, MODEL_NAME

def analyze_medicine_image(image):
# ==========================================
# Medicine Search
# ==========================================

def search_medicine(name):

    prompt = f"""
You are a licensed pharmacist.

Provide accurate information about this medicine:

{name}

Return the answer in Markdown with these headings:

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

If the medicine cannot be identified confidently, clearly say so.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text

    prompt = """
You are an expert pharmacist.

Analyze the uploaded medicine image.

Return your answer in this format:

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

If you cannot confidently identify the medicine, clearly state that.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, image]
    )

    return response.text
