from aiogram import Dispatcher
from data.config import admins_id


async def on_startup_notify(dp: Dispatcher):
    print("Notify admins")
    for admin in admins_id:
        await dp.bot.send_message(chat_id=admin, text="Бот запущен")
        print(admin)