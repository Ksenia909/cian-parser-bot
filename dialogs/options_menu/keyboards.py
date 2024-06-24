from aiogram_dialog.widgets.kbd import Button, Column
from aiogram_dialog.widgets.text import Const

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