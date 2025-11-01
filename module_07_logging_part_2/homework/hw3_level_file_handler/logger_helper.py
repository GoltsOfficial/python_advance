import logging
import sys


class LevelFileHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        #Создаём обработчики для каждого уровня
        self.level_files = {
            logging.DEBUG: 'calc_debug.log',
            logging.INFO: 'calc_info.log',
            logging.WARNING: 'calc_warning.log',
            logging.ERROR: 'calc_error.log',
            logging.CRITICAL: 'calc_critical.log',
        }

        self.handlers = {}
        formatter = logging.Formatter(
            '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        for level, filename in self.level_files.items():
            handler = logging.FileHandler(filename)
            handler.setLevel(level)
            handler.setFormatter(formatter)
            self.handlers[level] = handler

    def emit(self, record):
        """Отправляем запись в файл соответствующего уровня"""
        if record.levelno in self.level_files:
            self.handlers[record.levelno].emit(record)


def get_logger(name):
    # Создаем логгер
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Форматтер для всех обработчиков
    formatter = logging.Formatter(
        '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Обработчик для stdout
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)

    # Наш кастомный обработчик для файлов по уровням
    level_file_handler = LevelFileHandler()
    level_file_handler.setLevel(logging.DEBUG)

    # Добавляем обработчики к логгеру
    logger.addHandler(stdout_handler)
    logger.addHandler(level_file_handler)

    return logger

