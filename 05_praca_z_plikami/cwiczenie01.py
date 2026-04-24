"""
Dla kazdego uzytkownika z logs.txt policz sumaryczny czas spedzony w systemie.
Dane posortowane po czasie (malejaco) zapisz do pliku results.txt

- user1: 25860
- user19: 15679

[opcjonalnie]

Dodaj mozliwosc parametryzowania pliku wejsciowego i wyjsciowego

python cwiczenie01.py logs.txt results2.txt


"""
import sys
from collections import defaultdict

def handle_input():
    input = "logs.txt"
    output = "results.txt"
    if len(sys.argv) > 1:
        input = sys.argv[1]
    if len(sys.argv) > 2:
        output = sys.argv[2]
    return input, output


input_file, output_file = handle_input()

last_login = {}
total_time = defaultdict(int)

with open(input_file) as f:
    for line in f:
        user, action, t = line.split(";")
        t = int(t)

        if action == "LOGIN":
            last_login[user] = t
        else:
            total_time[user] += t - last_login[user]

data = sorted(total_time.items(), key=lambda x: x[1], reverse=True)

output = ""
for d in data:
    output += f" - {d[0]:>8}: {d[1]}\n"

with open(output_file, "w") as f:
    f.write(output)

print("Dane zapisane do pliku:", output_file)
