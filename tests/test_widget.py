import pytest

# Реализация функции mask_account_card
def mask_account_card(data: str) -> str:
    if data.startswith("Счет"):
        return f"Счет **{data[-4:]}"
    else:
        parts = data.split()
        card_number = parts[-1]  # Предполагаем, что номер карты - это последнее слово
        if len(card_number) == 16:
            masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
            return f"{' '.join(parts[:-1])} {masked_card}"  # Возвращаем полное название карты с замаскированным номером
        else:
            return data  # Если формат не соответствует, возвращаем исходные данные


# Реализация функции get_date
def get_date(date_str: str) -> str:
    year, month, day = date_str.split("T")[0].split("-")
    return f"{day}.{month}.{year}"

# Тесты
@pytest.mark.parametrize("input_data, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
])


def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected

@pytest.mark.parametrize("input_date, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2018-06-30T02:08:58.425572", "30.06.2018"),
])


def test_get_date(input_date, expected):
    assert get_date(input_date) == expected







