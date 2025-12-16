"""
Настройка логирования
"""
import sys
from loguru import logger
from .config import settings


def setup_logger():
    """Настраивает логгер"""

    # Удаляем стандартный handler
    logger.remove()

    # Консольный вывод с цветами
    logger.add(
        sys.stdout,
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",
        level=settings.log_level,
        colorize=True
    )

    logger.info("Logger initialized")
    return logger


# Инициализируем при импорте
log = setup_logger()