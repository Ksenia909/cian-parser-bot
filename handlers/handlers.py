from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from sqlalchemy.ext.asyncio import AsyncSession

from db.requests import merge_or_create_user
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
    await dialog_manager.start(state=MenuSG.start, mode=StartMode.RESET_STACK)


