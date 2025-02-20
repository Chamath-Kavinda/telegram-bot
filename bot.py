from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.utils import executor

# Replace this with your actual bot token from BotFather
BOT_TOKEN = "YOUR_BOT_TOKEN"
WEB_APP_URL = "https://yourapp.com"  # Replace with your Mini App URL

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    web_app_button = KeyboardButton("Open Mini App", web_app=WebAppInfo(url=WEB_APP_URL))
    keyboard.add(web_app_button)
    
    await message.answer("Click below to open the Mini App:", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp)
