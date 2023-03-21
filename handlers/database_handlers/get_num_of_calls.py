from aiogram.types import Message

from loader import dp

from filters import IsAdmin

from keyboards.admin_keyboards.keyboard_admin import kb_admin


@dp.message_handler(IsAdmin(), text="Колличество вызовов /testing")
async def choose(message: Message):
    from loader import num_of_calls
    await message.answer(f"{num_of_calls}", reply_markup=kb_admin)