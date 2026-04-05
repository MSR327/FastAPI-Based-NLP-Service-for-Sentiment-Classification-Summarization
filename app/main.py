# app/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.models.loader import load_models
from app.routes import sentiment, classify, summarize

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_models()
    yield

app = FastAPI(title="TextIQ", version="1.0", lifespan=lifespan)

app.include_router(sentiment.router, tags=["Sentiment"])
app.include_router(classify.router, tags=["Classify"])
app.include_router(summarize.router, tags=["Summarize"])

@app.get("/health")
def health():
    return {"status": "ok"}