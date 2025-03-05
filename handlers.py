import datetime 
from datetime import datetime

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import (Message)
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from tool_scheduller import add_event

from .commands import ADD_DAY_COMMAND
from .keyboard import BUTTON_ADD_DAY, BUTTON_DELETE_DAY, menu_keyboard

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Hello, {message.from_user.full_name}", reply_markup=menu_keyboard()
    )


@router.message(Command("add"))
async def add_event_handler(message: Message):
    try:
        parts = message.text.split(" ", 2)
        if len(parts) < 3:
            await message.answer("Use: /add YYYY-MM-DD Event")
            return

        date_str, event_text = parts[1], parts[2]
        datetime.strptime(date_str, "%Y-%m-%d")

        add_event(message.from_user.id, event_text, date_str)
        await message.answer(f"Event saved for {date_str}")
    except ValueError:
        await message.answer("Invalid date format. Use YYYY-MM-DD")


scheduler = AsyncIOScheduler()


@router.message(Command("delete"))
async def delete_event_handler(message: Message):
    try:
        parts = message.text.split(" ", 1)
        if len(parts) < 2:
            await message.answer("Use /delete EventID")
            return

        event_id = parts[1]
        await message.answer(f"Event {event_id} deleted")
    except ValueError:
        await message.answer("Invalid event ID")
