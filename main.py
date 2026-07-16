import asyncio
import logging
from loader import dp, bot
# 1. استيراد الموديلات والحارس
from modules.admin import admin_router
from middlewares.admin_check import AdminMiddleware

# إعداد السجلات
logging.basicConfig(level=logging.INFO)

async def main():
    print("ZeroTrace Enterprise System is Starting...")
    
    # 2. تفعيل الحارس (Middleware) على لوحة الأدمن فقط
    # هذا يضمن أن أوامر الأدمن محمية بـ ID الخاص بك فقط
    admin_router.message.middleware(AdminMiddleware())
    
    # 3. إدراج الموديلات في الـ Dispatcher
    dp.include_router(admin_router)
    
    # 4. تشغيل البوت
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
