# models.py
from pydantic import BaseModel

class IMCInput(BaseModel):
    poids: float
    taille_cm: float

class IMCResult(BaseModel):
    imc: float
    categorie: str
    conseil: str
