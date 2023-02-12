from loader import connection

def get_date() -> set:
    with connection.cursor() as cur:
        cur.execute("SELECT date FROM list")
        return set(cur.fetchall())



