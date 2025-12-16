"""
Обработчики команд Telegram бота
"""
from telegram import Update
from telegram.ext import ContextTypes
from ..utils.logger import log


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    user = update.effective_user
    log.info(f"User {user.id} (@{user.username}) started the bot")

    welcome_text = f"""
👋 Привет, {user.first_name}!

Я TeleDigest Bot - твой личный ассистент для чтения Telegram-каналов.

🎯 Что я буду уметь:
- Анализировать посты из твоих каналов
- Фильтровать спам и неважную информацию
- Создавать краткие саммари
- Присылать ежедневный дайджест

⚠️ Статус: Бот в разработке (Этап 2 из 6)

📋 Доступные команды:
/start - Начать работу
/help - Справка
/status - Статус разработки
    """

    await update.message.reply_text(welcome_text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /help"""
    log.info(f"User {update.effective_user.id} requested help")

    help_text = """
📖 Справка по командам

/start - Начать работу с ботом
/help - Показать эту справку
/status - Узнать статус разработки
    """

    await update.message.reply_text(help_text)


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /status"""
    log.info(f"User {update.effective_user.id} requested status")

    status_text = """
📊 Статус разработки TeleDigest Bot
    """

    await update.message.reply_text(status_text)


async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик текстовых сообщений (эхо)"""
    user_message = update.message.text
    log.debug(f"Received message from {update.effective_user.id}: {user_message}")

    response = f"🤖 Получил твоё сообщение: \"{user_message}\"\n\n"
    response += "Пока что я просто повторяю за тобой. "
    response += "Скоро научусь анализировать посты! 📊"

    await update.message.reply_text(response)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик ошибок"""
    log.error(f"Update {update} caused error: {context.error}")

    if update and update.effective_message:
        await update.effective_message.reply_text(
            "❌ Произошла ошибка. Попробуйте позже или используйте /help"
        )
