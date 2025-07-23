import re
from datetime import datetime

def mask_account_card(data: str) -> str:
    if data.startswith("Счет"):
        # Маскировка для счета (показываем только последние 4 цифры)
        return f"Счет **{data[-4:]}"
    else:
        # Маскировка для карт (показываем первые 4 цифры, две группы цифр маскируем, и последние 4 цифры)
        masked = re.sub(r'(\d{4})\d{2}(\d{2})\d{4}(\d{4})', r'\1 \2** **** \3', data)
        return masked

def get_date(date_str: str) -> str:
    # Преобразуем строку даты в объект datetime и форматируем в нужный формат
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")

if __name__ == "__main__":
    # Пример использования функций
    print(mask_account_card("Visa Platinum 7000792289606361"))  # "Visa Platinum 7000 79** **** 6361"
    print(mask_account_card("Счет 73654108430135874305"))  # "Счет **4305"
    print(get_date("2024-03-11T02:26:18.671407"))  # "11.03.2024"
    