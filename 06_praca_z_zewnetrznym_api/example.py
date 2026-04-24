# pip install requests

import requests

response = requests.get("https://api.nbp.pl/api/exchangerates/tables/A/")

print(response.status_code)

print(response.json())

"""
python example.py USD
3.56
"""