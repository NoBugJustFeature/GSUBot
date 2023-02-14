from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.database.kb_get_date import get_date


#for update keyboard
def update_date_list() -> ReplyKeyboardMarkup:
    lst = get_date()
    kb = [[KeyboardButton(text=i[0])] for i in lst]

    kb.append(["Отмена"])

    kb_select_date = ReplyKeyboardMarkup(keyboard=kb, 
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

    return kb_select_date
    

kb_select_date = update_date_list()