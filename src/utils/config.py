"""
Конфигурация приложения
"""
import os
from dotenv import load_dotenv

# Загружаем .env
load_dotenv()


class Settings:
    """Настройки приложения"""

    def __init__(self):
        # Базовые настройки
        self.debug = os.getenv("DEBUG", "false").lower() == "true"
        self.log_level = os.getenv("LOG_LEVEL", "INFO")

        # Telegram Bot
        self.bot_token = os.getenv("BOT_TOKEN", "")

        # Telegram API (добавим позже)
        self.telegram_api_id = os.getenv("TELEGRAM_API_ID", "")
        self.telegram_api_hash = os.getenv("TELEGRAM_API_HASH", "")
        self.telegram_phone = os.getenv("TELEGRAM_PHONE", "")

        # Groq AI (добавим позже)
        self.groq_api_key = os.getenv("GROQ_API_KEY", "")

    def validate_bot_token(self):
        """Проверяет наличие bot token"""
        if not self.bot_token:
            raise ValueError(
                "❌ BOT_TOKEN не найден в .env!\n"
                "Создайте бота через @BotFather и добавьте токен в .env"
            )
        return True

    def __repr__(self):
        return f"<Settings debug={self.debug} bot_configured={bool(self.bot_token)}>"


# Глобальный экземпляр
settings = Settings()