from transformers import pipeline
import os


os.environ["TRANSFORMERS_CACHE"] = "./hf_cache"  # local folder in your project

# Faster model than BART-large-MNLI
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

CATEGORIES = [
    "Amazon affiliate link",
    "Walmart link",
    "Coupon website",
    "YouTube redirect",
    "Personal blog or shop",
    "Random link"
]

def classify_text(text):
    result = classifier(text, CATEGORIES)
    return result["labels"][0]  # Top prediction
