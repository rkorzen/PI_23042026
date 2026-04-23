"""
Podaj tekst: Ala ma kota

Dlugosc tekstu: 12

Frekwencje samoglosek:
- a: 4
- o: 1

####

- musimy umiec zamienic napisa na male litery (dir(str))
- musimy umiec ustawiac jakies wartosci w slowniku:

>>> x["c"] = x.get("c", 0) + 1
>>> x
{'a': 1, 'b': 3, 'c': 1}
>>> x["c"] = x.get("c", 0) + 1
>>>
>>> x
{'a': 1, 'b': 3, 'c': 2}
>>>


"""

samogloski = "aeiou"

licznik_samoglosek = {} # przyda sie get

text = input("Podaj tekst: ")

