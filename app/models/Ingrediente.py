from pydantic import BaseModel
import app.models.enums.UnidadMedida as UnidadMedida

class Ingrediente(BaseModel):
    id: int
    nombre: str
    cantidad: float
    unidad_cantidad: str

    class Config:
        arbitrary_types_allowed = True