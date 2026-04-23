"""
Na podstawie ponizszego programu odpowiedz na pytania:

1. Ile unikalnych liczb wpisal uzytkownik?
2. Ile z tych unikalnych liczb jest parzystych i miesci sie w zakresie od 1 do 100?

Wskazowka:
- liczbe elementow w zbiorze mozesz sprawdzic za pomoca `len(kolekcja)`
"""

parzyste_liczby_od_2_do_100 = set(range(2, 101, 2))
unikalne_liczby_uzytkownika = set()

while True:
    wprowadzona_wartosc = input("Podaj liczbe lub 'q', aby zakonczyc: ")
    if wprowadzona_wartosc.lower() == 'q':
        break
    try:
        unikalne_liczby_uzytkownika.add(int(wprowadzona_wartosc))
    except ValueError:
        print("To nie jest poprawna liczba!")

unikalne_parzyste_liczby_w_zakresie = (
    unikalne_liczby_uzytkownika & parzyste_liczby_od_2_do_100
)

print(f"Liczba unikalnych liczb: {len(unikalne_liczby_uzytkownika)}")
print(
    "Unikalne liczby parzyste z zakresu 1-100: "
    f"{unikalne_parzyste_liczby_w_zakresie}"
)
print(
    "Liczba unikalnych liczb parzystych z zakresu 1-100: "
    f"{len(unikalne_parzyste_liczby_w_zakresie)}"
)

"""
[2, 3, 2, 3, 2, 3] 

Liczba unikalnych liczb: 2
Unikalne liczby parzyste z zakresu 1-100: {2}
Liczba unikalnych liczb parzystych z zakresu 1-100: 1

"""
