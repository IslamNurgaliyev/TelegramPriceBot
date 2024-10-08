import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv


load_dotenv('.env')

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f'Hello, {message.from_user.full_name}!')


@dp.edited_message()
async def edit(message: types.Message):
    await message.reply('ASD')


@dp.message()
async def echo(message: types.Message):
    await message.reply(message.text)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
