# pip install requests
import sys
import requests

currency = sys.argv[1] if len(sys.argv) > 1 else "USD"

response = requests.get("https://api.nbp.pl/api/exchangerates/tables/A/")

print(response.status_code)

rates = response.json()[0]["rates"]

for item in rates:
    if item["code"] == currency:
        print(item["mid"])
        break

"""
python example.py USD
3.56
"""