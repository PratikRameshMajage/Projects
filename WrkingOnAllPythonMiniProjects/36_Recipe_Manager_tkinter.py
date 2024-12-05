import tkinter as tk

# Define functions
def add_recipe():
    recipe_name = entry_recipe_name.get()
    ingredients = entry_ingredients.get("1.0", "end-1c")
    instructions = entry_instructions.get("1.0", "end-1c")
    
    # Add code to save the recipe to a file or database
    
    # Clear the fields
    entry_recipe_name.delete(0, tk.END)
    entry_ingredients.delete("1.0", tk.END)
    entry_instructions.delete("1.0", tk.END)

def clear_fields():
    entry_recipe_name.delete(0, tk.END)
    entry_ingredients.delete("1.0", tk.END)
    entry_instructions.delete("1.0", tk.END)

def exit_app():
    root.quit()

# Create the main window

root = tk.Tk()
root.title("Recipe Manager")
root.geometry("400x400")


# Add labels
lbl_recipe_name = tk.Label(root, text="Recipe Name")
lbl_recipe_name.pack()

lbl_ingredients = tk.Label(root, text="Ingredients")
lbl_ingredients.pack()

lbl_instructions = tk.Label(root, text="Instructions")
lbl_instructions.pack()

# Add entry boxes
entry_recipe_name = tk.Entry(root)
entry_recipe_name.pack()

entry_ingredients = tk.Text(root, height=5)
entry_ingredients.pack()

entry_instructions = tk.Text(root, height=10)
entry_instructions.pack()

# Add buttons
btn_add = tk.Button(root, text="Add Recipe")
btn_add.pack()

btn_clear = tk.Button(root, text="Clear Fields")
btn_clear.pack()

btn_exit = tk.Button(root, text="Exit", command=root.quit)
btn_exit.pack()

btn_add.config(command=add_recipe)
btn_clear.config(command=clear_fields)
btn_exit.config(command=exit_app)

root.mainloop()

