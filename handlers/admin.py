from aiogram.types import Message
from loader import dp

from keyboards.admin_keyboards.keyboard_admin_panel import kb_start
from filters import IsAdmin


@dp.message_handler(IsAdmin(), text="/admin")
async def command_start(message: Message):
    await message.answer("Вы в панели", reply_markup=kb_start)