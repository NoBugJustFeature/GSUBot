from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from FSM.state_testing import FSM_testing
from database.get_data import get_data

from filters import IsAdmin

from keyboards.cancel import kb_cancel
from keyboards.admin_keyboards.keyboard_admin import kb_admin
from keyboards.user_keyboards.keyboard_start import kb_start

from utils.misc import rate_limit
from loader import await_time


@dp.message_handler(IsAdmin(), state=FSM_testing.testing, text="Отмена")
async def cancel(message: Message, state=FSMContext):
    await message.answer(f"Отменено", reply_markup=kb_admin)
    await state.finish()
    

@dp.message_handler(state=FSM_testing.testing, text="Отмена")
async def cancel(message: Message, state=FSMContext):
    await message.answer(f"Отменено", reply_markup=kb_start)
    await state.finish()


@rate_limit(limit=await_time, key="/testing")
@dp.message_handler(text=["/testing", "Тестирование"])
async def command_testing(message: Message):
    await FSM_testing.testing.set()
    await message.answer(f"Напишите своё ФИО \n(Иванов Иван Иванович)", reply_markup=kb_cancel)


@dp.message_handler(state=FSM_testing.testing)
async def output_data(message: Message, state=FSMContext):
    await get_data(message)
    await state.finish()