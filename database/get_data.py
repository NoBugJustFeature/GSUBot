from aiogram.types import Message
from loader import connection, bot

from keyboards.user_keyboards.keyboard_start import kb_start
from keyboards.admin_keyboards.keyboard_admin import kb_admin

from loader import url

async def get_data(message: Message, is_admin: bool):
    
    keyboard = kb_admin if is_admin else kb_start

    name = message.text
    with connection.cursor() as cur:
        cur.execute(
            "SELECT * FROM list WHERE name = (%s)",
            (name.upper(),)
        )
        if data:=cur.fetchall():
            for row in data:
                name = row[0].title()
                place = row[1].title()
                subject = row[2].title()
                date = row[3]

                number = " ".join(place.split()[0:2])

                cur.execute(
                    'SELECT * FROM address WHERE number = (%s)',
                    (number,)
                )

                cords = cur.fetchall()[0]

                await message.answer(f"{name}\nПредмет: {subject}\n{place}\nДата: {date}", reply_markup=keyboard)
                await bot.send_location(message.from_id, latitude=float(cords[1]), longitude=float(cords[2]))
        else:
            await message.answer(f"ФИО не найдено\n(списки обновляются вечером за день до экзамена)", reply_markup=keyboard)
            await message.answer(f"Возможно вы ввели неверные данные при регистрации\nПопробуйте найти себя в онлайн-списке\n{url}", reply_markup=keyboard)
            
