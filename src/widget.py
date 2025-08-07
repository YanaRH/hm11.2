def mask_account_card(data: str) -> str:
    if data.startswith("Счет"):
        # Маскировка для счета (показываем только последние 4 цифры)
        return f"Счет **{data[-4:]}"
    else:
        # Маскировка для карт (показываем первые 4 цифры, две группы цифр маскируем, и последние 4 цифры)
        parts = data.split()
        card_number = parts[-1]  # Предполагаем, что номер карты - это последнее слово
        if len(card_number) == 16:
            masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
            return f"{' '.join(parts[:-1])} {masked_card}"  # Возвращаем полное название карты с замаскированным номером
        else:
            return data  # Если формат не соответствует, возвращаем исходные данные


def get_date(date_str: str) -> str:
    # Преобразуем строку даты в нужный формат
    year, month, day = date_str.split("T")[0].split("-")
    return f"{day}.{month}.{year}"

if __name__ == "__main__":
    # Пример использования функций
    print(mask_account_card("Visa Platinum 7000792289606361"))  # "Visa Platinum 7000 79** **** 6361"
    print(mask_account_card("Счет 73654108430135874305"))  # "Счет **4305"
    print(get_date("2024-03-11T02:26:18.671407"))  # "11.03.2024"


    