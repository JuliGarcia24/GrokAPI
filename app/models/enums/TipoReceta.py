from enum import Enum

class TipoReceta(str, Enum):
    BREAKFAST_SNACK = "BREAKFAST_SNACK"
    LUNCH_DINNER = "LUNCH_DINNER"