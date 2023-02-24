from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from filters import IsAdmin
from FSM.state_update_db import FSM_update_db
from database.pdf_to_db import update_db

from keyboards.admin_keyboards.keyboard_db import kb_db
from keyboards.cancel import kb_cancel

from loader import url, path
#for download file
import urllib.request


@dp.message_handler(IsAdmin(), state=FSM_update_db.select, text="Отмена")
async def cancel(message: Message, state=FSMContext):
    await message.answer(f"Отменено", reply_markup=kb_db)
    await state.finish()


@dp.message_handler(IsAdmin(), state=FSM_update_db.select, text="Скачать с сайта")
async def update_web(message: Message, state=FSMContext):
    try:
        urllib.request.urlretrieve(url, path)
    except Exception as exc:
        await message.answer(f"""Ошибка загрузки
                                 Обратитесь к системному администратору
                                 Ошибка: {exc}""")
    else:
        await update_db(path)
        await message.answer("БД обновлена", reply_markup=kb_db)
        await state.finish()