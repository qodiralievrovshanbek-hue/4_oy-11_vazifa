import asyncio
from aiogram import Bot,Dispatcher,F
from aiogram.types import Message,CallbackQuery
from aiogram.filters import Command,CommandStart

from keyboards.buttons import main_keyboards
from keyboards.buttons2 import it_buttons,ielts_buttons,sinf_buttons


dp = Dispatcher()

rasm = "https://pin.it/36lCpqP8B"

@dp.message(CommandStart())
async def start_handler(message:Message):
    await message.answer(text="Hello, everybody",
                         reply_markup=main_keyboards)

@dp.message(F.text == "IT Course")
async def about_it(message:Message):
    await message.answer(text="IT kurslarimiz",
                         reply_markup=it_buttons)

@dp.message(F.text == "IELTS Course")
async def about_ielts(message:Message):
    await message.answer(text="IELTS bo'limlari",
                         reply_markup=ielts_buttons)

@dp.message(F.text == "Maktab darsliklari")
async def about_maktab(message:Message):
    await message.answer(text="Sinfni tanlang",
                         reply_markup=sinf_buttons)

@dp.callback_query(F.data.startswith("course_"))
async def kurslar_haqida(callback:CallbackQuery):
    await callback.answer()

@dp.callback_query(F.data.startswith("ielts_"))
async def ielts_haqida(callback:CallbackQuery):
    await callback.answer()

@dp.callback_query(F.data.startswith("sinf_"))
async def sinflar_haqida(callback:CallbackQuery):
    if callback.data.endswith("1"):
        await callback.message.answer_photo(
            photo=rasm,
            caption="1-sinf"
        )
    elif callback.data.endswith("2"):
        await callback.message.answer_photo(
            photo=rasm,
            caption="2-sinf"
        )
    elif callback.data.endswith("3"):
        await callback.message.answer_photo(
            photo=rasm,
            caption="3-sinf"
        )
    elif callback.data.endswith("4"):
        await callback.message.answer_photo(
            photo=rasm,
            caption="4-sinf"
        )
    await callback.answer()


async def start():
    bot = Bot(token="8914205774:AAGDW0ymSKvJGL5pImKHmHol_ahMxwLE1ns")
    print("Bot ishga tushdi")
    await dp.start_polling(bot)



asyncio.run(start())