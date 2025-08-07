import pytest
import os
import json
from src.utils import read_json_file


def test_read_json_file_empty():
    # Тест для несуществующего файла
    assert read_json_file("data/non_existent_file.json") == []

    # Тест для пустого файла
    with open("data/empty_file.json", "w") as f:
        f.write("")

    assert read_json_file("data/empty_file.json") == []

    # Удаление тестового файла
    os.remove("data/empty_file.json")
