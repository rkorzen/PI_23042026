def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Pamietaj cholero, nie dziel przez 0")
    return a / b

operations = {
    "+": add, 
    "-": sub,
    "*": mul, 
    "/": div
}

def get_numeric_data(name):
    while True:
        try:
            x = input(f"Podaj arg {name}: ")
            x = int(x)
            return x
        except ValueError:
            print("Podaj liczbe")

def get_data_from_console():
    op = input("Podaj rodzaj operacji (+-/*): ")

    a = get_numeric_data("a")
    b = get_numeric_data("b")

    return op, a, b

def main():
    op, a, b = get_data_from_console()

    result = operations[op](a, b)

    print(f"Wynik {a} {op} {b} == {result}") 

