import tkinter.ttk as ttk
from tkinter import *

root = Tk()

# create a PhotoImage object from the Tkinter logo
# logo_image = ttk.PhotoImage(file="python.gif")

# create a label with the Tkinter logo
# logo_label = ttk.Label(root, image=logo_image)
# logo_label.pack()

# set the custom logo for the GUI window
# logo_image = PhotoImage(file="my_logo.gif")
root.iconbitmap("youtube.ico")

root.mainloop()
