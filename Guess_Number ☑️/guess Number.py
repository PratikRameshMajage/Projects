from tkinter import *
from random import randint
root =Tk()
root.title('guess Number')
root.config(bg='black')                  
root.geometry('400x300+700+90')
label = Label(root,text="Pick Number\nBetween 1 To 10",font=("Brush Script MT",20))
label.pack(pady=10)
def guesser():
    if guess.get().isdigit():
        label.config(text="Pick Number\nBetween 1 To 10")
        dif = abs(num - int(guess.get()))
        if int(guess.get()) == num:
            bc = "SystemButtonFace"
            label.config(text="Correct!!!!")
        elif dif == 5:
            bc = "white"
        elif dif < 5:
            bc = f'#ff{dif}{dif}{dif}{dif}'
        else:
            bc = f'#{dif}{dif}{dif}{dif}ff'
        root.config(bg=bc)
        label.config(bg=bc)
    else:
        guess .delete(0, END)
        label.config(text="That's not a label")
def rando():
    global num
    num = randint(0,10)
    guess .delete(0, END)
    label.config(bg="SystemButtonFace")
    root.config(bg="SystemButtonFace")
guess =Entry(root, font=("helvetica", 50), width=2)
guess.pack(pady=10)
guessB =Button(root, text="Submit", command = guesser)
guessB.pack(pady=10)
randoB = Button(root, text="New Number",command = rando)
randoB.pack(pady=10)
rando()
root.mainloop()