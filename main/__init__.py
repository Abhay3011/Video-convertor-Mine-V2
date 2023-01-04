#yo
from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=9544521, cast=int)
API_HASH = config("API_HASH", "5cf32e97dc94510e46524f2286c95116")
BOT_TOKEN = config("BOT_TOKEN", "5635132664:AAGoJCbGdLxyjmy1wB7UUTMpXUVv2O60dN8")
BOT_UN = config("BOT_UN", "dumpv4bot")

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
