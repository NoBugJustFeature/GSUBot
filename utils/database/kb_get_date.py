from loader import connection

def get_date() -> list:
    with connection.cursor() as cur:
        cur.execute("SELECT date FROM list")
        return cur.fetchall()[0]



