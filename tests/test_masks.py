import pytest
from src.masks import get_mask_card_number, get_mask_account


# Parameterized tests for mask_card_number with added exception handling
@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567890123456", "1234 56** **** 3456"),
    ("", ""),
    ("12345", None),  # This should raise an exception
])
def test_get_mask_card_number(card_number, expected):
    if card_number == "12345":  # Test for exception
        with pytest.raises(ValueError, match="Card number must be 16 digits long."):
            get_mask_card_number(card_number)
    else:
        assert get_mask_card_number(card_number) == expected


# Parameterized tests for mask_account with added exception handling
@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("12345678901234567890", "**7890"),
    ("", ""),
    ("123", None),  # This should raise an exception
])
def test_get_mask_account(account_number, expected):
    if account_number == "123":  # Test for exception
        with pytest.raises(ValueError, match="Account number must have at least 4 digits."):
            get_mask_account(account_number)
    else:
        assert get_mask_account(account_number) == expected
