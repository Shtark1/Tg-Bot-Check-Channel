import asyncio

from aiogram import Bot
from aiogram.types import ChatJoinRequest, Message
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


from telegram_bot.MessagesBot import MESSAGES
from telegram_bot.KeyboardButton import BUTTON_TYPES
from telegram_bot.DopFunctional import send_ad
from cfg.config import ADMIN_ID, BTN_TEXT_START
from cfg.database import Database

db = Database('cfg/database')


async def start_bot(bot: Bot):
    for admin_id in ADMIN_ID:
        await bot.send_message(admin_id, MESSAGES["start_bot"])


async def stop_bot(bot: Bot):
    for admin_id in ADMIN_ID:
        await bot.send_message(admin_id, MESSAGES["stop_bot"])


async def approve_request(chat_join: ChatJoinRequest, bot: Bot):
    await bot.send_message(chat_id=chat_join.from_user.id, text=MESSAGES["star_new_users"],
                           reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=f"{BTN_TEXT_START[0]}")]],
                                                            resize_keyboard=True, one_time_keyboard=True))

    await asyncio.sleep(5)
    try:
        await chat_join.approve()
    except:
        pass


# START
async def get_start(message: Message, bot: Bot):
    if message.from_user.id in ADMIN_ID:
        await message.answer(MESSAGES["start_admin"], reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
    else:
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id, message.from_user.username)
            await message.answer(MESSAGES["subscription_try"])

            await asyncio.sleep(10)
        await send_ad(bot, message)


# ЛЮБОЙ ТЕКСТ
async def all_text(message: Message, bot: Bot):
    if message.from_user.id in ADMIN_ID:
        await message.answer(MESSAGES["not_command"], reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
    else:
        await send_ad(bot, message)


