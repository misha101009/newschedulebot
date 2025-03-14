from aiogram.utils.keyboard import ReplyKeyboardBuilder

BUTTON_ADD_EVENT = "Add event"
BUTTON_DELETE_EVENT = "Delete event"


def menu_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(text=BUTTON_ADD_EVENT)
    builder.button(text=BUTTON_DELETE_EVENT)

    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)
