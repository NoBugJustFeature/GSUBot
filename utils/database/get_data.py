from aiogram.types import Message
from loader import connection

async def get_data(message: Message):
    name = message.text
    with connection.cursor() as cur:
        cur.execute(
            "SELECT * FROM list WHERE name = (%s)",
            (name.upper(),)
        )
        if data:=cur.fetchall():
            data = data[0]

            name = data[0].title()
            place = data[1]
            subject = data[2]
            date = data[3]

            await message.answer(f"{name}\nПредмет: {subject}\n{place}\nДата: {date}")
        else:
            await message.answer(f"ФИО не найдено\n(списки обновляются вечером за день до экзамена)")
