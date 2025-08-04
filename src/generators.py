def filter_by_currency(transactions, currency_code):
    """Фильтрует транзакции по указанной валюте."""
    return [transaction for transaction in transactions if transaction['operationAmount']['currency']['code'] == currency_code]

def transaction_descriptions(transactions):
    """Возвращает описания транзакций."""
    return (transaction['description'] for transaction in transactions)

def card_number_generator(start, end):
    """Генерирует номера карт в формате '0000 0000 0000 0000'."""
    for number in range(start, end + 1):
        # Форматируем номер карты с пробелами
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:16]
