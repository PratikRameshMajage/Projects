import tkinter as tk
from tkinter import messagebox

class ChatApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chat Application")
        self.geometry("400x500")
        
        # Create chat history text widget
        self.chat_history = tk.Text(self, state='disabled')
        self.chat_history.pack(fill='both', expand=True)

        # Create input field and send button
        self.input_field = tk.Entry(self)
        self.input_field.pack(side='left', fill='x', expand=True)
        self.send_button = tk.Button(self, text='Send', command=self.send_message)
        self.send_button.pack(side='right')

        # Bind Enter key to send message
        self.bind('<Return>', lambda event: self.send_message())

    def send_message(self):
        message = self.input_field.get()
        if message:
            self.chat_history.configure(state='normal')
            self.chat_history.insert('end', f"You: {message}\n")
            self.chat_history.see('end')
            self.chat_history.configure(state='disabled')
            self.input_field.delete(0, 'end')
        else:
            messagebox.showerror('Error', 'Message field is empty')

if __name__ == '__main__':
    app = ChatApplication()
    app.mainloop()
