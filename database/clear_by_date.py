from loader import connection

async def clear_by_date_db(date):
    with connection.cursor() as cur:
        cur.execute("DELETE FROM list WHERE date = (%s)", (date,))