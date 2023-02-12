from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Обновить БД"),
        ],
        [
            KeyboardButton(text="Очистить БД"),
        ]
    ],
    resize_keyboard=True
)