import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import json

async def add_job(bot, message_cron, USER_ID):
    scheduler.add_job(
        message_cron,
        trigger="date",
        minutes= 0.5,
        # hours = 1,
        start_date=datetime.datetime.now(),
        kwargs={"bot": bot, "user_id": USER_ID},
    )

scheduler = AsyncIOScheduler()

async def add_event(user_id: int, event_text: str, date_str: str, bot):
    event_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    scheduler.add_job(
        send_reminder,
        trigger="date",
        run_date=event_date,
        kwargs={"bot": bot, "user_id": user_id, "event_text": event_text},
    )

async def send_reminder(bot, user_id: int, event_text: str):
    await bot.send_message(user_id, text=f"Reminder: {event_text}")


def load_reminders():
    try:
        with open('reminders.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_reminders(reminders):
    with open('reminders.json', 'w') as file:
        json.dump(reminders, file, indent=4)

def add_event(user_id, event_text, date_str):
    reminders = load_reminders()
    reminders.append({
        "user_id": user_id,
        "event_text": event_text,
        "date": date_str
    })
    save_reminders(reminders)

def delete_event(user_id, date_str):
    reminders = load_reminders()
    reminders = [reminder for reminder in reminders if not (reminder["user_id"] == user_id and reminder["date"] == date_str)]
    save_reminders(reminders)