import os
import json
import http.client
from unittest import mock
from unittest.mock import patch
from src.external_api import convert_to_rub

@patch("http.client.HTTPSConnection")
def test_convert_to_rub(mock_https_connection):
    # Настройка мока для соединения
    mock_response = mock.Mock()
    mock_response.status = 200
    mock_response.read.return_value = json.dumps({"result": 75.0}).encode('utf-8')

    # Настройка мока для соединения и запроса
    mock_https_connection.return_value.getresponse.return_value = mock_response

    # Установка переменной окружения API_KEY
    os.environ["API_KEY"] = "test_api_key"

    transaction = {"currency": "USD", "amount": 1}
    result = convert_to_rub(transaction)

    assert result == 75.0
    mock_https_connection.assert_called_once_with("api.apilayer.com")
    mock_https_connection.return_value.request.assert_called_once_with(
        "GET",
        "/exchangerates_data/convert?from=USD&to=RUB&amount=1",
        headers={"apikey": "test_api_key"}
    )

