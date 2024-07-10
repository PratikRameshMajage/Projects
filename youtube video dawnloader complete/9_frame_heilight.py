import tkinter as tk
from PIL import ImageTk, Image

# frame = tk.Frame(root, width=200, height=100, bg="yellow", bd=50, highlightcolor="black", highlightthickness=10)
# frame.pack()

# frame = tk.Frame(root, width=500, height=430, bg="pink")
# frame.grid(row=0, column=0, padx=50, pady=50,)
# frame.pack_propagate(False)

# logo_img = ImageTk.PhotoImage(file="IronMan.png")
# logo_widget = tk.Label(frame, image = logo_img, bg="pink" )
# logo_widget.image = logo_img
# logo_widget.pack()

# frame = tk.Frame(root, width=500, height=350, bg="pink").pack()

root = tk.Tk()
root.geometry("500x350")
root.minsize(500, 350)
root.maxsize(500, 350)

bg = ImageTk.PhotoImage(file = "IronMan.png")
my_label = tk.Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(root, text='Hello, world!', font=('Arial', 12))
label.pack(pady=50)

tk.Button(root, text="DOWNLOAD", font=("TkHeadingFont",20), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2", activeforeground="black", command=lambda:load_frame2()).pack(pady=90)

root.mainloop()