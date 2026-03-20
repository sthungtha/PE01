# main.py
"""
Recipe Manager Project
----------------------
7. Documentation and Comments:
This program is a command-line Recipe Manager. It allows users to add, view,
search, edit, and delete recipes. Data is persistently stored in a JSON file
within the 'data' directory.

To use, simply run `python main.py` and follow the on-screen menu prompts.
"""

from data_handler import load_recipes
from recipe_functions import (
    add_recipe, 
    view_recipes, 
    search_recipes, 
    edit_recipe, 
    delete_recipe
)

# --- 5. User Interface ---
def main() -> None:
    """Main program loop providing a simple CLI for the Recipe Manager."""
    # 4. Ensure data persists between runs by loading it on startup
    recipes = load_recipes()
    
    while True:
        print("\n" + "="*20)
        print("   Recipe Manager   ")
        print("="*20)
        print("1. Add recipe")
        print("2. View recipes")
        print("3. Search recipes")
        print("4. Edit recipe")
        print("5. Delete recipe")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        # 6. Testing and Validation: Handle user menu selection safely
        if choice == "1":
            add_recipe(recipes)
        elif choice == "2":
            view_recipes(recipes)
        elif choice == "3":
            search_recipes(recipes)
        elif choice == "4":
            edit_recipe(recipes)
        elif choice == "5":
            delete_recipe(recipes)
        elif choice == "6":
            print("Exiting Recipe Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()