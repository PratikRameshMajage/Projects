import tkinter as tk
import requests

class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']
  
    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount
  
class App:
    def __init__(self, master):
        self.master = master
        master.title("Currency Converter")
        master.geometry("300x200")
        
        self.currency_converter = CurrencyConverter('https://api.exchangerate-api.com/v4/latest/USD')
        
        self.amount_label = tk.Label(master, text="Amount")
        self.amount_label.pack()
        
        self.amount_entry = tk.Entry(master)
        self.amount_entry.pack()
        
        self.from_label = tk.Label(master, text="From Currency")
        self.from_label.pack()
        
        self.from_entry = tk.Entry(master)
        self.from_entry.pack()
        
        self.to_label = tk.Label(master, text="To Currency")
        self.to_label.pack()
        
        self.to_entry = tk.Entry(master)
        self.to_entry.pack()
        
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
        
        self.convert_button = tk.Button(master, text="Convert", command=self.convert_currency)
        self.convert_button.pack()
        
    def convert_currency(self):
        from_currency = self.from_entry.get().upper()
        to_currency = self.to_entry.get().upper()
        amount = float(self.amount_entry.get())
        converted_amount = self.currency_converter.convert(from_currency, to_currency, amount)
        result = f"{amount} {from_currency} is equal to {converted_amount} {to_currency}"
        self.result_label.config(text=result)

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
