from config import client, MODEL_NAME

def analyze_medicine_image(image):

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
