from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from dialogs.options_menu.constants import MENU_BUTTON_STATES, IMAGE_LINKS
from dialogs.options_menu.states import MenuSG
from lexicon.lexicon import TEXT_OF_WINDOWS


async def start_menu(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=MenuSG.menu)


async def selected_option(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    if callback.data in MENU_BUTTON_STATES:
        await dialog_manager.switch_to(state=MENU_BUTTON_STATES[callback.data])
    elif callback.data == 'start_search':
        await callback.message.answer_photo(
            photo=IMAGE_LINKS['start_search'],
            caption=TEXT_OF_WINDOWS['start_search']
        )


