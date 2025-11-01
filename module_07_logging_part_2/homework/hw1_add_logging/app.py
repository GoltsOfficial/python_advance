import sys
import logging
from utils import string_to_operator

# Инициализируем логгер
logger = logging.getLogger(__name__)


def calc(args):
    # Получаем входные данные
    logger.debug(f"Получаем аргументы: {args}")

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
        # Получаем первое значение
        logger.debug(f"Пробуем преобразовать первое значение: {num_1}")
    except ValueError as e:
        logger.error(f"Ошибка преобразования первого значения: {num_1}.\n"
                     f"Содержимое ошибки: {e}")

    try:
        num_2 = float(num_2)
        # Получаем второе значение
        logger.debug(f"Пробуем преобразовать второе значение: {num_2}")
    except ValueError as e:
        logger.error(f"Ошибка преобразования второго значения: {num_2}.\n"
                     f"Содержимое ошибки: {e}")

    operator_func = string_to_operator(operator)
    logger.debug(f"Получаем функцию оператора: {operator_func}")

    result = operator_func(num_1, num_2)
    logger.debug(f"Выполнение операции: {num_1} {operator} {num_2} = {result}")

    logger.info(f"Успешно выполнена операция: {num_1} {operator} {num_2} = {result}")


if __name__ == '__main__':
    logger.info(f"Запуск приложения!")
    # calc(sys.argv[1:])
    calc('2+3')
    logger.info(f"Остановка работы приложения!")
