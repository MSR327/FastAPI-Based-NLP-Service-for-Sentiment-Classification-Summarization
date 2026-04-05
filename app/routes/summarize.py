# app/routes/summarize.py
from fastapi import APIRouter, HTTPException
from app.schemas.request import TextInput, SummaryOutput
from app.models import loader

router = APIRouter()

@router.post("/summarize", response_model=SummaryOutput)
def summarize_text(body: TextInput):
    if not body.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    if len(body.text.split()) < 30:
        raise HTTPException(status_code=400, detail="Text too short to summarize. Please provide at least 30 words.")

    result = loader.summarize_pipeline(body.text, max_length=130, min_length=30, do_sample=False)
    return SummaryOutput(summary=result[0]["summary_text"])