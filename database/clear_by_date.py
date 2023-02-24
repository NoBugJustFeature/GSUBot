from loader import connection

def clear_by_date_db(date):
    with connection.cursor() as cur:
        cur.execute("DELETE FROM list WHERE date = (%s)", (date,))