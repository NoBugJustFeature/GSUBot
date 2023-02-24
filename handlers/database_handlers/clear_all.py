from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp

from filters import IsAdmin
from FSM.state_clear_db import FSM_clear_db

from keyboards.admin_keyboards.keyboard_db import kb_db
from keyboards.cancel import kb_cancel

from database.clear_all import clear_all_db

#for confirm
from random import randrange


#cancel
@dp.message_handler(state=[FSM_clear_db.select, FSM_clear_db.confirm_all], text="Отмена")
async def cancel(message: Message, state=FSMContext):
    await message.answer(f"Отменено", reply_markup=kb_db)
    await state.finish()


@dp.message_handler(IsAdmin(), state=FSM_clear_db.select, text="Очистить всё")
async def confirm(message: Message, state=FSMContext):

    global key
    key = "{:03}".format(randrange(0, 10**3))

    await FSM_clear_db.confirm_all.set()
    await message.answer(f"Подтвердите действие\nВведите следующий код: {key}",
                        reply_markup=kb_cancel)


@dp.message_handler(IsAdmin(), state=FSM_clear_db.confirm_all)
async def finish(message: Message, state=FSMContext):
    if key == str(message.text):
        await clear_all_db()
        await message.answer("БД очищена", reply_markup=kb_db)
        await state.finish()
    else:
        await message.answer("Неверный код\nПовторите попытку", reply_markup=kb_cancel)