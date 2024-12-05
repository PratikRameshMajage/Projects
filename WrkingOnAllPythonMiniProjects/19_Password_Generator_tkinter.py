import tkinter as tk
import string
import random

# create the window
window = tk.Tk()
window.title("Password Generator")

# create labels for the password and length
password_label = tk.Label(window, text="", font=("Arial", 16))
length_label = tk.Label(window, text="Password Length:", font=("Arial", 12))

password_label.pack(pady=10)
length_label.pack()

# create an entry for the password length
length_entry = tk.Entry(window, width=5)
length_entry.pack()

# define function to generate password
def generate_password():
    # get the password length from the entry
    length = int(length_entry.get())
    
    # define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    # update the password label
    password_label.config(text=password)

# create button for generating password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# run the window
window.mainloop()
