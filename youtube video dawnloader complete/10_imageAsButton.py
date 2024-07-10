from tkinter import *


# Define the button click function
def button_click():
    print("Button clicked!")

# Create a Tkinter window
root = Tk()

# Create a PhotoImage object for the button image
button_image = PhotoImage(file="download6.png")

# Create a Button widget with the button image
button = Button(root, image=button_image,  fg='white', borderwidth=0, command=button_click)
button.pack()

# Run the Tkinter event loop
root.mainloop()
