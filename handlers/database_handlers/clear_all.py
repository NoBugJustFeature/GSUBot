from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp

from filters import IsAdmin
from FSM.state_clear_db import FSM_clear_db

from keyboards.admin_keyboards.keyboard_admin import kb_admin
from keyboards.cancel import kb_cancel

from database.clear_all import clear_all_db


#cancel
@dp.message_handler(state=[FSM_clear_db.select, FSM_clear_db.confirm_all], text="Отмена")
async def cancel(message: Message, state=FSMContext):
    await message.answer(f"Отменено", reply_markup=kb_admin)
    await state.finish()


@dp.message_handler(IsAdmin(), state=FSM_clear_db.select, text="Очистить всё")
async def confirm(message: Message, state=FSMContext):
    await FSM_clear_db.confirm_all.set()
    await message.answer(f"Подтвердите действие\nВведите следующую последовательность: {message.from_user.id}",
                        reply_markup=kb_cancel)


@dp.message_handler(IsAdmin(), state=FSM_clear_db.confirm_all)
async def finish(message: Message, state=FSMContext):
    if message.text == str(message.from_user.id):
        await clear_all_db()
        await message.answer("БД очищена", reply_markup=kb_admin)
    else:
        await message.answer("Действие отменено", reply_markup=kb_admin)
    await state.finish()