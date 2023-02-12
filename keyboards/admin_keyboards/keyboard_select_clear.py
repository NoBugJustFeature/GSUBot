from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.database.kb_get_date import get_date


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
lst = get_date()
kb = [[KeyboardButton(text=i)] for i in lst]

kb_select_date = ReplyKeyboardMarkup(keyboard=kb, 
                                     resize_keyboard=True,
                                     one_time_keyboard=True)