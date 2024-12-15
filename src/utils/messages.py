from sqlalchemy import select
from src.db.database import database
from src.db.models import Message
import pandas as pd
# Проверка на дублирование сообщения
async def is_duplicate_message(chat_id: str, message_text: str):
    query = select(Message).where(
        Message.chat_id == chat_id,
        Message.message_text == message_text
    )
    result = await database.fetch_one(query)
    return result is not None
# Экспорт сообщений в CSV
async def export_messages_to_csv():
    query = "SELECT * FROM messages"
    rows = await database.fetch_all(query)
    df = pd.DataFrame(rows)
    file_path = "/home/bot/projects/bot_news/data/messages.csv"
    df.to_csv(file_path, index=False)
    return file_path
# Очистка таблицы сообщений
async def clear_messages_table():
    query = "DELETE FROM messages"
    await database.execute(query)
