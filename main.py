import contextlib
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, Text
import logging

from telegram_bot import TelegramBot
from telegram_bot import Admin
from telegram_bot.utils import StateAdmin
from cfg.config import BOT_TOKEN, CHANNEL_ID, BTN_TEXT_START


async def start():
    logging.basicConfig(level=logging.DEBUG, format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s')

    bot: Bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    # РЕГИСТРАЦИЯ СОБЫТИЙ
    dp.startup.register(TelegramBot.start_bot)
    dp.shutdown.register(TelegramBot.stop_bot)

    dp.chat_join_request.register(TelegramBot.approve_request, F.chat.id == CHANNEL_ID)

    dp.message.register(TelegramBot.get_start, Command("start"))
    dp.message.register(TelegramBot.get_start, Text(BTN_TEXT_START))

    dp.message.register(Admin.add_admin, Text("Добавить админа"))
    dp.message.register(Admin.add_id_admin, StateAdmin.STATE_ADMIN_0)

    dp.message.register(Admin.edit_hi, Text("Изменить приветствие"))
    dp.message.register(Admin.new_text_hi, StateAdmin.STATE_ADMIN_1)

    dp.message.register(Admin.edit_ad_1, Text(["Изменить рекламный пост №1", "Изменить рекламный пост №2"]))
    dp.message.register(Admin.new_text_ad_1, StateAdmin.STATE_ADMIN_2)
    dp.message.register(Admin.new_photo_ad_1, StateAdmin.STATE_ADMIN_3)
    dp.callback_query.register(Admin.off_or_on, StateAdmin.STATE_ADMIN_2)

    dp.message.register(Admin.time_malling, Text("Сделать рассылку"))
    dp.message.register(Admin.date_malling, StateAdmin.STATE_ADMIN_4)
    dp.message.register(Admin.text_malling, StateAdmin.STATE_ADMIN_5)
    dp.message.register(Admin.photo_malling, StateAdmin.STATE_ADMIN_6)

    dp.message.register(Admin.edit_btn, Text("Изменить кнопку"))
    dp.message.register(Admin.save_btn, StateAdmin.STATE_ADMIN_7)

    dp.message.register(Admin.edit_text_post, Text("Изменить текст"))
    dp.message.register(Admin.save_text_post, StateAdmin.STATE_ADMIN_8)

    dp.message.register(TelegramBot.all_text, Text)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as ex:
        logging.error(f'[Exception] - {ex}', exc_info=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())
