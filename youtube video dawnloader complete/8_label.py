import tkinter as tk

root = tk.Tk()

# Create a canvas widget to draw the curved border
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

# Draw the curved border using create_arc()
canvas.create_arc(10, 10, 190, 90, start=0, extent=359, style=tk.ARC, width=4)

# Create the label widget with a transparent background
label = tk.Label(canvas, text="Hello, World!", font=("Arial", 14))
label.place(x=100, y=50, anchor=tk.CENTER)

root.mainloop()
