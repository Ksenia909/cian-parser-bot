from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Format

from dialogs.options_menu import keyboards, getters
from dialogs.options_menu.constants import IMAGE_LINKS
from dialogs.options_menu.states import MenuSG
from dialogs.options_menu import selected as s
from lexicon.lexicon import TEXT_OF_WINDOWS


def start_window():
    return Window(
        Const(TEXT_OF_WINDOWS['start']),
        StaticMedia(
            url=IMAGE_LINKS['start'],
            type=ContentType.PHOTO
        ),
        keyboards.start_keyboards(s.start_menu),
        state=MenuSG.start
    )


def options_menu_window():
    return Window(
        StaticMedia(
            url=IMAGE_LINKS['options_menu'],
            type=ContentType.PHOTO
        ),
        Format(TEXT_OF_WINDOWS['menu']),
        keyboards.menu_keyboards(s.selected_option),
        getter=getters.get_menu,
        state=MenuSG.menu
    )


def lines_window():
    return Window(
        StaticMedia(
            url=IMAGE_LINKS['lines'],
            type=ContentType.PHOTO
        ),
        keyboards.lines_keyboards(s.selected_line),
        keyboards.back_to_menu(s.selected_back_to_menu),
        state=MenuSG.select_line,
        getter=getters.get_lines
    )


def stations_window():
    return Window(
        Format('Линия {name_line}'),
        keyboards.stations_keyboards(s.selected_station),
        keyboards.back_to_menu(s.selected_back_to_menu),
        getter=getters.get_stations,
        state=MenuSG.select_station
    )


def time_window():
    return Window(
        StaticMedia(
            url=IMAGE_LINKS['time'],
            type=ContentType.PHOTO
        ),
        Const(TEXT_OF_WINDOWS['time']),
        TextInput(
            id='time',
            on_success=s.selected_time
        ),
        keyboards.back_to_menu(s.selected_back_to_menu),
        state=MenuSG.select_time
    )


def rooms_window():
    return Window(
        StaticMedia(
            url=IMAGE_LINKS['rooms'],
            type=ContentType.PHOTO
        ),
        keyboards.rooms_keyboards(s.selected_rooms),
        keyboards.back_to_menu(s.selected_back_to_menu),
        getter=getters.get_rooms,
        state=MenuSG.select_rooms
    )


def price_window():
    return Window(
        StaticMedia(
            url=IMAGE_LINKS['price'],
            type=ContentType.PHOTO
        ),
        Const(TEXT_OF_WINDOWS['price']),
        TextInput(
            id='price',
            on_success=s.selected_price
        ),
        keyboards.back_to_menu(s.selected_back_to_menu),
        state=MenuSG.select_price
    )


