from aiogram.fsm.state import State, StatesGroup


class AddScheduleForm(StatesGroup):
    message = State()
    date = State()
    time: State = State()
