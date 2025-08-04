from fastapi import FastAPI, UploadFile, Form, Header, HTTPException
from app import extract_insights_api  # importa do app.py

app = FastAPI()

# Registra o endpoint da API que já existe no app.py
app.post("/extract-insights")(extract_insights_api)
