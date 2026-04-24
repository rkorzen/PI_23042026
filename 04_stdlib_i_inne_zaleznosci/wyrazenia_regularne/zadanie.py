"""
Napisz wzorce ktore rozpoznaja nastepujace elementy;

- kod pocztowy - xx-xxx
- emil xxxx@xxx.xx  - liter, cyfry, kropka i znak podkreslenia
- daty w formacie dd <month> dddd  - month - to jan jun jul



"""
import re

ZIP_CODE = ""
EMAIL = ""
DATE = ""

re.match(ZIP_CODE, "17-120")
re.match(EMAIL, "rkorzen@wp.pl")
re.match(DATE, "17 Jan 2026")