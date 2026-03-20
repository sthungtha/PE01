# recipe_functions.py
from data_handler import save_recipes, Recipes

# --- 3. Implement Core Functionalities: Add Recipe ---
def add_recipe(recipes: Recipes) -> None:
    """Prompts the user to add a new recipe's title, ingredients, and instructions."""
    title = input("Enter recipe title: ").strip()
    
    # 6. Testing and Validation: Prevent empty titles
    if not title:
        print("Title cannot be empty. Aborting.")
        return

    ingredients = []
    print("Enter ingredients (leave blank to finish):")
    while True:
        ingredient = input("> ").strip()
        if not ingredient:
            break
        ingredients.append(ingredient)
        
    instructions = []
    print("Enter instructions (leave blank to finish):")
    while True:
        instruction = input("> ").strip()
        if not instruction:
            break
        instructions.append(instruction)
        
    recipes[title] = {"ingredients": ingredients, "instructions": instructions}
    save_recipes(recipes)
    print(f"Recipe '{title}' added successfully!")

# --- 3. Implement Core Functionalities: View Recipes ---
def view_recipes(recipes: Recipes) -> None:
    """Displays a list of all currently saved recipes."""
    if not recipes:
        print("No recipes found.")
        return
    print("\nAvailable recipes:")
    for title in recipes.keys():
        print(f"- {title}")

# --- 3. Implement Core Functionalities: Search Recipes ---
def search_recipes(recipes: Recipes) -> None:
    """Searches for recipes by matching the query against titles or ingredients."""
    query = input("Enter search query: ").strip().lower()
    matches = [
        (title, recipe)
        for title, recipe in recipes.items()
        if query in title.lower()
        or any(query in ingredient.lower() for ingredient in recipe["ingredients"])
    ]
    
    if not matches:
        print(f"No recipes found for '{query}'.")
        return
        
    print(f"\nRecipes matching '{query}':")
    for title, _ in matches:
        print(f"- {title}")

# --- 3. Implement Core Functionalities: Edit Recipe ---
def edit_recipe(recipes: Recipes) -> None:
    """Allows the user to modify an existing recipe's ingredients and instructions."""
    title = input("Enter recipe title to edit: ").strip()
    if title not in recipes:
        print(f"Recipe '{title}' not found.")
        return
        
    recipe = recipes[title]
    print(f"\nEditing recipe '{title}':")
    
    # Edit ingredients
    print("Current ingredients:")
    for i, ingredient in enumerate(recipe["ingredients"], start=1):
        print(f"{i}. {ingredient}")
    print("Enter new ingredients (leave blank to keep current):")
    
    new_ingredients = []
    while True:
        ingredient = input("> ").strip()
        if not ingredient:
            break
        new_ingredients.append(ingredient)
    recipe["ingredients"] = new_ingredients or recipe["ingredients"]
    
    # Edit instructions
    print("\nCurrent instructions:")
    for i, instruction in enumerate(recipe["instructions"], start=1):
        print(f"{i}. {instruction}")
    print("Enter new instructions (leave blank to keep current):")
    
    new_instructions = []
    while True:
        instruction = input("> ").strip()
        if not instruction:
            break
        new_instructions.append(instruction)
    recipe["instructions"] = new_instructions or recipe["instructions"]
    
    save_recipes(recipes)
    print(f"Recipe '{title}' updated successfully!")

# --- 3. Implement Core Functionalities: Delete Recipe ---
def delete_recipe(recipes: Recipes) -> None:
    """Removes a specific recipe from the dictionary and updates the file."""
    title = input("Enter recipe title to delete: ").strip()
    if title not in recipes:
        print(f"Recipe '{title}' not found.")
        return
        
    del recipes[title]
    save_recipes(recipes)
    print(f"Recipe '{title}' deleted successfully!")