from src.db.database import database
from src.db.models import Keyword

async def get_keywords():
    query = "SELECT word FROM keywords"
    rows = await database.fetch_all(query)
    return [row["word"] for row in rows]

async def add_keyword(word: str):
    query = "INSERT INTO keywords (word) VALUES (:word) ON CONFLICT DO NOTHING"
    await database.execute(query, values={"word": word.lower()})

async def remove_keyword(word: str):
    query = "DELETE FROM keywords WHERE word = :word"
    await database.execute(query, values={"word": word.lower()})

async def edit_keyword(old_word: str, new_word: str):
    query = """
        UPDATE keywords
        SET word = :new_word
        WHERE word = :old_word
    """
    await database.execute(query, values={"old_word": old_word.lower(), "new_word": new_word.lower()})
