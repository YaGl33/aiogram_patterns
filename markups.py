from aiogram.bot import Bot
from aiogram import Dispatcher, executor, types

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import logging


class TestMarkup(KeyboardButton):
    test_button_1 = KeyboardButton(text="Test 1")
    test_button_2 = KeyboardButton(text="Test 2")
    test_button_3 = KeyboardButton(text="Test 3")


markup_main = ReplyKeyboardMarkup(row_width=2)
markup_main.add(
    TestMarkup.test_button_1,
    TestMarkup.test_button_2,
    TestMarkup.test_button_3
)


bot = Bot(token="6482772943:AAGET_sVBjEVdS3bHANCPyIHKD9-SG9KmOo")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Choose one of theese buttons", 
                   reply_markup=markup_main)
    

@dp.message_handler(regexp="Test 1")
async def test_1(message: types.Message):
    await message.answer("Test 1 passed")


@dp.message_handler(regexp="Test 2")
async def test_2(message: types.Message):
    await message.answer("Test 2 passed")


@dp.message_handler(regexp="Test 3")
async def test_3(message: types.Message):
    await message.answer("Test 3 passed")

if "__main__" == __name__:
    executor.start_polling(dp, skip_updates=True)
