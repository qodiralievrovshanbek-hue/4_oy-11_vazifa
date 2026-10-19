from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="IT Course"), KeyboardButton(text="IELTS Course")],
        [KeyboardButton(text="Maktab darsliklari")],
    ],
    resize_keyboard=True,
)