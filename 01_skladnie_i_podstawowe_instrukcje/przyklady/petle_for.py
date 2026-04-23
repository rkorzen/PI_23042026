dane = "ala ma! kota"

for znak in dane:  # iteracja po danej sekwencji
    if znak == " ":
        continue
    elif znak == "!":
        break
    print(znak)

