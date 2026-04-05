# app/routes/sentiment.py
from fastapi import APIRouter, HTTPException
from app.schemas.request import TextInput, SentimentOutput
from app.models import loader

router = APIRouter()

@router.post("/sentiment", response_model=SentimentOutput)
def analyze_sentiment(body: TextInput):
    if not body.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    result = loader.sentiment_pipeline(body.text)[0]
    return SentimentOutput(label=result["label"], score=round(result["score"], 4))