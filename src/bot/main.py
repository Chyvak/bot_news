import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from src.bot.handlers import (
    start, add_keyword_command, remove_keyword_command,
    list_keywords_command, handle_message
)
from src.db.database import database, init_db

async def main():
    init_db()
    await database.connect()

    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add_keyword", add_keyword_command))
    app.add_handler(CommandHandler("remove_keyword", remove_keyword_command))
    app.add_handler(CommandHandler("list_keywords", list_keywords_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен.")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())


from src.bot.handlers import (
    start, add_keyword_command, remove_keyword_command,
    list_keywords_command, edit_keyword_command, help_command
)

async def main():
    init_db()
    await database.connect()

    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("add_keyword", add_keyword_command))
    app.add_handler(CommandHandler("remove_keyword", remove_keyword_command))
    app.add_handler(CommandHandler("edit_keyword", edit_keyword_command))
    app.add_handler(CommandHandler("list_keywords", list_keywords_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен.")
    await app.run_polling()

