from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "22768571"))
API_HASH = getenv("API_HASH", "7d92204d9b502be216843739f70ded0e")

BOT_TOKEN = getenv("BOT_TOKEN", "7604555634:AAGWMfCKmcumls1Pr0y1QyqTDrUPKcqyHns")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://meyitzadee:Mytbot47@mytbot.a6b81.mongodb.net/?retryWrites=true&w=majority&appName=MytBot")

OWNER_ID = int(getenv("OWNER_ID", 7762430617))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/MytSohbet")
