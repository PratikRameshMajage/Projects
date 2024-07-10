import tkinter as tk
from PIL import ImageTk, Image
import os
from pytube import YouTube
from tkinter import messagebox as m_box
import subprocess
import threading

# {FUNCTION}
def onClick():
    got_link = link.get()
    got_path = path.get()
    try:
        yt = YouTube(str(got_link))
    except:
        m_box.showerror("Error", "Connection Problem !")
    else:
        vid = yt.streams.get_highest_resolution()
        destination = str(got_path)
        vid.download(destination)
        os.startfile(got_path)
        return m_box.showinfo('Successfully Downloaded.', f"Your YouTube Vidoe Downloaded Successfully at {got_path}/{yt.title}")

# {FUNCTION}
threads = []
def startThredProcess():
    myNewThread = threading.Thread(target=onClick)
    threads.append(myNewThread)
    myNewThread.start()
# TKINTER MAINLOOP
root = tk.Tk()
root.title("YouTube Video Downloader")
root.iconbitmap("youtube.ico")
root.configure(bg='black')
# Frame
frame = tk.Frame(root, width=300, height=500, bg="pink")
frame.grid(row=0, column=0, padx=50, pady=50,)
frame.pack_propagate(False)
# ImageFrame
logo_img = ImageTk.PhotoImage(file="wolf.png")
logo_widget = tk.Label(frame, image = logo_img, bg="pink" )
logo_widget.image = logo_img
logo_widget.pack()
# Link
get_info = tk.Label(frame, text="@.Enter YouTube Video Link :- ", font=('Times', 12),foreground='white', background='black').pack(pady=20)
link = tk.StringVar()
yt_link = tk.Entry(frame, width=40, textvariable=link, font=('Times', 10), foreground="green",).pack(pady=10)
# Path
get_info = tk.Label(frame, text="@.Enter Downloading Path :- ", font=('Times', 12), foreground='white', background='black').pack(pady=20)
path = tk.StringVar()
download_path = tk.Entry(frame, width=40, textvariable=path, font=('Times', 10), foreground="green").pack(pady=10)
# Button
tk.Button(frame, text="DOWNLOAD", font=("TkHeadingFont",20), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2", activeforeground="black", command=lambda:startThredProcess()).pack(pady=20)

root.mainloop()