import asyncio
import datetime as dt
import os
import sys
from aiogram import Bot, Dispatcher, html
import logging
from aiogram.types.bot_command import BotCommand
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv
from app.handlers import router
from app.scheduller import scheduler

load_dotenv()

# Bot token can be obtained via https://t.me/BotFather
TOKEN = os.getenv("TOKEN_BOT")
# USER_ID = int(os.getenv("U_ID", 0))
# All handlers should be attached to the Router (or Dispatcher)

dp: Dispatcher = Dispatcher()
dp.include_router(router)


async def message_cron(bot: Bot, user_id: int):
    await bot.send_message(
        user_id, text=f"its message will be sent at {dt.datetime.now().isoformat()}"
    )


async def main():
    bot = Bot(TOKEN)
    scheduler.start()

    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Run bot"),
            BotCommand(command="add_event", description="add_event"),
            BotCommand(command="delete_event", description="delete_event"),
        ]
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        # filemode="w",
        # filename="botlog.log",
    )
    asyncio.run(main())
