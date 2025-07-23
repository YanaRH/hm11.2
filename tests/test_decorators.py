import pytest
from logger import log  # Импортируйте декоратор из вашего модуля

@log()
def success_function(x, y):
    return x + y

@log()
def error_function(x, y):
    return x / y  # Потенциальная ошибка при y = 0

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
    assert "error_function error: ZeroDivisionError" in captured.out
    assert "Inputs: args=(1, 0), kwargs={}" in captured.out

def test_file_logging(tmp_path):
    log_file = tmp_path / "test_log.txt"
    @log(filename=str(log_file))
    def function_to_log(x, y):
        return x + y

    function_to_log(4, 5)

    with open(log_file, "r") as f:
        logs = f.read()
    assert "Calling function_to_log with args=(4, 5)" in logs
    assert "function_to_log ok - result=9" in logs
