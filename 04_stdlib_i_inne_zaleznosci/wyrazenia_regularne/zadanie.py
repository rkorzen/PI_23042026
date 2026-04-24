"""
Napisz wzorce ktore rozpoznaja nastepujace elementy;

- kod pocztowy - xx-xxx
- emil xxxx@xxx.xx  - liter, cyfry, kropka i znak podkreslenia
- daty w formacie dd <month> dddd  - month - to jan jun jul



"""
import re

ZIP_CODE = r"\b\d{2}-\d{3}\b"
EMAIL = r"[\w\.\-]+@\w+\.+\w+"
DATE = r"\d{2} [A-Z][a-z]{2} \d{4}"

re.match(ZIP_CODE, "17-120")
re.match(EMAIL, "rkorzen@wp.pl")
re.match(DATE, "17 Jan 2026")

with open("dane.txt") as f:
    text = f.read()

    print(re.findall(ZIP_CODE, text))
    print(re.findall(EMAIL, text))
    print(re.findall(DATE, text))