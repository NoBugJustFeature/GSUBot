from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter

from data.config import admins_id


class IsAdmin(BoundFilter):
    async def check(self, message: Message):
        return message.from_id in admins_id
