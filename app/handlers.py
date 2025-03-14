import datetime
from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from apscheduler.job import Job
from app.scheduller import add_event
from .keyboard import BUTTON_ADD_EVENT, BUTTON_DELETE_EVENT, menu_keyboard
from .fsm import AddScheduleForm
from aiogram.fsm.context import FSMContext
from .scheduller import scheduler

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Hello, {message.from_user.full_name}! Use the buttons below to manage your reminders.",
        reply_markup=menu_keyboard(),
    )


@router.message(Command("add_event"))
@router.message(F.text == BUTTON_ADD_EVENT)
async def add_event_handler(message: Message, state: FSMContext):
    await state.set_state(AddScheduleForm.message)
    await message.answer(
        "Enter the reminder message:",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(AddScheduleForm.message)
async def step_get_message(message: Message, state: FSMContext):
    await state.update_data(message=message.text)
    await state.set_state(AddScheduleForm.date)
    await message.answer(
        "Enter the date in format YYYY-MM-DD. For example, 2023-10-25:",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(AddScheduleForm.date)
async def step_get_date(message: Message, state: FSMContext):
    try:
        datetime.datetime.strptime(message.text, "%Y-%m-%d")
        await state.update_data(date=message.text)
        await state.set_state(AddScheduleForm.time)
        await message.answer(
            "Enter the time in format HH:MM. For example, 14:30:",
            reply_markup=ReplyKeyboardRemove(),
        )
    except ValueError:
        await message.answer(
            "Invalid date format. Please use YYYY-MM-DD. Example: 2023-10-25",
            reply_markup=ReplyKeyboardRemove(),
        )


@router.message(AddScheduleForm.time)
async def step_get_time(message: Message, state: FSMContext, bot: Bot):
    try:
        data = await state.get_data()
        date_str = f"{data['date']} {message.text}"
        datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")

        result: Job = await add_event(
            message.from_user.id, data["message"], date_str, bot
        )
        await message.answer(
            f"Reminder saved for {date_str}", reply_markup=menu_keyboard()
        )
        await state.clear()
    except ValueError:
        await message.answer(
            "Invalid time format. Please use HH:MM. Example: 14:30",
            reply_markup=menu_keyboard(),
        )


@router.message(Command("delete"))
@router.message(F.text == BUTTON_DELETE_EVENT)
async def delete_event_handler(message: Message):
    jobs = scheduler.get_jobs()
    if not jobs:
        await message.answer("No reminders to delete.", reply_markup=menu_keyboard())
        return

    await message.answer(
        "Delete functionality is not yet implemented.", reply_markup=menu_keyboard()
    )
