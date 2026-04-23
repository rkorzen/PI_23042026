"""
Podaj tekst: Ala ma kota

Dlugosc tekstu: 12

Frekwencje samoglosek:
- a: 4
- o: 1

####

- musimy umiec zamienic napisa na male litery (dir(str))
- musimy umiec ustawiac jakies wartosci w slowniku:

>> x["c"] = x.get("c", 0) + 1
>> x
{'a': 1, 'b': 3, 'c': 1}
>> x["c"] = x.get("c", 0) + 1
>>
>> x
{'a': 1, 'b': 3, 'c': 2}
>>


for litera, licznik in x.items():
    print(f"{litera}: {licznik}")


x["klucz"] = 1

"""

samogloski = "aeiou"

licznik_samoglosek = {} # przyda sie get

text = input("Podaj tekst: ")

print("Długość tekstu:", len(text))

for znak in text.lower():
    if znak in samogloski:
        licznik_samoglosek[znak] = licznik_samoglosek.get(znak, default=0) + 1

for litera, licznik in licznik_samoglosek.items():
    print(" - ", litera, ": ", licznik)
    print(" - ", litera, ": ", licznik, sep="")
    print(" - " + litera + ": " + str(licznik))
    print(" - %s: %d" % (litera, licznik))
    print(" - {}: {}".format(litera, licznik))
    print(" - {a}: {b}".format(a=litera, b=licznik))
    print(f" - {litera}: {licznik}") # f-string

