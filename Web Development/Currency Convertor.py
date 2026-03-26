import requests

API_KEY = 'fca_live_FEalNAP17LZcbiTXbnAsDaGsYhzzf2yECnVM0P7o'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "INR", "AUD"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['data']
    except:
        print("Invalid Currency.")
        return None

while True:
    pin = input("Continue or Quit? (y/n): ").upper()
    if pin == "N":
        break

    money = int(input("Enter Money: "))
    base = input("Enter the base currency to exchange: ").upper()

    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value * money:.2f}")

