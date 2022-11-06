from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID","", default=None, cast=int)
API_HASH = config("API_HASH","", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_UN = config("BOT_UN","ir_convertbot", default=None)
AUTH_USERS = config("AUTH_USERS","763990585", default=None, cast=int)
LOG_CHANNEL = config("LOG_CHANNEL","-1001208480573", default=None)
LOG_ID = config("LOG_ID", default=None)
FORCESUB = config("FORCESUB","SeriesPlus1", default=None)
FORCESUB_UN = config("FORCESUB_UN", default=None)
ACCESS_CHANNEL = config("ACCESS_CHANNEL", default=None)
MONGODB_URI = config("MONGODB_URI","mongodb+srv://abirhasan2005:abirhasan@cluster0.lb2tp.mongodb.net/cluster0?retryWrites=true&w=majority", default=None)

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
