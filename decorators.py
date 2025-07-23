import functools
import logging
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования информации о выполнении функции.

    Записывает в лог информацию о вызове функции, включая её имя, аргументы, результат или ошибку, если она возникла.
    Если указан параметр `filename`, лог сохраняется в указанный файл; если нет — выводится в консоль.

    Args:
        filename (Optional[str]): Имя файла для сохранения лога. Если None, лог выводится в консоль.

    Returns:
        Callable: Обёрнутая функция с логированием.
    """

    def decorator(func: Callable) -> Callable:
        # Настройка логгера
        logger = logging.getLogger(func.__name__)
        handler = logging.FileHandler(filename) if filename else logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Логирование начала выполнения
            logger.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
            try:
                # Выполнение функции
                result = func(*args, **kwargs)
                # Логирование успешного завершения
                logger.info(f"{func.__name__} ok - result={result}")
                return result
            except Exception as e:
                # Логирование ошибки с аргументами
                logger.error(
                    f"{func.__name__} error: {type(e).__name__} - {str(e)}. Inputs: args={args}, kwargs={kwargs}")
                raise

        return wrapper

    return decorator
