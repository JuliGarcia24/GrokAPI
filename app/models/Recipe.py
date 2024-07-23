from pydantic import BaseModel
from typing import List, Optional
import app.models.enums.TipoReceta as TipoReceta
from .Ingrediente import Ingrediente

class Recipe(BaseModel):
    nombre: str
    # tipoReceta: TipoReceta
    tipoReceta: str
    ingredientes: List[Ingrediente]
    descripcion: List[str]
    tiempoEstimadoEnMinutos: int

    class Config:
        arbitrary_types_allowed = True