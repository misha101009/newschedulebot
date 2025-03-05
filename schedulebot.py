import asyncio
import datetime as dt
import os
from os import getenv

from aiogram import Bot, Dispatcher, html


from aiogram.types.bot_command import BotCommand
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

from handlers import router

load_dotenv()

# Bot token can be obtained via https://t.me/BotFather
TOKEN = os.getenv("BOT_TOKEN")
USER_ID = int(os.getenv("U_ID"))
# All handlers should be attached to the Router (or Dispatcher)

dp: Dispatcher = Dispatcher()
dp.include_router(router)


async def message_cron(bot: Bot, user_id: int):
    await bot.send_message(
        user_id, text=f"its message will be sent at {dt.datetime.now().isoformat()}"
    )


async def main():
    bot = Bot(TOKEN)
    scheduler = AsyncIOScheduler(timezone="Europe/Kyiv")

    scheduler.start()

    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Run bot"),
        ]
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

