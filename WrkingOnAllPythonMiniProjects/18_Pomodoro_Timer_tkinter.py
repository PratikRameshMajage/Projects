import tkinter as tk
import time

# define constants
WORK_TIME = 25 * 60  # 25 minutes in seconds
BREAK_TIME = 5 * 60  # 5 minutes in seconds

# create the window
window = tk.Tk()
window.title("Pomodoro Timer")

# create labels for the timer
timer_label = tk.Label(window, text="00:00", font=("Arial", 30))
timer_label.pack(pady=10)

# create buttons for starting and stopping the timer
start_button = tk.Button(window, text="Start")
stop_button = tk.Button(window, text="Stop")

start_button.pack(side=tk.LEFT, padx=10)
stop_button.pack(side=tk.RIGHT, padx=10)

# define function to update the timer
def update_timer(time_left):
    # calculate minutes and seconds from time_left
    minutes = time_left // 60
    seconds = time_left % 60
    
    # format the time as a string and update the label
    time_str = f"{minutes:02}:{seconds:02}"
    timer_label.config(text=time_str)
    
    # call the function again after 1 second
    if time_left > 0:
        window.after(1000, update_timer, time_left - 1)

# define function to start the timer
def start_timer():
    # get the work or break time depending on the current state
    if start_button["text"] == "Start":
        time_left = WORK_TIME
        start_button["text"] = "Pause"
    else:
        time_left = int(timer_label["text"][:2]) * 60 + int(timer_label["text"][3:])
        start_button["text"] = "Pause"
        
    # update the timer
    update_timer(time_left)

# define function to stop the timer
def stop_timer():
    start_button["text"] = "Start"
    timer_label.config(text="00:00")

# add command to the buttons
start_button.config(command=start_timer)
stop_button.config(command=stop_timer)

# run the window
window.mainloop()
