import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F
import asyncio

API_TOKEN = "6668563208:AAGjjyEvxGAetryZ-CaPjwyJjRIGbtKYBWI"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(F.text)
async def reply_all(message: Message):
    await message.reply("صاحب البوت هو: @xXx6l")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
