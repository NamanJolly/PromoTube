from transformers import pipeline
import os
import streamlit as st

os.environ["TRANSFORMERS_CACHE"] = "./hf_cache"  # local folder in your project

@st.cache_resource
def load_classifier():
    return pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
classifier = load_classifier()

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
