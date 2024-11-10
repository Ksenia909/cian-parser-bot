import asyncio
import logging
from asyncio import WindowsSelectorEventLoopPolicy

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage, Redis, DefaultKeyBuilder
from aiogram_dialog import setup_dialogs
from arq import create_pool
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config_data.config import Config, load_config
from dialogs.options_menu import options_menu_dialogs
from handlers import handlers
from middlewares import DbSessionMiddleware

logger = logging.getLogger(__name__)
asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

async def main() -> None:
    logging.basicConfig(level=logging.INFO,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    config: Config = load_config()

    redis = Redis(
        host=config.redis_host.host,
        port=config.redis_host.port,
        password=config.redis_host.password
    )
    storage = RedisStorage(redis=redis, key_builder=DefaultKeyBuilder(with_destiny=True))
    redis_pool = await create_pool()

    engine = create_async_engine(
        url=config.db_config.dsn,
        echo=config.db_config.echo
    )

    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))

    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode='HTML')
    )

    dp = Dispatcher(storage=storage)

    Sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
    dp.update.outer_middleware(DbSessionMiddleware(Sessionmaker))

    dp.include_router(handlers.router)
    dp.include_router(options_menu_dialogs())

    setup_dialogs(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, arqredis=redis_pool)

if __name__ == '__main__':
    asyncio.run(main())

