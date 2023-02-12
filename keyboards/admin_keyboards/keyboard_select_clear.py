from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_select_clear = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Очистить всё"),
        ],
        [
            KeyboardButton(text="Очистить по дате"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)