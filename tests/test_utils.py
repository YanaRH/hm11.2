# tests/test_utils.py
import pytest
from src.utils import read_json_file

def test_read_json_file():
    assert read_json_file("data/operations.json") == []  # Пример для пустого или несуществующего файла