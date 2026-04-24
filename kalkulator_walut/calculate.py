# pip install requests

import requests


API_URL = "https://api.nbp.pl/api/exchangerates/tables/A/"

def get_mid_for_currency(currency):
    response = requests.get(API_URL)
    rates = response.json()[0]["rates"]
    for item in rates:
        if item["code"] == currency:
            return item["mid"]

def exchange(amount, to_currency):
    return round(
        amount * get_mid_for_currency(to_currency), 2
    )

if __name__ == "__main__":
    print(exchange(10, "USD"))