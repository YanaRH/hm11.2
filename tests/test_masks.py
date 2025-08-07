import pytest
from src.masks import get_mask_card_number, get_mask_account

# Parameterized tests for mask_card_number with added exception handling
@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567890123456", "1234 56** **** 3456"),
    ("", None),  # Изменено на None, чтобы соответствовать ожиданиям
    ("12345", None),  # Это должно вызывать исключение
])
def test_get_mask_card_number(card_number, expected):
    if card_number == "12345":  # Тест на исключение
        with pytest.raises(ValueError, match="Card number must be 16 digits long."):
            get_mask_card_number(card_number)
    elif card_number == "":  # Проверка на пустую строку
        with pytest.raises(ValueError, match="Card number must be 16 digits long."):
            get_mask_card_number(card_number)
    else:
        assert get_mask_card_number(card_number) == expected


# Parameterized tests for mask_account with added exception handling
@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("12345678901234567890", "**7890"),
    ("", None),  # Изменено на None, чтобы соответствовать ожиданиям
    ("123", None),  # Это должно вызывать исключение
])


def test_get_mask_account(account_number, expected):
    if account_number == "123":  # Тест на исключение
        with pytest.raises(ValueError, match="Account number must have at least 4 digits."):
            get_mask_account(account_number)
    elif account_number == "":  # Проверка на пустую строку
        with pytest.raises(ValueError, match="Account number must have at least 4 digits."):
            get_mask_account(account_number)
    else:
        assert get_mask_account(account_number) == expected

