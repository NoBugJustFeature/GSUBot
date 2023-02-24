from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp

from filters import IsAdmin
from FSM.state_clear_db import FSM_clear_db

from keyboards.admin_keyboards.keyboard_admin import kb_admin
from keyboards.cancel import kb_cancel
from keyboards.admin_keyboards.keyboard_select_date import update_date_list

from database.clear_by_date import clear_by_date_db

#for confirm
from random import randrange


#cancel
@dp.message_handler(state=[FSM_clear_db.select, FSM_clear_db.select_date, FSM_clear_db.confirm_date], text="Отмена")
async def cancel(message: Message, state=FSMContext):
    await message.answer(f"Отменено", reply_markup=kb_admin)
    await state.finish()


@dp.message_handler(IsAdmin(), state=FSM_clear_db.select, text="Очистить по дате")
async def select_date(message: Message, state=FSMContext):
    await FSM_clear_db.select_date.set()
    #for update keyboard
    kb_select_date = update_date_list()
    await message.answer(f"Выберите дату из списка", 
                        reply_markup=kb_select_date)


@dp.message_handler(IsAdmin(), state=FSM_clear_db.select_date)
async def confirm(message: Message, state=FSMContext):

    global key
    key = "{:03}".format(randrange(0, 10**3))

    await FSM_clear_db.confirm_date.set()
    await message.answer(f"Подтвердите действие\nВведите следующий код: {key}",
                        reply_markup=kb_cancel)

    global date
    date = message.text


@dp.message_handler(IsAdmin(), state=FSM_clear_db.confirm_date)
async def finish(message: Message, state=FSMContext):
    if key == str(message.text):
        await clear_by_date_db(date)
        await message.answer(f"БД очищена по дате: {date}", reply_markup=kb_admin)
    else:
        await message.answer("Неверный код\nПовторите попытку", reply_markup=kb_cancel)
    await state.finish()