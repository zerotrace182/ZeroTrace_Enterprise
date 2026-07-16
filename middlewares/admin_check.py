from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable
import os

class AdminMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        
        # ROOT OWNER ID من ملف .env
        root_id = int(os.getenv("ROOT_OWNER_ID"))
        
        # فحص إذا كان المستخدم هو المالك
        if event.from_user.id == root_id:
            return await handler(event, data)
        
        # إذا لم يكن المالك، يتم تجاهل الرسالة (أو يمكنك إرسال رسالة خطأ)
        return
      
