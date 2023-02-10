from aiogram.types import Message, ContentTypes
from aiogram.dispatcher import FSMContext

from loader import dp
from filters import IsAdmin
from FSM.state_update_db import FSM_update_db


@dp.message_handler(IsAdmin(), text="Обновить БД")
async def command_help(message: Message):
    await FSM_update_db.pdf_file.set()
    await message.answer("Отправьте pdf файл")


@dp.message_handler(IsAdmin(), content_types=ContentTypes.DOCUMENT,state=FSM_update_db.pdf_file)
async def command_help(message: Message, state=FSMContext):
    if document := message.document:
        await document.download(
            destination_dir="data\pdf"
        )
    await message.answer("Скачано!")
    await state.finish()
