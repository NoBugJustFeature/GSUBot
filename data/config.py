import os
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN=str(os.getenv("BOT_TOKEN"))

admins_id=list(map(int, str(os.getenv("admins_id")).split()))

host=str(os.getenv("host"))
user=str(os.getenv("user"))
password=str(os.getenv("password"))
database=str(os.getenv("database"))


