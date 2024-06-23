from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config


config: Config = load_config()
bot = Bot(token=config.tg_bot.token)
dp = Dispatcher()


if __name__ == '__main__':
    dp.run_polling(bot)

