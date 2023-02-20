from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_db = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Обновить БД"),
        ],
        [
            KeyboardButton(text="Очистить БД"),
        ],
        [
            KeyboardButton(text="Отмена"),
        ]
    ],
    resize_keyboard=True
)