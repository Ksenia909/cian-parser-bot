import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage, Redis, DefaultKeyBuilder
from aiogram_dialog import setup_dialogs
from arq import create_pool

from config_data.config import Config, load_config
from dialogs.options_menu import options_menu_dialogs
from handlers import handlers

logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(level=logging.INFO,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    config: Config = load_config()

    redis = Redis(host=config.redis_host.host)
    storage = RedisStorage(redis=redis, key_builder=DefaultKeyBuilder(with_destiny=True))
    redis_pool = await create_pool()

    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode='HTML')
    )

    dp = Dispatcher(storage=storage)

    dp.include_router(handlers.router)
    dp.include_router(options_menu_dialogs())

    setup_dialogs(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, arqredis=redis_pool)


if __name__ == '__main__':
    asyncio.run(main())

