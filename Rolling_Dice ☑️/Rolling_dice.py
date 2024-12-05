import tkinter as tk 
import random 

root=tk.Tk() 
root.title("Rolling Dice") 
root.geometry("300x300") 
root.configure(bg='pink')

label=tk.Label(root,font=("Helvetica", 200, 'bold'), text = "", fg ="white",bg= "black" )

def rolldice():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack(pady=10)


button = tk.Button(root,font=("Helvetica", 25, 'bold'),text="**Dice Roll**",fg ="green",bg= "white" , command = rolldice) 
button.pack(pady=5) 

root.mainloop()