from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp

from filters import IsAdmin
from FSM.state_clear_db import FSM_clear_db

from keyboards.admin_keyboards.keyboard_admin import kb_admin
from keyboards.admin_keyboards.keyboard_select_clear import kb_select_clear


#cancel
@dp.message_handler(text="Отмена")
async def command_help(message: Message, state=FSMContext):
    await message.answer(f"Отменено", reply_markup=kb_admin)
    await state.finish()


@dp.message_handler(IsAdmin(), text="Очистить БД")
async def command_help(message: Message):
    await FSM_clear_db.select.set()
    await message.answer("Выберите способ", reply_markup=kb_select_clear)