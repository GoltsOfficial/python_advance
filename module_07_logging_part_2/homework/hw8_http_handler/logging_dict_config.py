import logging
import string


class ASCIIFilter(logging.Filter):
    def filter(self, record):
        """Фильтрует сообщения, содержащие не-ASCII символы"""
        message = record.getMessage()
        return message.isascii()


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'filters': {
        'ascii_filter': {
            '()': ASCIIFilter,
        }
    },

    'formatters': {
        'standard': {
            'format': '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },

    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'filters': ['ascii_filter'],
            'stream': 'ext://sys.stdout'
        },
        'debug_file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'filters': ['ascii_filter'],
            'filename': 'calc_debug.log'
        },
        'info_file': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'filters': ['ascii_filter'],
            'filename': 'calc_info.log'
        },
        'warning_file': {
            'class': 'logging.FileHandler',
            'level': 'WARNING',
            'formatter': 'standard',
            'filters': ['ascii_filter'],
            'filename': 'calc_warning.log'
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'standard',
            'filters': ['ascii_filter'],
            'filename': 'calc_error.log'
        },
        'critical_file': {
            'class': 'logging.FileHandler',
            'level': 'CRITICAL',
            'formatter': 'standard',
            'filters': ['ascii_filter'],
            'filename': 'calc_critical.log'
        },
        'utils_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'filters': ['ascii_filter'],
            'filename': 'utils.log',
            'when': 'H',
            'interval': 10,
            'backupCount': 1,
        }
    },

    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['stdout', 'debug_file', 'info_file', 'warning_file', 'error_file', 'critical_file']
        },
        'utils': {
            'level': 'INFO',
            'handlers': ['utils_file'],
            'propagate': False
        }
    }
}

# Альтернативная версия is_ascii
def is_ascii(text):
    """Проверяет, содержит ли строка только ASCII символы"""
    try:
        text.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False

# Ручная проверка is_ascii
def is_ascii_manual(text):
    """Ручная проверка ASCII символов"""
    return all(ord(char) < 128 for char in text)