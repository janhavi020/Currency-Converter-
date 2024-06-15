import os
import requests

API_KEY = os.environ.get("api_key")

base_currency = input("Enter the base currency: ").upper()
target_currency = input("Enter target currency: ").upper()
amount = int(input("Amount: "))

URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base_currency}/{target_currency}/{amount}"

response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    converted_amount = data["conversion_result"]
    print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}")
else:
    print("Error fetching exchange rate data")
