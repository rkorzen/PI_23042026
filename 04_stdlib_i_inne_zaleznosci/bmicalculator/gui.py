from tkinter import *
from tkinter import ttk
from bmi import calculate_bmi, classify_bmi


def oblicz():
    try:
        w = float(waga_entry.get())
        h = float(wzrost_entry.get()) / 100
        bmi = calculate_bmi(w, h)
        wynik.configure(text=f"Twoje BMI: {classify_bmi(bmi)}")
    except (ValueError, ZeroDivisionError):
        wynik.configure(text="Błędne dane!")


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Wzrost").grid(column=0, row=0)
wzrost_entry = ttk.Entry(frm)
wzrost_entry.grid(column=1, row=0)
ttk.Label(frm, text="Waga").grid(column=0, row=1)
waga_entry = ttk.Entry(frm)
waga_entry.grid(column=1, row=1)
wynik = ttk.Label(frm, text="tu bedzie wynik")
wynik.grid(column=0, row=2)
ttk.Button(frm, text="Oblicz", command=oblicz).grid(column=1, row=2)

root.mainloop()