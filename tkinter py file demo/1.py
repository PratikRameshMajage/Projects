from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# "width x height"
root.geometry("500x200")

# title
root.title("Pratik")

# width , height
# root.minsize(300,200)

# width , height
# root.maxsize(500,200)

# pack()
A = Label(text="Hello Pratik...")
A.pack()

# PhotoImage()
# photo = PhotoImage(file="1.png")
# B = Label(image=photo)
# B.pack()

# PhotoImage()  using IamgeTk.PhotoImage()
# ///////////////////////i don't know why it's not running/////////////////////////////
# image = Image.open("Tony.jpg")
# photo = ImageTk.PhotoImage(image)

# text label options
# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

# title_label = Label(text ='''
# # Abdul Rashid Salim Salman Khan is an Indian \nfilm actor, producer, occasional playback singer and television personality. In a film career spanning \nalmost thirty years, Khan has received numerous awards, including two National Film Awards as a film \nproducer, and two Filmfare Awards for acting. He has a significant following in Asia and the Indian \ndiaspora worldwide, and is cited in the media as one of the most commercially successful actors of Indian \ncinema. According to the Forbes 2018 list of Top-Paid 100 Celebrity Entertainers in world, Khan was \nthe highest ranked Indian with 82nd rank with earnings of $37.7 million.''', bg ="black", fg="white", padx=13, pady=94, font="comicsansms 10 bold", borderwidth=3, relief=SUNKEN)

# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
# title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)


f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN )
f1.pack(side=LEFT)

l = Label(f1, text="Pratik Majage")
l.pack()




root.mainloop()