from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from dialogs.options_menu import keyboards
from dialogs.options_menu.states import MenuSG
from dialogs.options_menu import selected as s


def start_window():
    return Window(
        # find image
        # add text
        # add button
        Const("test start"),
        keyboards.start_keyboards(s.start_menu),
        state=MenuSG.start
    )


def options_menu_window():
    return Window(
        # find image
        # add text
        # add button
        Const("test menu"),
        keyboards.menu_keyboards(s.selected_option),
        state=MenuSG.menu
    )


def lines_window():
    return Window(
        state=MenuSG.select_line
    )


def stations_window():
    return Window(
        state=MenuSG.select_station
    )


def time_window():
    return Window(
        state=MenuSG.select_time
    )


def rooms_window():
    return Window(
        state=MenuSG.select_rooms
    )


def price_window():
    return Window(
        state=MenuSG.select_price
    )


