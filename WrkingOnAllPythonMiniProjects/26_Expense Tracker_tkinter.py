import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Expense Tracker")

# Create a label and entry for the expense amount
amount_label = tk.Label(root, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

# Create a label and entry for the expense description
description_label = tk.Label(root, text="Description:")
description_label.pack()
description_entry = tk.Entry(root)
description_entry.pack()

# Create a button to add the expense
def add_expense():
    amount = float(amount_entry.get())
    description = description_entry.get()
    print(f"Added expense: ${amount} - {description}")
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.pack()

# Run the main loop
root.mainloop()
