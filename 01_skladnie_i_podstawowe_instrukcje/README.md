# markdown

* ele 1
* ele 2


1. xxx
2. xxx
3. xxx

[x](http://google.com)

**bold**
*italic*

| a | b |
|---|--- |
| 1 | 2 |
| 3 | 4 |


x = y + 1

# REPL

Z wiersza polecen odpalamy:

```
python
```

## przydante funkcje na poczatek

### `help`

```
help() - tryb interaktywnej pomocy

help("keywords") - pomoc dla konkretnego hasla

help("a".title) - pomoc dla konkretnwego obiekty. 


```

### `dir`

dir() - wypisuje nazwy z biezacej przestrzeni nazw

dir(<cos>) - wypisuje atrybuty tego obiektu

### `type`

type(<cos>) - zwroci nam typ danego obiektu


## podstawowe type

### typy liczbowe

#### int  - liczby calkowite

123  - liczba w systemie dziesietnym
0b0101 - liczba w systemie binarnym
0o1237 - liczba w systemie osemkowym
0xfff - liczba szesnatkowa

10_000_000 - mozemy stosowac _ jako wizualny separator

-123

int("ggg", base=17)


#### float - liczby zmiennoprzecinkowe

1.23

1.2e-10 - notacja naukowa

inf, -inf, nan

0.1 + 0.1 + 0.1 == 0.3

wiecej wyjasnienia tutaj:
https://pywaw.org/105/


#### complex - liczby zespolone

1 + 2j 

#### (bool)

False, True

True + True == 2

### opratory logiczne

and, or , not

    x > 10 and x % 2 == 0
    x > 10 or x % 2 == 0
    not False -> True





### operatory arytmetyczne

    + - / * 
    **  - potegowanie
    // - dzielenie calkowite
    % - modulo

```
x = 0
x = x + 1
x += 1

x /= 2  # x = x / 2

```

### zmienne

dobre:
x = 10 # x to jest zmienna
_1x = 10
x_y = 10

print = 10
int = 10

zle przyklady:

10 = x
1x = 10
x y = 10
for = 10  # keyword nie moze byc zmienna

konwencja: snake_case

### wyrazenia warunkowe
ogolnie:
if <warunek>:
   <blok instrukcji>

przyklad
if x > 10:
   print(x)
   print(x + 1)


ogolnie:
if <warunek>:
    <blok instrukcji>
else:
  <blok instrukcji>

przyklad

if x > 10:
   print(x)
else:
   print("za mala wartosc")



ogolnie:
if <warunek>:
   <blok instrukcji>
elif <warunek>:
    <blok instrukcji>
...
else:
    <blok instrukcji>

przyklad

if x > 10:
   print(x)
elif x > 5:
   print("x troche male")
else:
   print("za mala wartosc")

w innych jezykach bloki kodu wyznaczane sa przez nawiasy

if (x > 10) { print(x) } else { print("za mala wartosc") }

if (x > 10) { 
    print(x) 
} else { 
    print("za mala wartosc") 
}


### petle

#### petla for

for <zmienna> in <kolekcja>:
    <blok instrukcji>
<instrukcja po petlki>


continue - pominiecie biezacego iteracji
break - wyjscie z petli


### kolekcje

#### listy - list

x = []
x.append(1) # [1]
x.append(2) # [1, 2]

1 in x
1 not in x

#### zbiory - set

set() -  pusty zbior

A = {1, 2, 3}
B = {3, 4, 5}
C = {3, 5}
suma zbiorow = A | B
roznica zbiorow = A - B
wspolna zbiorowa = A & B
roznica symetryczna = A ^ B

czy C jest podzbiorem A

C.issubset(A)

# czy A jest nadzbiorem C

A.issuperset(C)


### slownik - dict

{
    "klucz": "wartosc",
    1: "a"
}

>>> x["c"]
Traceback (most recent call last):
  File "<python-input-45>", line 1, in <module>
    x["c"]
    ~^^^^^
KeyError: 'c'
>>> if "c" in x:
...     print(x["c"]
...     
... x.get("b")
... 
  File "<python-input-46>", line 2
    print(x["c"]
         ^
SyntaxError: '(' was never closed
>>> x.get("b")
2
>>> x.get("c")
>>> x["b"]
2
>>> x["b"] = 3
>>> x["b"]
3
>>> for el in x:
...     print(el)
...     
a
b
>>> for el in x.keys():
...     print(el)
...     
a
b
>>> for el in x.items():
...     print(el)
...     
('a', 1)
('b', 3)
>>> for k, v in x.items():
...     print(k, v)
...     
a 1
b 3
>>> 

### krotka - tuple

krotka jest niemutowalne

x = (1, 2, 3)
x.append(4) # bledne

