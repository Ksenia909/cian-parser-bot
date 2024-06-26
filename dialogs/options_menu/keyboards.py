import operator

from aiogram_dialog.widgets.kbd import Button, Column, ScrollingGroup, Select, Multiselect
from aiogram_dialog.widgets.text import Const, Format

from dialogs.options_menu.constants import SCROLLING_HEIGHT
from lexicon.lexicon import LEXICON_MENU


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


def stations_keyboards(on_click):
    return ScrollingGroup(
        Multiselect(
            Format('☑{item[0]}'),
            Format('{item[0]}'),
            id='scroll_stations',
            item_id_getter=operator.itemgetter(1),
            items='stations',
            on_state_changed=on_click,
        ),
        id='stations_ids',
        width=1, height=SCROLLING_HEIGHT
    )


def rooms_keyboards(on_click):
    return Column(
        Multiselect(
            Format('☑{item[0]}'),
            Format('{item[0]}'),
            id='scroll_rooms',
            item_id_getter=operator.itemgetter(1),
            items='rooms',
            on_state_changed=on_click,
        ))


