"""
$ python prosta_baza_pracownikow.py

[D]odac pracownika czy [W]ypsac czy Q by zakonczyc? D

imie: Rafal
stawka: 100.00

[D]odac pracownika czy [W]ypsac czy Q by zakonczyc?? W

1. Rafal (100.00)

[D]odac pracownika czy [W]ypsac czy Q by zakonczyc?? Q

$ python prosta_baza_pracownikow.py

[D]odac pracownika czy [W]ypsac czy Q by zakonczyc?? W

1. Rafal (100.00)


"""
import json

def read_data():
    try:
        with open("employees.json", "r") as f:
            employees = json.load(f)
            return employees
    except FileNotFoundError:
        return []

def save_data(employees):
    with open("employees.json", "w") as f:
        json.dump(employees, f, indent=4)

def add_employee():
    imie = input("Imie: ")
    stawka = input("Stawka: ")

    employees.append((imie, int(stawka)))


def display_employees():
    for i, (imie, stawka) in enumerate(employees, 1):
        print(f"{i}. {imie} ({stawka})")

def main():
    while True:
        command = input("[D]odac pracownika czy [W]ypsac czy Q by zakonczyc? ")
        if command.lower() == "q":
            break

        if command.lower() == "d":
            add_employee()

        elif command.lower() == "w":
            display_employees()

employees = read_data()
main()
save_data(employees)

