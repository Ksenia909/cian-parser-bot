from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from dialogs.options_menu.states import MenuSG

router = Router()


@router.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=MenuSG.start, mode=StartMode.RESET_STACK)


# @router.message(Command(commands='menu'))
# async def command_menu_process(message: Message, dialog_manager: DialogManager):
#     await dialog_manager.switch_to(state=MenuSG.menu)

