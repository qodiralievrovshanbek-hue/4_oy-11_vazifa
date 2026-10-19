from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

it_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Python", callback_data="course_python")],
    [InlineKeyboardButton(text="Full Stack", callback_data="course_fullStack")],
    [InlineKeyboardButton(text="Kiberxavfsizlik", callback_data="course_kiber")],
])

ielts_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Listening", callback_data="ielts_listening"),
     InlineKeyboardButton(text="Reading", callback_data="ielts_reading")],
    [InlineKeyboardButton(text="Writing", callback_data="ielts_writing"),
     InlineKeyboardButton(text="Speaking", callback_data="ielts_speaking")],
])

sinf_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="1-sinf", callback_data="sinf_1"),
     InlineKeyboardButton(text="2-sinf", callback_data="sinf_2")],
    [InlineKeyboardButton(text="3-sinf", callback_data="sinf_3"),
     InlineKeyboardButton(text="4-sinf", callback_data="sinf_4")],
])