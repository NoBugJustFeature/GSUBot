from aiogram.types import Message
from loader import dp

from keyboards.admin_keyboards.keyboard_db import kb_db
from filters import IsAdmin


@dp.message_handler(IsAdmin(), text=["Работа с БД"])
async def command_start(message: Message):
    await message.answer("Выберете что хотите сделать", reply_markup=kb_db)