from tkinter import *
from tkinter import ttk
from calculate import exchange


def oblicz():
    try:
        currency = currency_entry.get()
        amount = float(amount_entry.get())
        result  = exchange(amount, currency)
        wynik.configure(text=f"Kupisz {result} {currency}")
    except (ValueError, ZeroDivisionError):
        wynik.configure(text="Błędne dane!")


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Kod waluty").grid(column=0, row=0)
currency_entry = ttk.Entry(frm)
currency_entry.grid(column=1, row=0)
ttk.Label(frm, text="Ilosc PLN").grid(column=0, row=1)
amount_entry = ttk.Entry(frm)
amount_entry.grid(column=1, row=1)
wynik = ttk.Label(frm, text="tu bedzie wynik")
wynik.grid(column=0, row=2)
ttk.Button(frm, text="Wymien", command=oblicz).grid(column=1, row=2)

root.mainloop()