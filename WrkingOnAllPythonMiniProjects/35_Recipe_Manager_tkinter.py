import json

# Load the existing recipes from a file into a dictionary
with open("recipes.json", "r") as f:
    recipes = json.load(f)

# Define functions to add, update, delete, and display the recipes
def add_recipe():
    name = input("Enter the name of the recipe: ")
    ingredients = input("Enter the ingredients separated by commas: ").split(",")
    instructions = input("Enter the instructions: ")
    recipes[name] = {"ingredients": ingredients, "instructions": instructions}
    save_recipes()

def update_recipe():
    name = input("Enter the name of the recipe to update: ")
    if name in recipes:
        ingredients = input("Enter the new ingredients separated by commas: ").split(",")
        instructions = input("Enter the new instructions: ")
        recipes[name] = {"ingredients": ingredients, "instructions": instructions}
        save_recipes()
    else:
        print("Recipe not found.")

def delete_recipe():
    name = input("Enter the name of the recipe to delete: ")
    if name in recipes:
        del recipes[name]
        save_recipes()
    else:
        print("Recipe not found.")

def display_recipes():
    for name, recipe in recipes.items():
        print(name)
        print("Ingredients:", ", ".join(recipe["ingredients"]))
        print("Instructions:", recipe["instructions"])
        print()

def save_recipes():
    with open("recipes.json", "w") as f:
        json.dump(recipes, f)

# Display a menu with options to view, add, update, or delete a recipe
while True:
    print("Recipe Manager")
    print("1. View Recipes")
    print("2. Add Recipe")
    print("3. Update Recipe")
    print("4. Delete Recipe")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        display_recipes()
    elif choice == "2":
        add_recipe()
    elif choice == "3":
        update_recipe()
    elif choice == "4":
        delete_recipe()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

