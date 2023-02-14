from aiogram.types import Message, ContentTypes
from aiogram.dispatcher import FSMContext

from loader import dp
from filters import IsAdmin
from FSM.state_update_db import FSM_update_db
from utils.database.pdf_to_db import update_db

from keyboards.admin_keyboards.keyboard_admin_panel import kb_admin
from keyboards.cancel import kb_cancel


@dp.message_handler(IsAdmin(), text="Обновить БД")
async def command_help(message: Message):
    await FSM_update_db.pdf_file.set()
    await message.answer("Отправьте pdf файл",reply_markup=kb_cancel)


@dp.message_handler(IsAdmin(), content_types=ContentTypes.DOCUMENT, state=FSM_update_db.pdf_file)
async def command_help(message: Message, state=FSMContext):
    if document := message.document:
        await document.download(
            destination_file=f"data\pdf\{document.file_name}"
        )
    await message.answer("Скачано!\nНачинаю обработку файла...")

    await update_db(f"data\pdf\{document.file_name}")

    await message.answer("БД обновлена")
    await state.finish()


@dp.message_handler(IsAdmin(), state=FSM_update_db.pdf_file, text="Отмена")
async def command_help(message: Message, state=FSMContext):
    await message.answer(f"Отменено", reply_markup=kb_admin)
    await state.finish()
