from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from sqlalchemy.ext.asyncio import AsyncSession

from db.requests import merge_or_create_user, merge_or_create_user_last_link
from dialogs.options_menu.states import MenuSG

router = Router()


@router.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager, session: AsyncSession):
    await merge_or_create_user(
        session=session,
        telegram_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    await merge_or_create_user_last_link(
        session=session,
        telegram_id=message.from_user.id,
        last_link=''
    )
    apscheduler = dialog_manager.middleware_data['apscheduler']
    if apscheduler.get_job(str(dialog_manager.event.from_user.id)) is not None:
        apscheduler.remove_job(str(dialog_manager.event.from_user.id))

    await dialog_manager.start(state=MenuSG.start, mode=StartMode.RESET_STACK)


@router.message(Command(commands='stop'))
async def command_menu_process(message: Message, dialog_manager: DialogManager):
    apscheduler = dialog_manager.middleware_data['apscheduler']
    if apscheduler.get_job(str(dialog_manager.event.from_user.id)) is not None:
        apscheduler.remove_job(str(dialog_manager.event.from_user.id))

    await message.answer('Поиск остановлен!')

