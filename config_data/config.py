from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class RedisHost:
    host: str
    port: int
    password: str


@dataclass
class DbConfig:
    dsn: str
    echo: bool


@dataclass
class Config:
    tg_bot: TgBot
    redis_host: RedisHost
    db_config: DbConfig


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')),
                  redis_host=RedisHost(host=env('REDIS_HOST'),
                                       port=env.int('REDIS_PORT'),
                                       password=env('REDIS_PASSWORD')),
                  db_config=DbConfig(dsn=env('DATABASE_URL'),
                                     echo=env.bool('DB_ECHO')))
