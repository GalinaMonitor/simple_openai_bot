import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.utils.chat_action import ChatActionMiddleware

from config import settings
from handlers import router


async def main():
	bot = Bot(settings.bot_token)
	dp = Dispatcher()
	logging.basicConfig(level=logging.INFO)
	dp.include_router(router)
	dp.message.middleware(ChatActionMiddleware())
	await dp.start_polling(bot)

if __name__ == '__main__':
	asyncio.run(main())
