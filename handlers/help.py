from aiogram.types import Message
from loader import dp

from filters import IsAdmin

from utils.misc import rate_limit
from loader import await_time


@dp.message_handler(IsAdmin(), text="/help")
async def command_help(message: Message):
    await message.answer("Чтобы открыть панель администратора отправьте /admin")


@rate_limit(limit=await_time, key="/help")
@dp.message_handler(text="/help")
async def command_help(message: Message):
    await message.answer("Бот находится в разработке")