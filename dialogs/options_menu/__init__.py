from aiogram_dialog import Dialog

from dialogs.options_menu import windows


def options_menu_dialogs():
    return Dialog(
        windows.start_window(),
        windows.options_menu_window(),
        windows.lines_window(),
        windows.stations_window(),
        windows.time_window(),
        windows.rooms_window(),
        windows.price_window()
    )

