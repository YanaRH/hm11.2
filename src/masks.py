def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты в формате XXXX XX** **** XXXX.

    :param card_number: Номер банковской карты (16 цифр)
    :return: Замаскированный номер карты
    """

    if len(card_number) != 16:
        raise ValueError("Card number must be 16 digits long.")

    # Первые 6 цифр и последние 4 цифры остаются, остальное заменяется на звездочки

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета в формате **XXXX.

    :param account_number: Номер банковского счета
    :return: Замаскированный номер счета
    """

    if len(account_number) < 4:
        raise ValueError("Account number must have at least 4 digits.")

    # Последние 4 цифры отображаются, перед ними ставятся две звездочки

    return f"**{account_number[-4:]}"
