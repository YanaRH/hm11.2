from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список операций по статусу.

    :param data: Список словарей с операциями
    :param state: Статус для фильтрации (по умолчанию 'EXECUTED')
    :return: Новый список словарей, отфильтрованный по статусу
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате.

    :param data: Список словарей с операциями
    :param reverse: Если True, сортировка по убыванию (по умолчанию)
    :return: Новый список словарей, отсортированный по дате
    """
    return sorted(data, key=lambda x: x['date'], reverse=reverse)


if __name__ == "__main__":
    # Пример данных для проверки
    data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    filtered = filter_by_state(data)
    sorted_data = sort_by_date(data)
    print(filtered)
    print(sorted_data)