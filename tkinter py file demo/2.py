import tkinter as tk
from PIL import Image, ImageTk

def load_frame1():
    

    logo_img = ImageTk.PhotoImage(file="wolf.png")
    logo_widget = tk.Label(frame1, image = logo_img, bg="pink" )
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(frame1, text="Hellow Guys", bg= "black", fg="white", font=("Times",15)).pack()

    tk.Button(frame1, text="SUFFLE", font=("TkHeadingFont",20), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2", activeforeground="black", command=lambda:load_frame2()).pack(pady=20)


def load_frame2():
    print("Hello Pratik")

root = tk.Tk()
# root.geometry("400x400")
root.title("Pratik")
root.iconbitmap("youtube.ico")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=300, height=300, bg="pink")
frame2 = tk.Frame(root, bg="pink")
frame1.pack_propagate(False)

for frame in (frame1, frame2):
    frame1.grid(row=0 ,column=0,)

load_frame1()

root.mainloop()