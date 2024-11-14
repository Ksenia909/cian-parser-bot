import asyncio

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from cian.parser import CianParser


async def parse_and_send_links(dialog_manager: DialogManager, callback: CallbackQuery, url: str):
    links = await CianParser(url=url).get_links()
    for link in links[::2]:
        await callback.message.answer(link)
        await asyncio.sleep(2)