import datetime
import time
import asyncio
from telegram_bot.MessagesBot import MESSAGES
from cfg.config import PHOTO_FILE_ID, AD_1_2
from cfg.database import Database

db = Database('cfg/database')


async def send_ad(bot, message):
    print(AD_1_2)

    if AD_1_2[0]:
        try:
            await bot.send_photo(chat_id=message.from_user.id, caption=MESSAGES["ad_1"], photo=PHOTO_FILE_ID[0])
        except:
            await message.answer(MESSAGES["ad_1"])

        await asyncio.sleep(5)

    if AD_1_2[1]:
        try:
            await bot.send_photo(chat_id=message.from_user.id, caption=MESSAGES["ad_2"], photo=PHOTO_FILE_ID[1])
        except:
            await message.answer(MESSAGES["ad_2"])


async def malling_now(bot, text, file_id, t_or_f):
    try:
        all_ids = db.get_all_user_ids()
        for id_user in all_ids:
            try:
                if t_or_f:
                    await bot.send_photo(chat_id=id_user, photo=file_id, caption=text)
                else:
                    await bot.send_message(chat_id=id_user, text=text)
            except:
                ...
    except:
        pass


async def malling_postponed(bot, text, file_id, t_or_f, time):
    try:
        current_time = datetime.datetime.now()
        target_time = datetime.datetime.strptime(time, "%d.%m.%Y %H.%M")

        # Вычисляем разницу между текущим временем и целевым временем
        time_difference = target_time - current_time

        # Преобразуем разницу в секунды
        seconds = time_difference.total_seconds()

        all_ids = db.get_all_user_ids()

        await asyncio.sleep(seconds)
        for id_user in all_ids:
            try:
                if t_or_f:
                    await bot.send_photo(chat_id=id_user, photo=file_id, caption=text)
                else:
                    await bot.send_message(chat_id=id_user, text=text)
            except:
                ...
    except:
        ...

