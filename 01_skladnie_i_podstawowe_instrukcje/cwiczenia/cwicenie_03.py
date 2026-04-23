"""
Bazujac na ponizszym kodzie
wypisz odpoweidz na pytania:

1. ile bylo unikalnych liczb wprowadzony przez uzytkownika
2. ile z tych liczb to liczby parzyste z zakresu 1 do 100

len(kolekcja)
"""

liczby_parzyste_z_1_do_100 = range(2, 101, 2)

while True:
    x = input("Podaj liczbe lub q by zakonczyc")
    if x == "q":
        break
    print(x)

n_unikalnych_liczb = ...
n_parzystych_z_1_do_100 = ...
print("Liczba unikalnych liczb: ", n_unikalnych_liczb)
print("Parzyste z zakresu 1 do 100: ", n_parzystych_z_1_do_100)