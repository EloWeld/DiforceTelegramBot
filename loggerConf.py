# Создаем логгер
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Создаем обработчики файла для каждого уровня логирования
debug_handler = logging.FileHandler('botlog_debug.log')
info_handler = logging.FileHandler('botlog_info.log')
warning_handler = logging.FileHandler('botlog_warning.log')
error_handler = logging.FileHandler('botlog_error.log')

# Устанавливаем уровень логирования для каждого обработчика
debug_handler.setLevel(logging.DEBUG)
info_handler.setLevel(logging.INFO)
warning_handler.setLevel(logging.WARNING)
error_handler.setLevel(logging.ERROR)
        
# Создаем форматтер и добавляем его в обработчики
formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s')
debug_handler.setFormatter(formatter)
info_handler.setFormatter(formatter)
warning_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

# Добавляем обработчики в логгер
logger.addHandler(debug_handler)
logger.addHandler(info_handler)
logger.addHandler(warning_handler)
logger.addHandler(error_handler)