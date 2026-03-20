# data_handler.py
import json
import os
from typing import Dict, List

# --- 2. Define Recipe Data Structure ---
# Using type hints to represent a recipe as a dictionary and a collection of recipes.
Recipe = Dict[str, List[str]]
Recipes = Dict[str, Recipe]

# Define the path to the data folder and file
DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "recipes.json")

# Ensure the data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# --- 4. File Handling: Load Recipes ---
def load_recipes() -> Recipes:
    """Loads recipes from a JSON file. Returns an empty dict if not found."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # 6. Testing and Validation: Handle edge cases where file is missing or corrupted
        return {}

# --- 4. File Handling: Save Recipes ---
def save_recipes(recipes: Recipes) -> None:
    """Saves the current recipe dictionary to a JSON file to ensure data persists."""
    with open(DATA_FILE, "w") as file:
        json.dump(recipes, file, indent=4) # Added indent for readable JSON