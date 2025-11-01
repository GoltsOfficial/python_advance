LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

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
            'stream': 'ext://sys.stdout'
        },
        'debug_file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'filename': 'calc_debug.log'
        },
        'info_file': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'filename': 'calc_info.log'
        },
        'warning_file': {
            'class': 'logging.FileHandler',
            'level': 'WARNING',
            'formatter': 'standard',
            'filename': 'calc_warning.log'
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'standard',
            'filename': 'calc_error.log'
        },
        'critical_file': {
            'class': 'logging.FileHandler',
            'level': 'CRITICAL',
            'formatter': 'standard',
            'filename': 'calc_critical.log'
        }
    },

    'utils_file': {
                '()': 'logging.handlers.TimedRotatingFileHandler',
                'level': 'INFO',
                'formatter': 'standard',
                'filename': 'utils.log',
                'when': 'H',
                'interval': 10,
                'backupCount': 1,
    },

    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': [
                'stdout',
                'debug_file',
                'info_file',
                'warning_file',
                'error_file',
                'critical_file'
            ]
        },
        'utils': {
            'level': 'INFO',
            'handlers': ['utils_file'],
            'propagate': False
        }
    }
}