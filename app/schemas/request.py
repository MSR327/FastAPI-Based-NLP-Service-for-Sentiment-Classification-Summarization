# app/schemas/request.py
from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

class SentimentOutput(BaseModel):
    label: str
    score: float

class ClassifyInput(BaseModel):
    text: str
    labels: list[str] = ["technology", "sports", "politics", "entertainment", "business"]

class ClassifyOutput(BaseModel):
    label: str
    score: float

class SummaryOutput(BaseModel):
    summary: str