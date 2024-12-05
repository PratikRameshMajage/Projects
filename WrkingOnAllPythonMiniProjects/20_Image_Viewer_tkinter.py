from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")

# Open image
my_img = Image.open("moon-knight.jpg")
# Resize image
my_img = my_img.resize((600, 400))
# Create ImageTk object
img = ImageTk.PhotoImage(my_img)

# Create label to display image
my_label = Label(image=img)
my_label.pack()

root.mainloop()
