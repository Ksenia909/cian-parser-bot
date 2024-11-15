import asyncio

from aiogram.types import CallbackQuery
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from cian.parser import CianParser
from db.models import UserLastLink


async def parse_and_send_links(callback: CallbackQuery, url: str, session: AsyncSession, telegram_id: int):
    links = await CianParser(url=url).get_links()
    result = await session.execute(
        select(UserLastLink).where(UserLastLink.telegram_id == telegram_id)
    )
    user_last_link = result.scalars().first()
    for link in links[::2]:
        if user_last_link.last_link == link:
            break
        await callback.message.answer(link)
        await asyncio.sleep(2)

    if links and links[0] != user_last_link.last_link:
        user_last_link.last_link = links[0]
        await session.commit()