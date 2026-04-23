zakupy = {
    "Gouda": {"cena_za_kg": 12.5, "ilosc_kg": 10},
    "Ketchup": {"cena_za_kg": 1.5, "ilosc_kg": 6.5},
    "Mustard": {"cena_za_kg": 2.5, "ilosc_kg": 1.2},
    "Mayonnaise": {"cena_za_kg": 0.5, "ilosc_kg": 1.4},
    "Kebab": {"cena_za_kg": 5, "ilosc_kg": 1},
    "Sos 100 wysp": {"cena_za_kg": 1.5, "ilosc_kg": 2.5},
}

"""
Zakupy:
Gouda        12.50 PLN, 10.0 kg, 125.00 PLN
...
Sos 100 wysp  1.50 PLN,  2.5 kg,   3.75 PLN
"""

raport = """
Zakupy:
"""

for nazwa, dane in zakupy.items():
    c_kg = dane["cena_za_kg"]
    ilosc_kg = dane["ilosc_kg"]
    cena = c_kg * ilosc_kg
    raport += f"{nazwa:15} {c_kg:6.2f}\n"

print(raport)