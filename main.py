import asyncio
import logging
from loader import dp, bot

# إعداد السجلات (عشان لو حصل خطأ تعرف وين المشكلة)
logging.basicConfig(level=logging.INFO)

async def main():
    print("ZeroTrace Bot Is Starting...")
    # هنا لاحقاً سنضيف الـ Routers (الوحدات) الخاصة بنا
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  
