from pydantic import BaseModel
from .Recipe import Recipe
from typing import List, Optional

class DailyPlan(BaseModel):
    recetas: List[Recipe]