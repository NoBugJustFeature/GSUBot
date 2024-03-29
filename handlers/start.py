from aiogram.types import Message
from loader import dp

from filters import IsAdmin
from keyboards.user_keyboards.keyboard_start import kb_start
from keyboards.admin_keyboards.keyboard_admin import kb_admin

from utils.misc import rate_limit
from loader import await_time


@dp.message_handler(IsAdmin(), text="/start")
async def command_start(message: Message):
    await message.answer(f"Здравствуйте, {message.from_user.first_name}",
                          reply_markup=kb_admin)
    

@rate_limit(limit=await_time, key="/start")
@dp.message_handler(text="/start")
async def command_start(message: Message):
    await message.answer(f"Привет!\n"
                          "Напишите боту /testing и узнаете где и когда у вас РТ\n"
                          "(списки обновляются вечером за день до тестирования)",
                          reply_markup=kb_start)