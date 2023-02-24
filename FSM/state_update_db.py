from aiogram.dispatcher.filters.state import State, StatesGroup


class FSM_update_db(StatesGroup):
    select = State()
    select_send = State()

    #the second way is to download from the site without a special state