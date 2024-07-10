from tkinter import *
from PIL import ImageTk, Image

root = Tk()

img = Image.open("download5.png")
bg_img = ImageTk.PhotoImage(img)

label = Label(root, image=bg_img, borderwidth=100)
label.pack()

entry = Entry(root,width=40, highlightthickness=2)
entry.place(relx=0.5, rely=0.5, anchor=CENTER)



root.mainloop()
