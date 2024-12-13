

from telegram import Update
from telegram.ext import ContextTypes
from src.db.database import database
from src.db.models import Message
from src.utils.keywords import get_keywords, add_keyword, remove_keyword

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я собираю сообщения по ключевым словам.")

async def add_keyword_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Укажите ключевое слово для добавления.")
        return
    keyword = " ".join(context.args)
    await add_keyword(keyword)
    await update.message.reply_text(f"Ключевое слово '{keyword}' добавлено.")

async def remove_keyword_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Укажите ключевое слово для удаления.")
        return
    keyword = " ".join(context.args)
    await remove_keyword(keyword)
    await update.message.reply_text(f"Ключевое слово '{keyword}' удалено.")

async def list_keywords_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keywords = await get_keywords()
    if keywords:
        await update.message.reply_text("Ключевые слова:\n" + "\n".join(keywords))
    else:
        await update.message.reply_text("Список ключевых слов пуст.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    session = SessionLocal()
    message_text = update.message.text.lower()
    keywords = await get_keywords()

    if any(keyword in message_text for keyword in keywords):
        new_message = Message(
            chat_id=str(update.message.chat_id),
            username=update.message.from_user.username,
            message_text=update.message.text,
        )
        session.add(new_message)
        session.commit()
    session.close()


async def edit_keyword_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text(
            "Использование: /edit_keyword <старое_слово> <новое_слово>"
        )
        return
    old_word, new_word = context.args[0], " ".join(context.args[1:])
    await edit_keyword(old_word, new_word)
    await update.message.reply_text(f"Ключевое слово '{old_word}' изменено на '{new_word}'.")

# Обновленный список доступных команд
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    commands = (
        "/add_keyword <слово> — добавить ключевое слово.\n"
        "/remove_keyword <слово> — удалить ключевое слово.\n"
        "/edit_keyword <старое_слово> <новое_слово> — изменить ключевое слово.\n"
        "/list_keywords — список всех ключевых слов."
    )
    await update.message.reply_text(f"Доступные команды:\n{commands}")

