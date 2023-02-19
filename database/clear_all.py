from loader import connection

async def clear_all_db():
    with connection.cursor() as cur:
        cur.execute("TRUNCATE list")
