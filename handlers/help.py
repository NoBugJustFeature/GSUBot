from aiogram import types
from loader import dp

from filters import IsAdmin


@dp.message_handler(IsAdmin(), text="/help")
async def command_start(message: types.Message):
    await message.answer("Возможности администратора:\n"
                         "1) Обновлять БД (отправьте pdf)")


@dp.message_handler(text="/help")
async def command_start(message: types.Message):
    await message.answer("Бот находится в разработке")