from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Тестирование"),
        ]
    ],
    resize_keyboard=True
)