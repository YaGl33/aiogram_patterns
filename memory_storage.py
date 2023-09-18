from aiogram import Dispatcher, executor, types
from aiogram.bot import Bot
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

import logging

logging.basicConfig(level=logging.INFO)


storage = MemoryStorage()
bot = Bot(token="6482772943:AAGET_sVBjEVdS3bHANCPyIHKD9-SG9KmOo")
dp = Dispatcher(bot, storage=storage)


class InputName(StatesGroup):
    input_word = State()



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Welcome")


@dp.message_handler(commands=['in'])
async def in_command(message: types.Message):
    await message.answer("Enter ur name")
    await InputName.next()


@dp.message_handler(state=InputName.input_word)
async def return_word(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['w'] = message.text
        await message.answer(f"Ur name is {data['w']}")
        await state.finish()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
