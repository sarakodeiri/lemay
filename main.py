from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Load the sentiment analysis pipeline from Hugging Face
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

class InferenceRequest(BaseModel):
    texts: List[str]

@app.post("/infer/")
def infer(request: InferenceRequest):
    """
    Performs sentiment analysis on a list of texts.
    """
    return sentiment_pipeline(request.texts)

@app.get("/")
def read_root():
    return {"message": "Inference server is running"}