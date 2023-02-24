from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from filters import IsAdmin
from FSM.state_update_db import FSM_update_db

from keyboards.admin_keyboards.keyboard_db import kb_db
from keyboards.admin_keyboards.keyboard_update_db import kb_update_db
from keyboards.cancel import kb_cancel


@dp.message_handler(IsAdmin(), state=FSM_update_db.select, text="Отмена")
async def cancel(message: Message, state=FSMContext):
    await message.answer(f"Отменено", reply_markup=kb_db)
    await state.finish()


@dp.message_handler(IsAdmin(), text="Обновить БД")
async def select(message: Message):
    await FSM_update_db.select.set()
    await message.answer("Выберите способ", reply_markup=kb_update_db)
