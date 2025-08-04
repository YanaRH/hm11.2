import os
import http.client
import json
from typing import Dict

def convert_to_rub(transaction: Dict) -> float:
    """Конвертирует сумму транзакции в рубли, если валюта USD или EUR."""
    currency = transaction.get("currency")
    amount = transaction.get("amount", 0)

    # Если валюта уже в рублях, просто возвращаем сумму
    if currency == "RUB":
        return float(amount)

    # Проверка наличия API_KEY
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY is not set in the environment variables.")

    conn = http.client.HTTPSConnection("api.apilayer.com")
    url = f"/exchangerates_data/convert?from={currency}&to=RUB&amount={amount}"
    headers = {"apikey": api_key}

    try:
        conn.request("GET", url, headers=headers)
        response = conn.getresponse()

        if response.status == 200:
            data = response.read()
            result = json.loads(data).get("result", 0)
            return result
        else:
            return 0.0
    except Exception as e:
        print(f"Error during API request: {e}")
        return 0.0
    finally:
        conn.close()
