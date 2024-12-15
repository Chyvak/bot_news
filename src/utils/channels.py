from src.db.database import database

async def get_channels():
    query = "SELECT chat_id FROM channels"
    rows = await database.fetch_all(query)
    return [int(row["chat_id"]) for row in rows]

async def add_channel(chat_id: int, name: str = None):
    query = "INSERT INTO channels (chat_id, name) VALUES (:chat_id, :name) ON CONFLICT DO NOTHING"
    await database.execute(query, values={"chat_id": chat_id, "name": name})

async def remove_channel(chat_id: int):
    query = "DELETE FROM channels WHERE chat_id = :chat_id"
    await database.execute(query, values={"chat_id": chat_id})

