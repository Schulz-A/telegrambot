import logging

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import ctx_data

from tgBot.config import Config


class AdminFilter(BoundFilter):
    key = "is_admin"

    def __init__(self, is_admin=None):
        self.is_admin = is_admin

    async def check(self, message: types.Message):
        if self.is_admin is None:
            return
        data = ctx_data.get()
        config = data.get('config')
        user_id = message.from_user.id
        return user_id in config.tg_bot.admin_ids
