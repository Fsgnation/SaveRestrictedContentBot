#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("BQAlPCVPPqT7TnqWFajHJjFMTAkiaALLlKDqMjsHSntkDkkn5EDUXSfgL03TW5TWUEVOs8c2Uyet6Iu4vDLykwC6eNhCSOM7nk-CmVY8dHCMeOu0_IWYHR9pRcg5wrC2zP0Fwi4cC28rN_29wmjkHt8BK-EfnLqGGC6eC0NdM6JJfuZ5UxsAiEjpmCEwT82mrtLdarSdN8FbOPW84M3XwmoHrlp4-uOOzVPsM-bqZgn1oqnW7DGTETWnu4S9mzZtl_8Lem6F-lykNIh72LFBKs8aGGRTXqhimsylPqRd2255JRbZmo2i9X5-RG-qomNl4ewXJZhGGYSHMgW7Pwp3OFAAAAAXbpQSMA", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
