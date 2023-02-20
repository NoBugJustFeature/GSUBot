from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Работа с БД"),
        ],
        [
            KeyboardButton(text="Тестирование"),
        ]
    ],
    resize_keyboard=True
)