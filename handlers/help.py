from aiogram.types import Message
from loader import dp

from filters import IsAdmin


@dp.message_handler(IsAdmin(), text="/help")
async def command_help(message: Message):
    await message.answer("Чтобы открыть панель администратора отправьте /admin")


@dp.message_handler(text="/help")
async def command_help(message: Message):
    await message.answer("Бот находится в разработке")