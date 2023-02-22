'''
This file create tables, use this once before launching the bot
'''
from loader import connection


addresses=[("Корпус 1", "52.445663", "30.998869"),
         ("Корпус 5", "52.4418203", "31.0014247"),
         ("Корпус 4", "52.4429174", "31.0009885"),
         ("Корпус 3", "52.4450565", "30.9968833"),
         ("Корпус 2", "52.4451328", "30.9960911"),
         ("Корпус 8", "52.4431563", "30.9991332"),]


def create_tables(connection):
    with connection.cursor() as cur:
        cur.execute(
            '''CREATE TABLE list(
                name TEXT NOT NULL,
                place TEXT NOT NULL,
                subject TEXT NOT NULL,
                date TEXT NOT NULL
            );''')

        cur.execute(
            '''CREATE TABLE address(
                number TEXT NOT NULL,
                lat TEXT NOT NULL,
                lon TEXT NOT NULL
            );''')


def setup_address(connection):
    with connection.cursor() as cur:
        for address in addresses:
            cur.execute(
                '''INSERT INTO address (number, lat, lon)
                    VALUES (%s, %s, %s);''',(
                    address[0],
                    address[1],
                    address[2],
                ))


if __name__ == '__main__':
    create_tables(connection)
    setup_address(connection) 