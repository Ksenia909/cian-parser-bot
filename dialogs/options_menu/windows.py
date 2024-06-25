from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const

from dialogs.options_menu import keyboards
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
        Const("test menu"),
        StaticMedia(
            url=IMAGE_LINKS['options_menu'],
            type=ContentType.PHOTO
        ),
        keyboards.menu_keyboards(s.selected_option),
        state=MenuSG.menu
    )


def lines_window():
    return Window(
        StaticMedia(
            url=IMAGE_LINKS['lines'],
            type=ContentType.PHOTO
        ),
        state=MenuSG.select_line
    )


def stations_window():
    return Window(
        state=MenuSG.select_station
    )


def time_window():
    return Window(
        StaticMedia(
            url=IMAGE_LINKS['time'],
            type=ContentType.PHOTO
        ),
        state=MenuSG.select_time
    )


def rooms_window():
    return Window(
        StaticMedia(
            url=IMAGE_LINKS['rooms'],
            type=ContentType.PHOTO
        ),
        state=MenuSG.select_rooms
    )


def price_window():
    return Window(
        StaticMedia(
            url=IMAGE_LINKS['price'],
            type=ContentType.PHOTO
        ),
        Const(TEXT_OF_WINDOWS['time']),
        state=MenuSG.select_price
    )


