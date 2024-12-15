from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from src.utils.keywords import get_keywords, add_keyword, remove_keyword, edit_keyword
from src.utils.channels import add_channel, remove_channel
from src.utils.messages import export_messages_to_csv
# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Добавить ключевое слово", callback_data="add_keyword")],
        [InlineKeyboardButton("Удалить ключевое слово", callback_data="remove_keyword")],
        [InlineKeyboardButton("Добавить канал", callback_data="add_channel")],
        [InlineKeyboardButton("Удалить канал", callback_data="remove_channel")],
        [InlineKeyboardButton("Экспорт данных", callback_data="export_data")],
        [InlineKeyboardButton("Помощь", callback_data="help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Добро пожаловать! Выберите действие:", reply_markup=reply_markup
    )
# Обработчик кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Подтверждаем нажатие кнопки

    if query.data == "add_keyword":
        await query.message.reply_text("Введите ключевое слово для добавления.")
    elif query.data == "remove_keyword":
        await query.message.reply_text("Введите ключевое слово для удаления.")
    elif query.data == "add_channel":
        await query.message.reply_text("Введите ID канала для добавления.")
    elif query.data == "remove_channel":
        await query.message.reply_text("Введите ID канала для удаления.")
    elif query.data == "export_data":
        file_path = await export_messages_to_csv()
        await query.message.reply_text(f"Данные экспортированы в файл: {file_path}")
    elif query.data == "help":
        await help_command(query.message, context)
# Добавление ключевого слова
async def add_keyword_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Укажите ключевое слово для добавления.")
        return
    keyword = " ".join(context.args)
    await add_keyword(keyword)
    await update.message.reply_text(f"Ключевое слово '{keyword}' добавлено.")
# Удаление ключевого слова
async def remove_keyword_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Укажите ключевое слово для удаления.")
        return
    keyword = " ".join(context.args)
    await remove_keyword(keyword)
    await update.message.reply_text(f"Ключевое слово '{keyword}' удалено.")
# Помощь
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    commands = (
        "/add_keyword <слово> — добавить ключевое слово.\n"
        "/remove_keyword <слово> — удалить ключевое слово.\n"
        "/edit_keyword <старое_слово> <новое_слово> — изменить ключевое слово.\n"
        "/list_keywords — список всех ключевых слов.\n"
        "/add_channel <ID> <имя> — добавить канал.\n"
        "/remove_channel <ID> — удалить канал.\n"
        "/start — показать меню с кнопками.\n"
        "/help — показать описание всех команд.\n"
        "/export_data — экспортировать данные в CSV."
    )
    await update.message.reply_text(f"Доступные команды:\n{commands}")
async def add_channel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Укажите ID канала для добавления.")
        return

    chat_id = int(context.args[0])
    name = " ".join(context.args[1:]) if len(context.args) > 1 else None
    await add_channel(chat_id, name)
    await update.message.reply_text(f"Канал с ID {chat_id} добавлен.")
async def remove_channel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Укажите ID канала для удаления.")
        return

    chat_id = int(context.args[0])
    await remove_channel(chat_id)
    await update.message.reply_text(f"Канал с ID {chat_id} удален.")
