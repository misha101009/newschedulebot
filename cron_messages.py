import datetime as dt

from aiogram import Bot

from config import UID


async def send_message_cron(bot: Bot):
    dtime = dt.datetime.now().strftime("%H:%M:%S")
    await bot.send_message(UID, text=f"Time now: {dtime}")
