import tkinter as tk
import tkinter.ttk as ttk
import webbrowser

class WebBrowser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Web Browser")
        self.geometry("800x600")

        # Create address bar and go button
        self.address_bar = ttk.Entry(self)
        self.address_bar.pack(fill='x', padx=10, pady=10)
        self.go_button = ttk.Button(self, text='Go', command=self.load_webpage)
        self.go_button.pack(side='right', padx=10)

        # Create browser window using a text widget
        self.browser_window = tk.Text(self)
        self.browser_window.pack(fill='both', expand=True)

    def load_webpage(self):
        url = self.address_bar.get()
        if url.startswith('http://') or url.startswith('https://'):
            webbrowser.open(url)
            self.browser_window.insert('end', f"Opening {url}\n")
            self.browser_window.see('end')
        else:
            self.browser_window.insert('end', f"Invalid URL: {url}\n")
            self.browser_window.see('end')
        self.address_bar.delete(0, 'end')

if __name__ == '__main__':
    app = WebBrowser()
    app.mainloop()
