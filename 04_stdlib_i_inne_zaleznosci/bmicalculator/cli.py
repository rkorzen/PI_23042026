import sys
from bmi import calculate_bmi, classify_bmi

print(sys.argv)

if len(sys.argv) != 3:
    print("Zle wywolanie: Poprawne to : python cli.py <wzrost w cm> <waga>")
    exit

wzrost = int(sys.argv[1])
waga = int(sys.argv[2])

bmi = calculate_bmi(waga, wzrost / 100)
print(f"bmi: {bmi:.2f}, to jest {classify_bmi(bmi)}")
