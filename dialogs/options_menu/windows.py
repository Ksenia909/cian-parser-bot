from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const

from dialogs.options_menu.states import MenuSG


def start_window():
    return Window(
        # find image
        # add text
        # add button
        Const("test start"),
        state=MenuSG.start
    )


def options_menu_window():
    return Window(
        # find image
        # add text
        # add button
        Const("test menu"),
        state=MenuSG.menu
    )


def lines_window():
    return Window()


def stations_window():
    return Window()


def time_window():
    return Window()


def rooms_window():
    return Window()


def price_window():
    return Window()


