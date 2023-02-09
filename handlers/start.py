from aiogram import types
from loader import dp

from filters import IsAdmin


@dp.message_handler(IsAdmin(), text="/start")
async def command_start(message: types.Message):
    await message.answer(f"Здравуствуйте, {message.from_user.first_name}")
    

@dp.message_handler(text="/start")
async def command_start(message: types.Message):
    await message.answer("Привет, напиши боту своё ФИО и узнаешь где и когда у тебя РТ")