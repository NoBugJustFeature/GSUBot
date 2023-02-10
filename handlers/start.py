from aiogram.types import Message
from loader import dp

from filters import IsAdmin


@dp.message_handler(IsAdmin(), text="/start")
async def command_start(message: Message):
    await message.answer(f"Здравствуйте, {message.from_user.first_name}\n"
                           "Напишите /admin чтобы войти в панель администратора")
    

@dp.message_handler(text="/start")
async def command_start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name.capitalize()}\n"
                          "Напиши боту своё ФИО и узнаешь где и когда у тебя РТ")