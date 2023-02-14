from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp

from filters import IsAdmin
from FSM.state_clear_db import FSM_clear_db
from keyboards.admin_keyboards.keyboard_admin_panel import kb_admin
from keyboards.admin_keyboards.keyboard_select_clear import kb_select_clear
from keyboards.cancel import kb_cancel
from keyboards.admin_keyboards.keyboard_select_date import update_date_list

from utils.database.clear_all import clear_all_db
from utils.database.clear_by_date import clear_by_date_db


#cancel
@dp.message_handler(state=[FSM_clear_db.select, FSM_clear_db.select_date, FSM_clear_db.select_all], text="Отмена")
async def command_help(message: Message, state=FSMContext):
    await message.answer(f"Отменено", reply_markup=kb_admin)
    await state.finish()


@dp.message_handler(IsAdmin(), text="Очистить БД")
async def command_help(message: Message):
    await FSM_clear_db.select.set()
    await message.answer("Выберите способ", reply_markup=kb_select_clear)


#if clear by date
@dp.message_handler(IsAdmin(), state=FSM_clear_db.select, text="Очистить по дате")
async def command_help(message: Message, state=FSMContext):
    await FSM_clear_db.select_date.set()
    #for update keyboard
    kb_select_date = update_date_list()
    await message.answer(f"Выберите дату из списка", 
                        reply_markup=kb_select_date)


@dp.message_handler(IsAdmin(), state=FSM_clear_db.select_date)
async def command_help(message: Message, state=FSMContext):
    await FSM_clear_db.confirm_date.set()
    await message.answer(f"Подтвердите действие\nВведите следующую последовательность: {message.from_user.id}",
                        reply_markup=kb_cancel)

    global date
    date = message.text


@dp.message_handler(IsAdmin(), state=FSM_clear_db.confirm_date)
async def command_help(message: Message, state=FSMContext):
    if message.text == str(message.from_user.id):
        await clear_by_date_db(date)
        await message.answer(f"БД очищена по дате: {date}", reply_markup=kb_admin)
    else:
        await message.answer("Действие отменено", reply_markup=kb_admin)
    await state.finish()


#if clear all
@dp.message_handler(IsAdmin(), state=FSM_clear_db.select, text="Очистить всё")
async def command_help(message: Message, state=FSMContext):
    await FSM_clear_db.confirm_all.set()
    await message.answer(f"Подтвердите действие\nВведите следующую последовательность: {message.from_user.id}",
                        reply_markup=kb_cancel)


@dp.message_handler(IsAdmin(), state=FSM_clear_db.confirm_all)
async def command_help(message: Message, state=FSMContext):
    if message.text == str(message.from_user.id):
        await clear_all_db()
        await message.answer("БД очищена", reply_markup=kb_admin)
    else:
        await message.answer("Действие отменено", reply_markup=kb_admin)
    await state.finish()
