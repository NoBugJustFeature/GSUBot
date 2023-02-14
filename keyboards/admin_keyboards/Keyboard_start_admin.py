from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_admin_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Открыть панель администратора"),
        ]
    ],
    resize_keyboard=True
)