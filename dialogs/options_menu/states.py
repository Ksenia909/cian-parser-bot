from aiogram.fsm.state import State, StatesGroup


class MenuSG(StatesGroup):
    start = State()
    menu = State()

