from aiogram.utils.keyboard import (ReplyKeyboardBuilder)

BUTTON_ADD_DAY = "Додати день"
BUTTON_DELETE_DAY = "Видалити день"

PAGE_SIZE = 3


def menu_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(text=BUTTON_ADD_DAY)
    builder.button(text=BUTTON_DELETE_DAY)

    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup
