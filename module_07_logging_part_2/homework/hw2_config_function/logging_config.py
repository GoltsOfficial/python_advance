"""Стандартное логирование для всех файлов в папке"""

import logging
import sys

def setup_logging():
    """
    Переводит логи в формат: уровень | логгер | время | номер строки | сообщение
    """
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    # Хэндлеры для stdout
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    # Конфигурация root
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(handler)