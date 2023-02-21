from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from psycopg2 import connect

from data import config


storage = MemoryStorage()

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)

connection=connect(host=config.host,
                   user=config.user,
                   password=config.password,
                   database=config.database)

connection.autocommit = True


ban_time = 60
