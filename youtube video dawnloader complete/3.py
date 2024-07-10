import tkinter as tk

# Create a Tkinter window
window = tk.Tk()

# Create a label widget and pack it
label = tk.Label(window, text='Hello, world!', font=('Arial', 12))
label.pack()

# Set the font color to green
label.configure(fg='green')

# Run the main loop
window.mainloop()