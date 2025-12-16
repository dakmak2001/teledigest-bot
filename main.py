"""
TeleDigest Bot - Главный файл
Этап 2: Простой Telegram бот
"""
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters
)

from src.utils.config import settings
from src.utils.logger import log
from src.bot.handlers import (
    start_command,
    help_command,
    status_command,
    echo_message,
    error_handler
)


def main():
    """Главная функция"""
    log.info("🚀 TeleDigest Bot - Starting...")
    log.info(f"📊 Debug mode: {settings.debug}")

    # Проверяем наличие токена
    try:
        settings.validate_bot_token()
        log.success("✅ Bot token found")
    except ValueError as e:
        log.error(str(e))
        return

    # Создаём приложение
    log.info("🔧 Creating bot application...")
    app = Application.builder().token(settings.bot_token).build()

    # Регистрируем обработчики
    log.info("📝 Registering command handlers...")
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("status", status_command))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message))
    app.add_error_handler(error_handler)

    log.success("✅ Bot configured successfully!")
    log.info("🤖 Starting polling... (Press Ctrl+C to stop)")
    log.info("💬 Open Telegram and send /start to your bot!")

    # ⚠️ ВАЖНО: БЕЗ await
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.info("👋 Bot stopped by user")
    except Exception as e:
        log.error(f"❌ Fatal error: {e}")
        raise
