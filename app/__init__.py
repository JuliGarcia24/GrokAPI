from fastapi import FastAPI
from pydantic import BaseModel
from .services.groqAI_service import GroqService

app = FastAPI()
groq_service = GroqService()

@app.get("/")
def index():
    return {"message": f"Hola Jujo!, esta es tu key: {groq_service.groq_key}"}

@app.get("/recipe")
def groq():
    return groq_service.create_recipe()

@app.get("/daily_plan")
def generate_daily():
    return groq_service.create_daily_plan()

@app.get("/schema")
def show_json_schema():
    return groq_service.show_schema()
