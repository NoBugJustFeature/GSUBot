from aiogram.types import Message
from loader import dp

from filters import IsAdmin
from keyboards.user_keyboards.keyboard_start import kb_start


@dp.message_handler(IsAdmin(), text="/start")
async def command_start(message: Message):
    await message.answer(f"Здравствуйте, {message.from_user.first_name}\n"
                           "Напишите /admin чтобы войти в панель администратора",
                          reply_markup=kb_start)
    

@dp.message_handler(text="/start")
async def command_start(message: Message):
    await message.answer(f"Привет!\n"
                          "Напиши боту /testing и узнаешь где и когда у тебя РТ\n"
                          "(списки обновляются вечером за день до тестирования)",
                          reply_markup=kb_start)