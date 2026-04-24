import sys
from calculate import exchange

if len(sys.argv) != 3:
    print("Zle wywolanie: Poprawne to : python cli.py <kod waluty> <kwota>")
    exit

currency, amount = sys.argv[1:]

print(exchange(float(amount), currency))