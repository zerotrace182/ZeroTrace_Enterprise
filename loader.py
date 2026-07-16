import os
from aiogram import Bot, Dispatcher
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# تحميل البيانات من ملف .env
load_dotenv()

# تهيئة البوت
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# تهيئة قاعدة البيانات (MongoDB)
# نستخدم AsyncIOMotorClient لضمان سرعة البوت وعدم تجمد الأوامر
db_client = AsyncIOMotorClient(os.getenv("MONGO_URL"))
db = db_client.ZeroTrace_DB # اسم قاعدة بياناتك

