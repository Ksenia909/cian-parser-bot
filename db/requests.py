import json
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User, CianURL


async def merge_or_create_user(
        session: AsyncSession,
        telegram_id: int,
        first_name: str,
        last_name: str | None = None,
):
    user = User(
        telegram_id=telegram_id,
        first_name=first_name,
        last_name=last_name,
    )
    await session.merge(user)
    await session.commit()


async def merge_or_create_cian_url(
        session: AsyncSession,
        telegram_id: int,
        url: str,
        data: dict
):
    print(data)
    cian_url = CianURL(
        telegram_id=telegram_id,
        url=url,
        metro=json.dumps(data.get("metro")),  # Преобразуем dict в строку
        time=data.get("time"),
        rooms=json.dumps(data.get("rooms")),  # Преобразуем list в строку
        price_min=data.get("price_min"),
        price_max=data.get("price_max"),
    )

    await session.merge(cian_url)
    await session.commit()

