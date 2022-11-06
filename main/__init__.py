from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID","3335796", default=None, cast=int)
API_HASH = config("API_HASH","138b992a0e672e8346d8439c3f42ea78", default=None)
BOT_TOKEN = config("BOT_TOKEN","5002292255:AAG3EmBHEaTPRxW8hZ797xuES-baLWm29Wo", default=None)
BOT_UN = config("BOT_UN","ir_convertbot", default=None)
AUTH_USERS = config("AUTH_USERS","763990585", default=None, cast=int)
LOG_CHANNEL = config("LOG_CHANNEL","wplus1", default=None)
LOG_ID = config("LOG_ID","-1001482606933", default=None)
FORCESUB = config("FORCESUB","-1001208480573", default=None)
FORCESUB_UN = config("FORCESUB_UN","seriesplus1", default=None)
ACCESS_CHANNEL = config("ACCESS_CHANNEL","default", default=None)
MONGODB_URI = config("MONGODB_URI","mongodb+srv://abirhasan2005:abirhasan@cluster0.lb2tp.mongodb.net/cluster0?retryWrites=true&w=majority", default=None)

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
