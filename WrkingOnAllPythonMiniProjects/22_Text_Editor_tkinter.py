import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox

class TextEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text Editor")
        self.root.geometry("800x600")

        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill="both", expand=True)

        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About", command=self.about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        self.root.config(menu=self.menu_bar)

    def new_file(self):
        self.text_area.delete("1.0", "end")

    def open_file(self):
        filetypes = (("Text Files", "*.txt"), ("All Files", "*.*"))
        filename = filedialog.askopenfilename(title="Open File", filetypes=filetypes)
        if filename:
            with open(filename, "r") as file:
                self.text_area.delete("1.0", "end")
                self.text_area.insert("1.0", file.read())

    def save_file(self):
        try:
            filename = self.current_file
            with open(filename, "w") as file:
                file.write(self.text_area.get("1.0", "end-1c"))
        except:
            self.save_file_as()

    def save_file_as(self):
        filetypes = (("Text Files", "*.txt"), ("All Files", "*.*"))
        filename = filedialog.asksaveasfilename(title="Save As", filetypes=filetypes)
        if filename:
            with open(filename, "w") as file:
                file.write(self.text_area.get("1.0", "end-1c"))
            self.current_file = filename

    def exit_app(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.root.destroy()

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def about(self):
        messagebox.showinfo("About", "Text Editor v1.0")

    def run(self):
        self.current_file = None
        self.root.mainloop()

if __name__ == "__main__":
    app = TextEditor()
    app.run()
