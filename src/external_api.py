# src/external_api.py
import os
import requests
from typing import Dict

def convert_to_rub(transaction: Dict) -> float:
    """Конвертирует сумму транзакции в рубли, если валюта USD или EUR."""
    currency = transaction.get("currency")
    amount = transaction.get("amount", 0)
    if currency == "RUB":
        return float(amount)

    api_key = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert"
    params = {"from": currency, "to": "RUB", "amount": amount}

    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json().get("result", 0)
    else:
        return 0.0