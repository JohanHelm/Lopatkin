import os
import dotenv

from aiogram import Bot, Dispatcher

from handlers.register import register_common


async def start_bot():
    dotenv.load_dotenv("secrets/.env")
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    register_common(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
