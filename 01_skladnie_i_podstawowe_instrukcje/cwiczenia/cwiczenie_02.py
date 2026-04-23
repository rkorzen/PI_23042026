"""
mamy jakas kolekcje - liste obiektow

dane = [1, 2, 3, 4, 5, 6, 1, 2, 3, 10, "x"]


utworz nowa liste na podstawie dane, ktora bedzei zawierac unikalne liczby z dane

y = []
....

print(y)

[1, 2, 3, 4, 5, 6, 10]

.append
if
in
print()

type(1) == int
"""

dane = [1, 2, 3, 4, 5, 6, 1, 2, 3, 10, "x"]
output = []

for el in dane:
    if el in output or type(el) != int:
        continue
    output.append(el)

print(output)


## jako ciekawostke

print(list({el for el in dane if type(el) == int}))



dane = [1, 2, 3, 4, 5, 6, 1, 2, 3, 10, "x"]
output = []

for el in dane:
    if type(el) == int:
        output.append(el)


print(output)
print(set(output))
