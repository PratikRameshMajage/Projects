import tkinter as tk

# Create a Tkinter window
window = tk.Tk()

# Create a label widget
label = tk.Label(window, text="Hello, world!")

# Create a frame widget
frame = tk.Frame(window,)

# Pack the label and frame widgets
label.pack()
frame.pack()

# Run the Tkinter event loop
window.mainloop()
