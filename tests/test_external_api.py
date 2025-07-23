# tests/test_external_api.py
from unittest.mock import patch
from src.external_api import convert_to_rub

@patch("src.external_api.requests.get")
def test_convert_to_rub(mock_get):
    mock_get.return_value.json.return_value = {"result": 75.0}
    mock_get.return_value.status_code = 200
    transaction = {"currency": "USD", "amount": 1}
    assert convert_to_rub(transaction) == 75.0