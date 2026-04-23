# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import IMCInput, IMCResult
from calculator import calculer_imc

app = FastAPI()

@app.get("/")
def home():
    return {"status": "IMC API en ligne"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/calculer", response_model=IMCResult)

def calculer(data: IMCInput):
    return calculer_imc(data.poids, data.taille_cm) 
