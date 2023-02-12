from aiogram.dispatcher.filters.state import State, StatesGroup


class FSM_clear_db(StatesGroup):
    select = State()
    select_date = State()
    select_all = State()
    confirm_date = State()
    confirm_all = State()
