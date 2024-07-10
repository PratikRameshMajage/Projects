from tkinter import *

root = Tk()
root.geometry("300x100")
root.title("YouTube Video Downloader")
root.configure(bg='black')
root.minsize(300, 100)
root.maxsize(300, 100)


# create an entry widget
entry = Entry(root, bg='black', fg='red',  width=15, font="Times")

# set the text in the entry widget
entry.insert(0, "Hello, PRATIK!")


# # disable the entry widget
# entry.config(state='disabled')

# pack the widget to display it
entry.pack(padx=10, pady=40)

root.mainloop()
