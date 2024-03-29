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

#time for antispam
#minimal time between commands
await_time = 10
#time of ban for spam
ban_time = 60

#link for download file
url = "http://old.gsu.by/dinamika/SpisokRT.pdf"
#path for download file
path = "data\pdf\SpisokRT.pdf"


#for statistic
class Counter:
    def __init__(self):
        self.__num = 0

    def __str__(self):
        return str(self.__num)

    def add(self):
        self.__num += 1

num_of_calls = Counter()