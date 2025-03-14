import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
import logging

scheduler = AsyncIOScheduler(timezone="Europe/Kyiv")


async def add_event(user_id: int, event_text: str, date_str: str, bot: Bot):
    event_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")

    return scheduler.add_job(
        send_reminder,
        trigger="date",
        run_date=event_date,
        kwargs={"bot": bot, "user_id": user_id, "event_text": event_text},
    )


async def send_reminder(bot: Bot, user_id: int, event_text: str):
    await bot.send_message(user_id, text=f"Reminder: {event_text}")


if __name__ == "__main__":
    import asyncio, sys
    from dotenv import load_dotenv
    import os

    load_dotenv()

    TOKEN = os.getenv("BOT_TOKEN")
    USER_ID = int(os.getenv("U_ID"))


def list_jobs():
    jobs = scheduler.get_jobs()
    for job in jobs:
        print(f"Job ID: {job.id}, Run Time: {job.next_run_time}, Args: {job.kwargs}")

    async def main():
        event_date = datetime.datetime.now() + datetime.timedelta(hours=1, seconds=20)

        # bot = Bot(TOKEN)
        # dp: Dispatcher = Dispatcher()

        print("add sgh")

        scheduler.add_job(
            # send_reminder,
            lambda x: print(f"he {x}: {event_date}"),
            trigger="date",
            run_date=event_date,
            kwargs={"x": "uid"},
            # kwargs={
            #     "bot": bot,
            #     "user_id": USER_ID,
            #     "event_text": f"hi, {event_date}",
            # },
        )
        print("run sgh")
        scheduler.start()
        breakpoint()

        # await bot.delete_webhook(drop_pending_updates=True)
        # await dp.start_polling(bot)

    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())
