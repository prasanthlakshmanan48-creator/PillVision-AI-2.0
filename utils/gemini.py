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

Return your answer in Markdown with these headings:

## 🚦 Risk Level
(Low / Moderate / High)

## 📖 Interaction Summary

## ⚠️ Possible Side Effects

## 💊 Recommendation

## 🚑 When to Consult a Doctor

If there is no known interaction, clearly state that.

If you are uncertain, say you are uncertain instead of guessing.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text

    prompt = f"""
You are a licensed pharmacist.

Provide accurate information about this medicine:

{name}

Return the answer in Markdown using these headings:

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
