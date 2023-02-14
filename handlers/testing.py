from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from FSM.state_testing import FSM_testing
from utils.database.get_data import get_data

from keyboards.cancel import kb_cancel
from keyboards.user_keyboards.keyboard_start import kb_start
    

@dp.message_handler(text=["/testing", "Тестирование"])
async def command_start(message: Message):
    await FSM_testing.testing.set()
    await message.answer(f"Напиши своё ФИО (Иванов Иван Иванович", reply_markup=kb_cancel)


@dp.message_handler(state=FSM_testing.testing, text="Отмена")
async def command_help(message: Message, state=FSMContext):
    await message.answer(f"Отменено", reply_markup=kb_start)
    await state.finish()


@dp.message_handler(state=FSM_testing.testing)
async def command_help(message: Message, state=FSMContext):
    await get_data(message)
    await state.finish()