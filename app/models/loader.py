
from transformers import pipeline

sentiment_pipeline = None
classify_pipeline = None
summarize_pipeline = None

def load_models():
    global sentiment_pipeline, classify_pipeline, summarize_pipeline

    print(" Loading sentiment model...")
    sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    print("Loading classification model...")
    classify_pipeline = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    print(" Loading summarization model...")
    summarize_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

    print("All models loaded!")