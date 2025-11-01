# TODO переписать реализацию ini-файла в формате dict-конфигурации.
import configparser
import logging


def ini_to_dict(ini_file_path):
    """Конвертирует INI конфиг логирования в dict-конфиг"""

    config = configparser.ConfigParser()
    config.read(ini_file_path)

    dict_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {},
        'handlers': {},
        'loggers': {}
    }

    # Форматтеры
    if 'formatters' in config:
        for formatter_key in config['formatters']['keys'].split(','):
            section = f'formatter_{formatter_key}'
            dict_config['formatters'][formatter_key] = {
                'format': config[section]['format'],
                'datefmt': config[section]['datefmt']
            }

    # Обработчики
    if 'handlers' in config:
        for handler_key in config['handlers']['keys'].split(','):
            section = f'handler_{handler_key}'
            handler_config = {
                'class': config[section]['class'],
                'level': config[section]['level'],
                'formatter': config[section]['formatter']
            }

            # Обработка args
            args_str = config[section]['args']
            if args_str:
                # Безопасный eval для кортежа
                args = eval(args_str)
                if args:
                    if 'StreamHandler' in handler_config['class']:
                        handler_config['stream'] = args[0]
                    elif 'FileHandler' in handler_config['class']:
                        handler_config['filename'] = args[0]

            dict_config['handlers'][handler_key] = handler_config

    # Логгеры
    if 'loggers' in config:
        for logger_key in config['loggers']['keys'].split(','):
            section = f'logger_{logger_key}'
            logger_config = {
                'level': config[section]['level'],
                'handlers': config[section]['handlers'].split(',')
            }

            if 'propagate' in config[section]:
                logger_config['propagate'] = bool(int(config[section]['propagate']))
            if 'qualname' in config[section]:
                logger_config['qualname'] = config[section]['qualname']

            dict_config['loggers'][logger_key] = logger_config

    return dict_config


if __name__ == '__main__':
    dict_config = ini_to_dict('logging_conf.ini')

    # Применение конфигурации
    import logging.config

    logging.config.dictConfig(dict_config)

    # Тестирование
    root_logger = logging.getLogger()
    app_logger = logging.getLogger('appLogger')

    root_logger.debug("Root debug message")
    app_logger.info("App info message")
    app_logger.warning("App warning message")