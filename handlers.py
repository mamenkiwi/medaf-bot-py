from aiogram.types import Message, ContentType
from aiogram.types import PreCheckoutQuery, LabeledPrice
from aiogram.dispatcher.filters import Command

from main import bot, dp
from config import PAYMENTS_TOKEN

from keyboards import keyboard,   keybord_markup

@dp.message_handler(Command('start'))
async def start(message: Message):
    await bot.send_message(message.chat.id,
                           "<b>Let's get started!</b>\nPlease tap the button below to order your phone case",
                           reply_markup=keybord_markup)