# app/routes/classify.py
from fastapi import APIRouter, HTTPException
from app.schemas.request import ClassifyInput, ClassifyOutput
from app.models import loader

router = APIRouter()

@router.post("/classify", response_model=ClassifyOutput)
def classify_text(body: ClassifyInput):
    if not body.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    result = loader.classify_pipeline(body.text, candidate_labels=body.labels)
    return ClassifyOutput(
        label=result["labels"][0],
        score=round(result["scores"][0], 4)
    )