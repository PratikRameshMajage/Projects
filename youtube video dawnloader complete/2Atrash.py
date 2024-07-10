# from tkinter import *
import tkinter as tk
# from tkinter import ttk
from PIL import ImageTk, Image
import os
from pytube import YouTube
from tkinter import messagebox as m_box
import subprocess
import threading

# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# # {FUNCTION}
# def onClick():
#     got_link = link.get()
#     got_path = path.get()
#     try:
#         yt = YouTube(str(got_link))
#     except:
#         m_box.showerror("Error", "Connection Problem !")
#     else:
#         vid = yt.streams.get_highest_resolution()
#         destination = str(got_path)
#         vid.download(destination)
#         os.startfile(got_path)
#         return m_box.showinfo('Successfully Downloaded.', f"Your YouTube Vidoe Downloaded Successfully at {got_path}/{yt.title}")


# threads = []

# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# # {FUNCTION}
# def startThredProcess():
#     myNewThread = threading.Thread(target=onClick)
#     threads.append(myNewThread)
#     myNewThread.start()

# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# # {BASIC GEOMETRY OF TKINTER}
# ####### Set the background color to red
# # window.configure(bg='red')

root = tk.Tk()
root.title("YouTube Video Downloader")
root.iconbitmap("youtube.ico")
root.configure(bg='black')
# root.geometry("440x350")
# root.minsize(440, 350)
# root.maxsize(440, 350)


# # label = ttk.Label(root)
# # label.grid(row=0, column=0, padx=100, pady=0)

# # img0 = Image.open("download5.png")
# # bg_img0 = ImageTk.PhotoImage(img0)
# # label = ttk.Label(root, image=bg_img0)
# # label.grid(row=0, column=0, padx=100, pady=100)

frame = tk.Frame(root, width=300, height=300, bg="white")
frame.grid(row=0, column=0, padx=50, pady=50,)
frame.pack_propagate(False)

logo_img = ImageTk.PhotoImage(file="wolf.png")
logo_widget = tk.Label(frame, image = logo_img, bg="white" )
logo_widget.image = logo_img
logo_widget.pack()

# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ######### Create a label widget and pack it
# # label = tk.Label(window, text='Hello, world!', font=('Arial', 12))
# # label.pack()
# ######### Set the font color to black
# # get_info.configure(foreground='black')
# ######### getting information of {DOWNLOADING VIDEO LINK}
# # (creating LABELS)
# get_info = ttk.Label(frame, text="@.Enter YouTube Video Link :- ", font=('Times', 12),foreground='white', background='black')
# get_info.grid(row=0, column=0,sticky=tk.W )

# # (VARIABLE STRING)
# link = tk.StringVar()

# img1 = Image.open("download1.png")
# bg_img1 = ImageTk.PhotoImage(img1)
# get_info = ttk.Label(frame, image=bg_img1)
# get_info.grid(row=1, columnspan=3, padx=0, pady=3)

# # (taking ENTRIES)
# yt_link = ttk.Entry(frame, width=40, textvariable=link, font=('Times', 10), foreground="green", )
# yt_link.grid(row=1, columnspan=3, padx=0, pady=3)
# yt_link.focus()

# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# # label = Label(root, image=bg_img)
# # label.pack()

# # entry = Entry(root,width=40, highlightthickness=2)
# # entry.place(relx=0.5, rely=0.5, anchor=CENTER)

# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# # getting information of {DOWNLOADING PATH}
# # (creating LABELS)
# get_info = ttk.Label(frame, text="@.Enter Downloading Path :- ", font=('Times', 12), foreground='white', background='black')
# get_info.grid(row=3, column=0, sticky=tk.W)
# # get_info.configure(foreground='black')

# # (VARIABLE STRING)
# path = tk.StringVar()

# img2 = Image.open("download2.png")
# bg_img2 = ImageTk.PhotoImage(img2)
# get_info = ttk.Label(frame, image=bg_img2)
# get_info.grid(row=4, columnspan=3, padx=0, pady=3)

# # (taking ENTRIES)
# download_path = ttk.Entry(frame, width=40, textvariable=path, font=('Times', 10), foreground="green")
# download_path.grid(row=4, columnspan=3, padx=0, pady=3)

# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# # Create a PhotoImage object for the button image
# button_image = ImageTk.PhotoImage(file="download3.png")

# {DOWNLOADING BUTTON TO DOWNLOAD VIDEO}
# btn1 = tk.Button(frame, image=button_image, borderwidth=0, command=startThredProcess)
# btn1 = tk.Button(frame, image=button_image)
# btn1.grid(row=1, column=0)
# button = tk.Button(window, text='Click me!', font=('Arial', 12), fg='blue', bg='white', command=my_function)
# button.config(width=10, height=2, state=tk.NORMAL, relief=tk.RAISED)

# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# # {END MAINLOOP}
root.mainloop()