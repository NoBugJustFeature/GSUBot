from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Работа с БД"),
        ],
        [
            KeyboardButton(text="Тестирование"),
        ],
        [
            KeyboardButton(text="Колличество вызовов /testing"),
        ]
    ],
    resize_keyboard=True
)