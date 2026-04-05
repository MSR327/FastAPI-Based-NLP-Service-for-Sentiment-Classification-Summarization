# TextIQ 
A multi-task NLP REST API built with FastAPI and HuggingFace Transformers.

## Features
-  **Sentiment Analysis** — Positive / Negative detection
-  **Zero-Shot Classification** — Classify text into any custom categories
-  **Summarization** — Condense long text into key points

## Tech Stack
- FastAPI + Uvicorn
- HuggingFace Transformers 4.44.2
- Python 3.11
- Pydantic v2

## Setup
```bash
git clone https://github.com/yourusername/textiq.git
cd textiq
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/sentiment` | Analyze sentiment of text |
| POST | `/classify` | Zero-shot topic classification |
| POST | `/summarize` | Summarize long text |
| GET  | `/health`   | Health check |

## Example Requests

**Sentiment:**
```bash
curl -X POST http://localhost:8000/sentiment \
  -H "Content-Type: application/json" \
  -d '{"text": "This project is going really well!"}'
```

**Classify:**
```bash
curl -X POST http://localhost:8000/classify \
  -H "Content-Type: application/json" \
  -d '{"text": "The new iPhone has a stunning camera", "labels": ["technology", "sports", "politics"]}'
```

**Summarize:**
```bash
curl -X POST http://localhost:8000/summarize \
  -H "Content-Type: application/json" \
  -d '{"text": "Your long paragraph here..."}'
```
