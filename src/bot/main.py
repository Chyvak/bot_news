import sys
import os
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from configs.config import BOT_TOKEN, LOG_FILE, LOG_LEVEL
from src.bot.handlers import (
    start, add_keyword_command, remove_keyword_command,
    add_channel_command, remove_channel_command, button_handler,
    help_command
)
# Добавляем корневую директорию проекта в PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
# Настройка логирования
log_dir = os.path.dirname(LOG_FILE)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=LOG_FILE,
    level=LOG_LEVEL,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add_keyword", add_keyword_command))
    app.add_handler(CommandHandler("remove_keyword", remove_keyword_command))
    app.add_handler(CommandHandler("add_channel", add_channel_command))
    app.add_handler(CommandHandler("remove_channel", remove_channel_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button_handler))  # Обработчик кнопок

    logger.info("Команды зарегистрированы. Ожидание сообщений...")
    print("Бот запущен.")
    app.run_polling()  # Здесь PTB сам управляет циклом событий

if __name__ == "__main__":
    main()
