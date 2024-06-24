from aiogram.fsm.state import State, StatesGroup


class MenuSG(StatesGroup):
    start = State()
    menu = State()
    select_line = State()
    select_station = State()
    select_time = State()
    select_rooms = State()
    select_price = State()

