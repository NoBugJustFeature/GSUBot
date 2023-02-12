from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("testing", "Узнать место и время тестирования (списки обновляются вечером за день до экзамена)"),
        types.BotCommand("help", "Помощь")
    ])