from aiogram import Dispatcher, executor, types
from aiogram.bot import Bot

import logging

logging.basicConfig(level=logging.INFO)


bot = Bot(token="6482772943:AAGET_sVBjEVdS3bHANCPyIHKD9-SG9KmOo")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Hello, this is the simple echo bot.\n"
                         "Write me something...")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
    

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
