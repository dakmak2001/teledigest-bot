"""
TeleDigest Bot - Главный файл
Этап 1: Проверка базовой настройки
"""
from src.utils.config import settings
from src.utils.logger import log


def main():
    """Главная функция"""
    log.info("🚀 TeleDigest Bot - Starting...")
    log.info(f"📊 Debug mode: {settings.debug}")
    log.info(f"📝 Log level: {settings.log_level}")

    # Проверяем конфигурацию
    if settings.bot_token:
        log.success("✅ Bot token found")
    else:
        log.warning("⚠️  Bot token not configured yet")

    log.info("✅ Configuration loaded successfully!")
    log.info("📋 Next step: Create Telegram bot and add BOT_TOKEN to .env")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.info("👋 Stopped by user")
    except Exception as e:
        log.error(f"❌ Error: {e}")
        raise