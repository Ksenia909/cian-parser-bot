from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button, ManagedMultiselect

from cian.metro import METRO
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


async def selected_back_to_menu(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=MenuSG.menu)


async def selected_line(callback: CallbackQuery, button: Button, dialog_manager: DialogManager, item_id: str):
    dialog_manager.current_context().dialog_data.update(line=item_id)
    await dialog_manager.switch_to(state=MenuSG.select_station)


async def selected_station(callback: CallbackQuery, checkbox: ManagedMultiselect, *args, **kwargs):
    if callback.data.split(':')[-1] == 'back_to_menu':
        stations = checkbox.get_checked()[:-1]
        if stations:
            data = checkbox.manager.current_context().dialog_data
            metro = data.setdefault('metro', dict())

            name_line = list(METRO.keys())[int(data['line'])]
            name_stations = [
                list(METRO[name_line].keys())[int(num)]
                for num in stations
            ]
            metro[name_line] = name_stations
        await checkbox.reset_checked()
        await checkbox.manager.back()


async def selected_time(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, time: str):
    if time.isdigit():
        data = dialog_manager.current_context().dialog_data
        data['time'] = time
        await message.answer(f'Время до метро: {time} минут')
        await dialog_manager.switch_to(state=MenuSG.menu)
    else:
        await message.answer_photo(
            photo=IMAGE_LINKS['error'],
            caption='Введите целое число')


async def selected_rooms(callback: CallbackQuery, checkbox: ManagedMultiselect, *args, **kwargs):
    if callback.data.split(':')[-1] == 'back_to_menu':
        rooms = checkbox.get_checked()[:-1]
        if rooms:
            data = checkbox.manager.current_context().dialog_data
            data['rooms'] = rooms
        await checkbox.reset_checked()
        await checkbox.manager.switch_to(state=MenuSG.menu)


