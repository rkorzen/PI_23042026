# 01. Składnia i podstawowe instrukcje

To są notatki z pierwszych zajęć. Zebrane są tutaj podstawy, które były pokazywane w REPL-u i w krótkich skryptach.

## Na start

Tryb interaktywny:

```bash
python3
```

Uruchomienie pliku:

```bash
python3 przyklady/petle_for.py
python3 przyklady/wyrazenia_warunkowe.py
```

Na początku warto znać:

- `help()` - wbudowana pomoc.
- `help("keywords")` - słowa kluczowe języka.
- `help(str.lower)` - pomoc dla metody lub funkcji.
- `dir()` - co mam aktualnie w przestrzeni nazw.
- `dir("abc")` - jakie metody ma dany obiekt.
- `type(x)` - jaki jest typ.
- `len(x)` - długość napisu, listy itp.

## Podstawowe typy

### `int`

Liczby całkowite:

```python
123
-45
0b1010
0o17
0xFF
10_000_000
```

Konwersje:

```python
int("15")
int("FF", base=16)
```

### `float`

Liczby zmiennoprzecinkowe:

```python
3.14
1.2e-10
```

Uwaga:

```python
0.1 + 0.1 + 0.1 == 0.3
```

To daje `False`, bo `float` ma ograniczoną precyzję.

### `complex`

```python
1 + 2j
complex(2, 3)
```

### `bool`

```python
True
False
```

`bool` w Pythonie jest spokrewniony z `int`:

```python
True + True == 2
False == 0
```

### `str`

Napisy:

```python
"Ala ma kota"
'Python'
"""
To jest
wielolinijkowy napis.
"""
```

Podstawowe operacje:

```python
tekst = "Ala ma kota"

tekst.lower()
tekst.upper()
len(tekst)
"kot" in tekst
```

### `None`

`None` oznacza brak wartości.

## Zmienne

Poprawne przykłady:

```python
x = 10
liczba_studentow = 24
_tmp = 5
wiek_uzytkownika = 30
```

Niepoprawne przykłady:

```python
1x = 10
x y = 10
for = 10
```

Wnioski:

- nazwa nie zaczyna się od cyfry,
- nie ma spacji,
- nie używamy słów kluczowych,
- trzymamy się `snake_case`.

Zła praktyka:

```python
print = 10
list = [1, 2, 3]
```

Tak można nadpisać wbudowane nazwy i potem samemu sobie utrudnić życie.

## Przypisanie i operatory

### Przypisanie

```python
x = 10
x = x + 1
x += 1
x *= 2
x /= 2
```

### Operatory arytmetyczne

```python
+   # dodawanie
-   # odejmowanie
*   # mnożenie
/   # dzielenie
//  # dzielenie całkowite
%   # modulo
**  # potęgowanie
```

Przykłady:

```python
2 + 3
7 // 2
7 % 2
4 ** 3
```

### Operatory porównania

```python
==
!=
<
<=
>
>=
```

Wynik porównania to zawsze `True` albo `False`.

### Operatory logiczne

```python
and
or
not
```

Przykłady:

```python
x > 10 and x % 2 == 0
x > 10 or x % 2 == 0
not False
```

Ważna rzecz: Python liczy warunki leniwie.

```python
x = 1
x > 5 and x / 0 == 1
```

Tutaj nie będzie błędu dzielenia przez zero, bo pierwszy warunek już jest `False`, więc Python nie musi sprawdzać drugiego.

Przykład z zajęć: [przyklady/operatory_logiczne_i_bledy.py](./przyklady/operatory_logiczne_i_bledy.py)

## Instrukcje warunkowe

Podstawowy schemat:

```python
if warunek:
    instrukcja
```

Przykład:

```python
x = 10

if x > 5:
    print(x)
```

Wersja z `else`:

```python
if x > 10:
    print("duża wartość")
else:
    print("za mała wartość")
```

Wersja z `elif`:

```python
if x > 10:
    print("duża wartość")
elif x > 5:
    print("średnia wartość")
else:
    print("mała wartość")
```

Najważniejsza rzecz na początku: blok kodu wyznacza wcięcie.

Po `:` zaczyna się blok i wszystko, co należy do tego bloku, musi mieć poprawne wcięcie.

Przykład z katalogu: [przyklady/wyrazenia_warunkowe.py](./przyklady/wyrazenia_warunkowe.py)

## Pętle

### `for`

Najczęściej używamy jej do przechodzenia po sekwencji albo kolekcji.

```python
for element in kolekcja:
    print(element)
```

Przykład:

```python
dane = "ala ma kota"

for znak in dane:
    print(znak)
```

Iteracja po zakresie:

```python
for i in range(5):
    print(i)
```

To wypisze `0, 1, 2, 3, 4`.

Jeszcze jeden wariant:

```python
for i in range(2, 10, 2):
    print(i)
```

### `while`

`while` działa tak długo, jak długo warunek jest prawdziwy.

```python
licznik = 0

while licznik < 3:
    print(licznik)
    licznik += 1
```

### `break` i `continue`

- `break` - wychodzimy z pętli.
- `continue` - pomijamy bieżący krok i lecimy dalej.

Przykład:

```python
for znak in "ala ma! kota":
    if znak == " ":
        continue
    if znak == "!":
        break
    print(znak)
```

Pełny przykład: [przyklady/petle_for.py](./przyklady/petle_for.py)

## Kolekcje

### Lista - `list`

Uporządkowana, mutowalna kolekcja.

```python
liczby = [1, 2, 3]
liczby.append(4)

print(liczby)      # [1, 2, 3, 4]
print(liczby[0])   # 1
print(2 in liczby) # True
```

### Krotka - `tuple`

Podobna do listy, ale niemutowalna.

```python
punkt = (10, 20)
```

### Zbiór - `set`

Przechowuje unikalne elementy.

```python
set()
{1, 2, 3}
```

Operacje:

```python
A = {1, 2, 3}
B = {3, 4, 5}
C = {3, 5}

A | B
A - B
A & B
A ^ B
C.issubset(B)
```

Zbiory są bardzo przydatne, gdy:

- chcemy usunąć duplikaty,
- interesują nas unikalne wartości,
- chcemy szybko sprawdzać przynależność.

### Słownik - `dict`

Pary `klucz: wartość`.

```python
licznik = {}
licznik["a"] = 1
licznik["a"] = licznik.get("a", 0) + 1
```

Iteracja po słowniku:

```python
for klucz, wartosc in licznik.items():
    print(f"{klucz}: {wartosc}")
```

To się przydaje np. do liczenia liter albo słów.

## `input()` i `print()`

Pobieranie danych:

```python
tekst = input("Podaj tekst: ")
```

Ważne:

- `input()` zawsze zwraca napis,
- jeśli chcemy liczbę, to trzeba zrobić konwersję, np. `int(...)`.

Wypisywanie:

```python
print("Wynik:", tekst)
```

f-string:

```python
imie = "Ala"
print(f"Cześć, {imie}!")
```

## `try` / `except`

Przy danych od użytkownika to się bardzo szybko przydaje.

```python
try:
    liczba = int(input("Podaj liczbę: "))
except ValueError:
    print("To nie jest poprawna liczba")
```

Czyli:

- próbujemy wykonać kod,
- jeśli poleci `ValueError`, to obsługujemy błąd i program się nie wywali.

## Rzeczy, o których łatwo zapomnieć

- `=` to przypisanie, `==` to porównanie.
- `input()` daje `str`, nie `int`.
- `float` nie nadaje się do ścisłych porównań bez zastanowienia.
- `set` nie służy do zachowywania kolejności.
- po `:` musi być wcięty blok.
- `type(x) == int` działa, ale często lepiej użyć `isinstance(x, int)`.
- nie nadpisujemy nazw typu `print`, `list`, `set`, `int`.

## Pliki z tego modułu

Przykłady:

- [przyklady/wyrazenia_warunkowe.py](./przyklady/wyrazenia_warunkowe.py)
- [przyklady/operatory_logiczne_i_bledy.py](./przyklady/operatory_logiczne_i_bledy.py)
- [przyklady/petle_for.py](./przyklady/petle_for.py)

Ćwiczenia:

- [cwiczenia/cwiczenie01.py](./cwiczenia/cwiczenie01.py) - liczby i konwersje typów.
- [cwiczenia/cwiczenie_02.py](./cwiczenia/cwiczenie_02.py) - filtrowanie danych i usuwanie duplikatów.
- [cwiczenia/cwicenie_03.py](./cwiczenia/cwicenie_03.py) - `while`, `input`, `set`, `try/except`.
- [cwiczenia/cwiczenia_04.py](./cwiczenia/cwiczenia_04.py) - napisy i zliczanie wystąpień w słowniku.

## Jak z tym pracować

Najlepszy tryb nauki na tym etapie:

1. Uruchomić przykład.
2. Zmienić dane wejściowe.
3. Zepsuć coś celowo i zobaczyć błąd.
4. Przepisać fragment samodzielnie.
5. Dopiero potem przejść do ćwiczeń.
