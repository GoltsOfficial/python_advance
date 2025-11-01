import logging
import logging.config
import logging_tree
import os

try:
    from logging_dict_config import LOGGING_CONFIG

    logging.config.dictConfig(LOGGING_CONFIG)

    root_logger = logging.getLogger()
    utils_logger = logging.getLogger('utils')
    main_logger = logging.getLogger('app')

    root_logger.debug("Тест корневого логгера")
    utils_logger.info("Тест utils логгера")
    main_logger.warning("Тест app логгера")

except ImportError:
    logging.basicConfig(level=logging.DEBUG)

    logger1 = logging.getLogger('app')
    logger2 = logging.getLogger('utils')
    logger1.info("Тест app")
    logger2.warning("Тест utils")

tree_structure = logging_tree.format.build_description()

with open('logging_tree.txt', 'w', encoding='utf-8') as f:
    f.write(tree_structure)

print("Дерево ВСЕХ логгеров записано в logging_tree.txt")

logging.shutdown()

calc_files_to_cleanup = [
    'calc_debug.log', 'calc_info.log', 'calc_warning.log',
    'calc_error.log', 'calc_critical.log', 'utils.log'
]

for log_file in calc_files_to_cleanup:
    if os.path.exists(log_file):
        os.remove(log_file)
        print(f"Удален временный файл: {log_file}")

print("Самоочистка завершена. Остался только logging_tree.txt")