from aiogram_dialog import Dialog

from dialogs.options_menu import windows


def options_menu_dialogs():
    return Dialog(
        windows.start_window(),
        windows.options_menu_window()
    )

