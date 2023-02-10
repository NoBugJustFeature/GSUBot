from aiogram.dispatcher.filters.state import State, StatesGroup


class FSM_update_db(StatesGroup):
    pdf_file = State()