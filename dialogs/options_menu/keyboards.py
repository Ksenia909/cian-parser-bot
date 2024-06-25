import operator

from aiogram_dialog.widgets.kbd import Button, Column, ScrollingGroup, Select
from aiogram_dialog.widgets.text import Const, Format

from lexicon.lexicon import LEXICON_MENU


SCROLLING_HEIGHT = 6


def start_keyboards(on_click):
    return Button(
            text=Const('Начать настройки поиска'),
            id='options',
            on_click=on_click
        )


def menu_keyboards(on_click):
    return Column(*[
        Button(
            text=Const(text),
            id=id,
            on_click=on_click
        )
        for text, id in LEXICON_MENU.items()
    ])


def back_to_menu(on_click):
    return Button(
        text=Const('🔙️ Назад 🔙'),
        id='back',
        on_click=on_click)


def lines_keyboards(on_click):
    return ScrollingGroup(
        Select(
            Format('{item[0]}'),
            id='scroll_lines',
            item_id_getter=operator.itemgetter(1),
            items='lines',
            on_click=on_click
        ),
        id='lines_ids',
        width=1, height=SCROLLING_HEIGHT,
    )