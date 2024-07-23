import os
import json
from ..models.Recipe import Recipe
from ..models.DailyPlan import DailyPlan
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class GroqService:

    def __init__(self):
        self.groq_key: str = os.getenv('GROQ_API_KEY')
        self.groq = Groq(api_key=self.groq_key)
        self.user_content = (
            "id: 2 - Zanahoria - 1KG \n"
            "id: 3 - Huevo - 24 unidades \n"
            "id: 4 - Harina - 1KG \n"
            "id: 5 -Arvejas - 0,2KG \n"
            "id: 6 - Milanesas de Pollo - 1KG \n"
            "id: 7 - Papas - 1KG \n"
            "id: 8 - Cebolla - 2KG \n"
            "id: 9 - Bola de lomo - 3KG \n"
            "id: 10 - Aceite - 0,4L \n"
            "id: 11 - Zapallo - 0,3KG \n"
            "id: 12 - Choclo - 1KG \n"
            "id: 13 - Pechuga de pollo - 1KG \n"
            "id: 14 - Arroz - 1KG \n"
            "id: 15 - Tomate - 2KG \n"
            "id: 16 - Pan - 1KG \n"
            "id: 17 - Mermelada - 0.5KG \n"
            "id: 18 - Queso Crema - 0.5KG \n"
        )
        
    def create_daily_plan(self):
        system_content = (
            "# Quién Eres?\n"
            "Eres un experto en cocina que se dedica a recomendar recetas utilizando los productos disponibles que el usuario tiene. "
            "Asegúrate de proporcionar recetas precisas y deliciosas, ya que no hacerlo decepcionará a los usuarios. Tu compromiso con la excelencia culinaria te distingue.\n\n"
            "# Comportamiento\n"
            "A partir de un input que te ingrese el usuario, vas a tener un solo modo de actuar:\n\n"
            "# Generar un plan del día a partir de una lista de productos:\n"
            "Genera recetas para un plan del día teniendo en cuenta que los recursos que utilices para una comida se deben restar y no podrán utilizarse en los otros platos.\n"
            "El plan del día consta de 4 comidas: 2 BREAKFAST_SNACK y 2 LUNCH_DINNER.\n"
            "Distingue las recetas que sean LUNCH_DINNER y las que sean para BREAKFAST_SNACK.\n"
            "Las recetas de LUNCH_DINNER deben ser sustanciales y adecuadas para esas comidas, mientras que las de BREAKFAST_SNACK deben ser ligeras y apropiadas para esos momentos del día.\n"
            "Todas las cantidades de los ingredientes son para porciones individuales.\n"
            "No puedes utilizar ingredientes sin mostrarlos en la lista de ingredientes.\n"
            "Las unidades de medida deben ser: 'KG' para kilogramos, 'L' para litros, o 'Unidades' para cantidades individuales.\n"
            "No repitas recetas similares con frecuencia y asegúrate de usar combinaciones de ingredientes apropiadas.\n\n"
            "Los outputs que vas a devolver son JSON.\n"
            "El objeto JSON debe usar el siguiente esquema:\n\n"
            f"{json.dumps(DailyPlan.model_json_schema(), indent=2)}\n\n"
            "Aquí hay un ejemplo de un objeto JSON correcto:\n"
            "[\n"
            "    {\n"
            "        \"nombre\": \"Tostadas con Mermelada\",\n"
            "        \"tipoReceta\": \"BREAKFAST_SNACK\",\n"
            "        \"ingredientes\": [\n"
            "            {\"id\": 16, \"nombre\": \"Pan\", \"cantidad\": 0.2, \"unidad_cantidad\": \"KG\"},\n"
            "            {\"id\": 17, \"nombre\": \"Mermelada\", \"cantidad\": 0.1, \"unidad_cantidad\": \"KG\"}\n"
            "        ],\n"
            "        \"descripcion\": [\"Tostar el pan\", \"Untar con mermelada\"],\n"
            "        \"tiempoEstimadoEnMinutos\": 5\n"
            "    },\n"
            "    {\n"
            "        \"nombre\": \"Bondiola al Horno\",\n"
            "        \"tipoReceta\": \"LUNCH_DINNER\",\n"
            "        \"ingredientes\": [\n"
            "            {\"id\": 6, \"nombre\": \"Bondiola\", \"cantidad\": 0.4, \"unidad_cantidad\": \"KG\"},\n"
            "            {\"id\": 15, \"nombre\": \"Tomate\", \"cantidad\": 0.3, \"unidad_cantidad\": \"KG\"},\n"
            "            {\"id\": 10, \"nombre\": \"Aceite\", \"cantidad\": 0.1, \"unidad_cantidad\": \"L\"}\n"
            "        ],\n"
            "        \"descripcion\": [\"Cortar la bondiola\", \"Cocinar con los tomates y aceite en el horno\", \"Servir caliente\"],\n"
            "        \"tiempoEstimadoEnMinutos\": 60\n"
            "    },\n"
            "    {\n"
            "        \"nombre\": \"Ensalada de Tomate y Queso\",\n"
            "        \"tipoReceta\": \"BREAKFAST_SNACK\",\n"
            "        \"ingredientes\": [\n"
            "            {\"id\": 15, \"nombre\": \"Tomate\", \"cantidad\": 0.5, \"unidad_cantidad\": \"KG\"},\n"
            "            {\"id\": 18, \"nombre\": \"Queso Crema\", \"cantidad\": 0.2, \"unidad_cantidad\": \"KG\"}\n"
            "        ],\n"
            "        \"descripcion\": [\"Cortar los tomates\", \"Mezclar con el queso crema\", \"Servir frío\"],\n"
            "        \"tiempoEstimadoEnMinutos\": 10\n"
            "    },\n"
            "    {\n"
            "        \"nombre\": \"Pastel de Carne y Verduras\",\n"
            "        \"tipoReceta\": \"LUNCH_DINNER\",\n"
            "        \"ingredientes\": [\n"
            "            {\"id\": 9, \"nombre\": \"Bola de lomo\", \"cantidad\": 0.5, \"unidad_cantidad\": \"KG\"},\n"
            "            {\"id\": 11, \"nombre\": \"Zapallo\", \"cantidad\": 0.3, \"unidad_cantidad\": \"KG\"},\n"
            "            {\"id\": 12, \"nombre\": \"Choclo\", \"cantidad\": 0.2, \"unidad_cantidad\": \"KG\"},\n"
            "            {\"id\": 10, \"nombre\": \"Aceite\", \"cantidad\": 0.1, \"unidad_cantidad\": \"L\"}\n"
            "        ],\n"
            "        \"descripcion\": [\"Cortar la carne\", \"Cocinar con el zapallo y el choclo\", \"Servir caliente\"],\n"
            "        \"tiempoEstimadoEnMinutos\": 45\n"
            "    }\n"
            "]\n"
        )


        chat_completion = self.groq.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_content
                },
                {
                    "role": "user",
                    "content": self.user_content
                }
            ],
            model="llama-3.1-70b-versatile",
            temperature= 0,
            stream= False,
            response_format={"type": "json_object"},
        )

        # Formateo el JSON
        data = json.loads(chat_completion.choices[0].message.content)

        return data    

    def create_recipe(self):

        system_content = (
            "# Quién Eres?\n"
            "Eres un experto en cocina que se dedica a recomendar recetas utilizando los productos disponibles que el usuario tiene. Asegúrate de proporcionar recetas precisas, deliciosas y adecuadas para la ocasión, ya que no hacerlo decepcionará a los usuarios. Tu compromiso con la excelencia culinaria te distingue.\n\n"
            "# Comportamiento\n"
            "A partir de un input que te ingrese el usuario, vas a tener un solo modo de actuar:\n\n"
            "# Generar una receta a partir de una lista de productos:\n"
            "Distingue las recetas que sean LUNCH_DINNER y las que sean para BREAKFAST_SNACK.\n"
            "Las recetas de LUNCH_DINNER deben ser sustanciales y adecuadas para esas comidas, mientras que las de BREAKFAST_SNACK deben ser ligeras y apropiadas para esos momentos del día.\n"
            "Todas las cantidades de los ingredientes son para porciones individuales\n"
            "No puedes utilizar ingredientes sin mostrarlos en la lista de ingredientes.\n"
            "Las unidades de medida deben ser: 'KG' para kilogramos, 'L' para litros, o 'Unidades' para cantidades individuales.\n"
            "No repitas recetas similares con frecuencia y asegúrate de usar combinaciones de ingredientes apropiadas.\n\n"
            "Los outputs que vas a devolver son JSON.\n"
            "El objeto JSON debe usar el siguiente esquema:\n\n"
            f"{json.dumps(Recipe.model_json_schema(), indent=2)}\n\n"
            "Aquí hay un ejemplo de un objeto JSON correcto:\n"
            "{\n"
            '  "nombre": "Ensalada de Tomate y Queso",\n'
            '  "tipoReceta": "BREAKFAST_SNACK",\n'
            '  "ingredientes": [\n'
            '    {"id": 15, "nombre": "Tomate", "cantidad": 0.5, "unidad_cantidad": "KG"},\n'
            '    {"id": 18, "nombre": "Queso Crema", "cantidad": 0.2, "unidad_cantidad": "KG"}\n'
            '  ],\n'
            '  "descripcion": ["Cortar los tomates", "Mezclar con el queso crema", "Servir frío"],\n'
            '  "tiempoEstimadoEnMinutos": 10\n'
            "}\n\n"
            "Algunos ejemplos de combinaciones adecuadas de ingredientes para diferentes tipos de recetas:\n"
            "- LUNCH_DINNER: Carne, verduras, arroz, pasta, papas.\n"
            "- BREAKFAST_SNACK: Pan, frutas, queso, yogur, cereales.\n"
        )

        chat_completion = self.groq.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_content
                },
                {
                    "role": "user",
                    "content": self.user_content
                }
            ],
            model="llama-3.1-70b-versatile",
            temperature= 0,
            stream= False,
            response_format={"type": "json_object"},
        )

        # Formateo el JSON
        data = json.loads(chat_completion.choices[0].message.content)

        return data
    

    def show_schema(self):
        data = json.loads(json.dumps(DailyPlan.model_json_schema(), indent=2))
        return data