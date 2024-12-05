import tkinter as tk
from tkinter import scrolledtext

# Create the main window
window = tk.Tk()
window.title("Note-taking App")

# Create the text area
text_area = scrolledtext.ScrolledText(window, width=50, height=20, font=("Arial", 12))
text_area.pack()

# Create the save function
def save_file():
    file_name = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_name:
        with open(file_name, "w") as file:
            file.write(text_area.get("1.0", tk.END))

# Create the open function
def open_file():
    file_name = tk.filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_name:
        text_area.delete("1.0", tk.END)
        with open(file_name, "r") as file:
            text_area.insert(tk.END, file.read())

# Create the menu bar
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

# Start the GUI main loop
window.mainloop()
