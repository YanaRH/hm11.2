import pytest


def success_function(x, y):
    print(f"Calling success_function with args=({x}, {y})")  # Добавлен вывод
    result = x + y
    print(f"success_function ok - result={result}")  # Добавлен вывод
    return result


def error_function(x, y):
    try:
        result = x / y
        print(f"error_function ok - result={result}")  # Добавлен вывод
        return result
    except ZeroDivisionError:
        print("error_function error: division by zero")  # Изменено сообщение об ошибке
        raise


def test_success_function(capsys):
    result = success_function(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    assert "Calling success_function with args=(2, 3)" in captured.out
    assert "success_function ok - result=5" in captured.out


def test_error_function(capsys):
    with pytest.raises(ZeroDivisionError):
        error_function(1, 0)
    captured = capsys.readouterr()
    assert "error_function error: division by zero" in captured.out  # Проверка на сообщение об ошибке


def test_file_logging(tmp_path):
    log_file = tmp_path / "test_log.txt"

    def function_to_log(x, y):
        result = x + y
        with open(log_file, "a") as log_file_handle:  # Изменено имя переменной
            log_file_handle.write(f"function_to_log called with args=({x}, {y}), result={result}\n")
        return result

    # Вызов функции и проверка логирования
    function_to_log(4, 5)

    # Проверка содержимого лог-файла
    with open(log_file) as log_file_handle:  # Изменено имя переменной
        log_contents = log_file_handle.read()
    assert "function_to_log called with args=(4, 5), result=9" in log_contents





