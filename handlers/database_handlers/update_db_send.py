from aiogram.types import Message, ContentTypes
from aiogram.dispatcher import FSMContext

from loader import dp
from filters import IsAdmin
from FSM.state_update_db import FSM_update_db
from database.pdf_to_db import update_db

from keyboards.admin_keyboards.keyboard_update_db import kb_update_db
from keyboards.cancel import kb_cancel

from loader import path


@dp.message_handler(IsAdmin(), state=FSM_update_db.select_send, text="Отмена")
async def cancel(message: Message, state=FSMContext):
    await message.answer(f"Отменено", reply_markup=kb_update_db)
    await state.finish()


@dp.message_handler(IsAdmin(), state=FSM_update_db.select, text="Отправить файл")
async def get_file(message: Message):
    await FSM_update_db.select_send.set()
    await message.answer("Отправьте pdf файл",reply_markup=kb_cancel)


@dp.message_handler(IsAdmin(), content_types=ContentTypes.DOCUMENT, state=FSM_update_db.select_send)
async def update(message: Message, state=FSMContext):
    if document := message.document:
        await document.download(destination_file=path)

    await message.answer("Скачано!\nНачинаю обработку файла...")

    await update_db(path)

    await message.answer("БД обновлена", reply_markup=kb_update_db)
    await state.finish()