from typing import List, Dict, Iterator


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Генератор, который возвращает транзакции с заданной валютой.
    """
    for transaction in transactions:
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, который возвращает описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction.get('description', '')


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор, который выдает номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.
    """
    for number in range(start, end + 1):
        yield f"{number:016}".replace(" ", "").rjust(19, '0')