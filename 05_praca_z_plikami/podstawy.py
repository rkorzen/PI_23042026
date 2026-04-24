with open("text.txt", "w") as f:
    f.write("""
A;1
B;2
C;3
D;4
E;5
    """)

with open("text.txt", "r") as f:
    for line in f:
        print(line.strip().lower().split(";"))
