from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_update_db = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить файл"),
        ],
        [
            KeyboardButton(text="Скачать с сайта"),
        ],
        [
            KeyboardButton(text="Отмена"),
        ]
    ],
    resize_keyboard=True
)