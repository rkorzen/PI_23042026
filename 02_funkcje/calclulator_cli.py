import sys
import calculator
from calculator import operations as oper
print(sys.argv)

if len(sys.argv) != 4:
    print("Zle wywolanie: Poprawne to : python caluclator_cli.py + 10 20")
    exit

op, a, b = sys.argv[1:]
a = int(a)
b = int(b)
# result = calculator.operations[op](a, b)
result = oper[op](a, b)
print(result)
