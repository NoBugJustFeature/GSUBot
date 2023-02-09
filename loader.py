from aiogram import Bot, Dispatcher
from data import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)