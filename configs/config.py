# /home/bot/projects/bot_news/configs/config.py

# Токен Telegram-бота
BOT_TOKEN = "7778409248:AAH5-jsD0ohwn6BtBNbu575t5TnLaZFjiwk"

# Интервал обновления кэша (в секундах)
CACHE_UPDATE_INTERVAL = 60

# Настройки базы данных PostgreSQL
DATABASE_URL = "postgresql+asyncpg://botnews:password@localhost:5432/bot_news"

# Логирование
LOG_FILE = "/home/bot/projects/bot_news/logs/bot_news.log"
LOG_LEVEL = "INFO"
