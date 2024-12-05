import tkinter as tk
from tkinter import filedialog

def browse_directory():
    directory = filedialog.askdirectory()
    print("Selected directory:", directory)

root = tk.Tk()
root.geometry("400x300")
root.title("File Explorer")

browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.pack(pady=50)

root.mainloop()
