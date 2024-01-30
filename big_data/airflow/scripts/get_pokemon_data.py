import requests
import pandas as pd
from datetime import datetime
import os
import logging  

print("TESTE")
logging.info('Hello')

logger = logging.getLogger("airflow.task")


POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"
CSV_FILE_PATH = "./data/pokemon_data.csv"

def get_pokemon_data(pokemon_id):
    response = requests.get(f"{POKEAPI_URL}{pokemon_id}")

    data = response.json()

    name = data["name"]
    base_experience = data["base_experience"]
    height = data["height"]
    weight = data["weight"]
    logger.info(f"get_pokemon_data {pokemon_id}: {name}")

    df = pd.DataFrame([[name, base_experience, height, weight]],
                      columns=["Name", "Base Experience", "Height", "Weight"])

    df.to_csv(CSV_FILE_PATH, mode='a', index=False, header=not os.path.exists(CSV_FILE_PATH))

def run_get_data():
    logger.warning("This is a warning  message")
    logger.info("This is a log message")

    logger.info(f"Iniciando get_pokemon_data ")
    
    for pokemon_id in range(1, 6):
        get_pokemon_data(pokemon_id)

if __name__ == "__main__":
    run_get_data()
