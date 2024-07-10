from tkinter import *

root = Tk()

button = Button(root, text='Click me!', bg='blue', fg='white', font=('Arial', 16), command=lambda: print('Button clicked!'))

button.pack()

root.mainloop()
