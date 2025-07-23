# src/utils.py
import json
from typing import List, Dict

def read_json_file(file_path: str) -> List[Dict]:
    """Читает JSON-файл и возвращает список данных о транзакциях."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []