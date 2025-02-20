import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties

# Replace with your actual bot token
BOT_TOKEN = "7937438041:AAFu0Btg_S2-yA-bo4PVixy9Jqe_eYk1hfk"
WEB_APP_URL = "https://bbkriket.com/chama"  # Replace with your Mini App URL

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    web_app_button = KeyboardButton(text="Open Mini App", web_app=WebAppInfo(url=WEB_APP_URL))
    keyboard.add(web_app_button)

    await message.answer("Click below to open the Mini App:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
