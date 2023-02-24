import os
import pdfplumber
from loader import connection


async def update_db(path: str):
    #parse pdf
    with pdfplumber.open(path) as pdf:

        subject_list = ["Русский язык", "Белорусский язык", "Физика", "Математика",
                    "Химия", "Биология", "Английский язык", "Немецкий язык",
                    "Испанский язык", "Французский язык", "История Беларуси"
                    "Обществоведение", "География", "Всемирная история (новейшее время)",
                    "Китайский язык"]

        date = ""
        subject = ""
        place = ""
        name = ""

        for pdf_page in pdf.pages:
            text = iter(pdf_page.extract_text().split('\n'))

            if not date:
                for row in text:
                    if "Дата тестирования" in row:
                        date = row[-10:len(row)]
                        break

            for row in text:
                if row in subject_list:
                    subject=row

                elif "Корпус" in row:
                    place=row

                else:
                    name = " ".join(row.split().pop()) if 3 >= len(row.split()) <= 4 else ""
                    if name:
                        #add data in database
                        with connection.cursor() as cur:
                            cur.execute(
                                """INSERT INTO list (name, place, subject, date) VALUES (%s, %s, %s, %s);""",
                                (name.upper(),
                                place.upper(),
                                subject.upper(),
                                date.upper())
                            )

    os.remove(path=path)
                            
                            