import tkinter as tk
import tkinter.messagebox as messagebox
import csv

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        # create the contact list as a dictionary
        self.contacts = {}

        # create the GUI elements
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, padx=5, pady=5)

        self.save_button = tk.Button(self.root, text="Save Contacts", command=self.save_contacts)
        self.save_button.grid(row=3, column=1, padx=5, pady=5)

        self.listbox = tk.Listbox(self.root)
        self.listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.load_contacts()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name == "" or phone == "" or email == "":
            messagebox.showwarning("Error", "Please enter all fields")
            return

        if name in self.contacts:
            messagebox.showwarning("Error", "Contact already exists")
            return

        self.contacts[name] = {"phone": phone, "email": email}

        self.listbox.insert(tk.END, name)
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def save_contacts(self):
        with open("contacts.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for name, info in self.contacts.items():
                writer.writerow([name, info["phone"], info["email"]])
        messagebox.showinfo("Save", "Contacts saved successfully")

    def load_contacts(self):
        try:
            with open("contacts.csv", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    name = row[0]
                    phone = row[1]
                    email = row[2]
                    self.contacts[name] = {"phone": phone, "email": email}
                    self.listbox.insert(tk.END, name)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
