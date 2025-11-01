import logging
from typing import Union, Callable
from operator import sub, mul, truediv, add

from module_07_logging_part_2.homework.hw2_config_function.logging_config import setup_logging

# Инициализируем стандарт для форматирования логов
setup_logging()

# Инициализируем логгер
logger = logging.getLogger(__name__)

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

Numeric = Union[int, float]


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    if not isinstance(value, str):
        logger.error(f"wrong operator type: {value} (type: {type(value)})")
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        logger.error(f"wrong operator value: {value}")
        raise ValueError("wrong operator value")

    logger.debug(f"successfully converted operator: {value} -> {OPERATORS[value]}")
    return OPERATORS[value]
