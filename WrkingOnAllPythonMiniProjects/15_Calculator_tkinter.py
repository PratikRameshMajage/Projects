import tkinter as tk

def add_to_display(number):
    display.insert(tk.END, number)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    expression = display.get()
    try:
        result = str(eval(expression))
    except ZeroDivisionError:
        result = "Error: Division by zero"
    clear_display()
    add_to_display(result)

# create the main window
root = tk.Tk()
root.title("Calculator")

# create the display widget
display = tk.Entry(root, width=20, justify="right")
display.grid(row=0, column=0, columnspan=4)

# create the number buttons
button_1 = tk.Button(root, text="1", command=lambda: add_to_display("1"))
button_1.grid(row=1, column=0)

button_2 = tk.Button(root, text="2", command=lambda: add_to_display("2"))
button_2.grid(row=1, column=1)

button_3 = tk.Button(root, text="3", command=lambda: add_to_display("3"))
button_3.grid(row=1, column=2)

button_4 = tk.Button(root, text="4", command=lambda: add_to_display("4"))
button_4.grid(row=2, column=0)

button_5 = tk.Button(root, text="5", command=lambda: add_to_display("5"))
button_5.grid(row=2, column=1)

button_6 = tk.Button(root, text="6", command=lambda: add_to_display("6"))
button_6.grid(row=2, column=2)

button_7 = tk.Button(root, text="7", command=lambda: add_to_display("7"))
button_7.grid(row=3, column=0)

button_8 = tk.Button(root, text="8", command=lambda: add_to_display("8"))
button_8.grid(row=3, column=1)

button_9 = tk.Button(root, text="9", command=lambda: add_to_display("9"))
button_9.grid(row=3, column=2)

button_0 = tk.Button(root, text="0", command=lambda: add_to_display("0"))
button_0.grid(row=4, column=1)

# create the operator buttons
button_plus = tk.Button(root, text="+", command=lambda: add_to_display("+"))
button_plus.grid(row=1, column=3)

button_minus = tk.Button(root, text="-", command=lambda: add_to_display("-"))
button_minus.grid(row=2, column=3)

button_multiply = tk.Button(root, text="*", command=lambda: add_to_display("*"))
button_multiply.grid(row=3, column=3)

button_divide = tk.Button(root, text="/", command=lambda: add_to_display("/"))
button_divide.grid(row=4, column=3)

button_clear = tk.Button(root, text="C", command=clear_display)
button_clear.grid(row=4, column=0)

button_equals = tk.Button(root, text="=", command=calculate)
button_equals.grid(row=4, column=2)

# start the main loop
root.mainloop()
