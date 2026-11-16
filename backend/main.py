from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

app = FastAPI(title="Synergy Translation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_NAME = "Helsinki-NLP/opus-mt-ru-en"

print("Загрузка модели... Пожалуйста, подождите.")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
print("Модель успешно загружена!")

class TranslationRequest(BaseModel):
    text: str

@app.post("/translate")
def translate(req: TranslationRequest):
    if not req.text.strip():
        return {"translation": ""}
        
    inputs = tokenizer(req.text, return_tensors="pt", truncation=True, max_length=512)
    
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=512)
        
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"translation": result}
