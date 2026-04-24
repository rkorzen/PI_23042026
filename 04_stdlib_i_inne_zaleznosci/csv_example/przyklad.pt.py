import csv
import pprint
with open('logs.txt', 'r') as f:
    reader = csv.reader(f, delimiter=";")

    for row in reader:
        print(row)

data = [[x * y for x in range(1, 11)] for y in range(1, 11)]


pprint.pprint(data)

with open("data.csv", "w") as f:
    text = ""
    for row in data:
        text += ",".join(map(str, row)) + "\n"
    f.write(text)


with open("data2.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(data)

columns = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

data2 = [dict(zip(columns, row)) for row in data]


with open("data3.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
    writer.writeheader()
    writer.writerows(data2)


with open("data3.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)