from aiogram.types import Message
from loader import dp

from filters import IsAdmin
from keyboards.user_keyboards.keyboard_start import kb_start
from keyboards.admin_keyboards.Keyboard_start_admin import kb_admin_start


@dp.message_handler(IsAdmin(), text="/start")
async def command_start(message: Message):
    await message.answer(f"Здравствуйте, {message.from_user.first_name}\n"
                           "Напишите /admin чтобы войти в панель администратора",
                          reply_markup=kb_admin_start)
    

@dp.message_handler(text="/start")
async def command_start(message: Message):
    await message.answer(f"Привет!\n"
                          "Напишите боту /testing и узнаете где и когда у вас РТ\n"
                          "(списки обновляются вечером за день до тестирования)",
                          reply_markup=kb_start)