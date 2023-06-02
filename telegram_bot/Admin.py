import re
from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from telegram_bot.MessagesBot import MESSAGES
from telegram_bot.KeyboardButton import BUTTON_TYPES
from telegram_bot.utils import StateAdmin
from cfg.config import ADMIN_ID, PHOTO_FILE_ID, AD_1_2, BTN_TEXT_START
from telegram_bot.DopFunctional import send_ad, malling_now, malling_postponed


# =================== ДОБАВЛЕНИЯ АДМИНА ===================
async def add_admin(message: Message, state: FSMContext, bot: Bot):
    if message.from_user.id in ADMIN_ID:
        await message.answer(MESSAGES["add_admin"], reply_markup=BUTTON_TYPES["BTN_CANCEL"])
        await state.set_state(StateAdmin.STATE_ADMIN_0)
    else:
        await send_ad(bot, message)


# Сохранение нового id админа
async def add_id_admin(message: Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await message.answer(MESSAGES['start_admin'], reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
        await state.clear()
    elif message.text.isnumeric():
        new_users_id = int(message.text)
        ADMIN_ID.append(new_users_id)
        await message.answer("Добавил!", reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
        await state.clear()
    else:
        await message.answer(MESSAGES["not_admin_id"], reply_markup=BUTTON_TYPES["BTN_CANCEL"])
        await state.set_state(StateAdmin.STATE_ADMIN_0)


# =================== ИЗМЕНЕНИЕ ПРИВЕТСТВИЯ ===================
async def edit_hi(message: Message, state: FSMContext, bot: Bot):
    if message.from_user.id in ADMIN_ID:
        await message.answer(MESSAGES["edit_hi"])
        await message.answer(MESSAGES["star_new_users"], reply_markup=BUTTON_TYPES["BTN_CANCEL"])

        await state.set_state(StateAdmin.STATE_ADMIN_1)
    else:
        await send_ad(bot, message)


# Сохранение нового текста
async def new_text_hi(message: Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await message.answer(MESSAGES['start_admin'], reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
        await state.clear()
    else:
        MESSAGES["star_new_users"] = f"{message.text}"
        await message.answer("Изменил!", reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
        await state.clear()


# =================== ИЗМЕНЕНИЕ РЕКЛАМНОГО ПОСТА №1 & №2 ===================
async def edit_ad_1(message: Message, state: FSMContext, bot: Bot):
    if message.from_user.id in ADMIN_ID:
        await state.update_data(type_ad=f"{message.text}")
        await message.answer(MESSAGES["edit_ad"], reply_markup=BUTTON_TYPES["BTN_CANCEL"])

        if message.text == "Изменить рекламный пост №1":
            if AD_1_2[0]:
                await message.answer(MESSAGES["ad_1"], reply_markup=BUTTON_TYPES["BTN_OFF"])
            else:
                await message.answer(MESSAGES["ad_1"], reply_markup=BUTTON_TYPES["BTN_ON"])

        else:
            if AD_1_2[1]:
                await message.answer(MESSAGES["ad_2"], reply_markup=BUTTON_TYPES["BTN_OFF"])
            else:
                await message.answer(MESSAGES["ad_2"], reply_markup=BUTTON_TYPES["BTN_ON"])

        await state.set_state(StateAdmin.STATE_ADMIN_2)
    else:
        await send_ad(bot, message)


# Получение текста
async def new_text_ad_1(message: Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await message.answer(MESSAGES['start_admin'], reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
        await state.clear()
    else:
        await state.update_data(ad_text=f"{message.text}")
        await message.answer(MESSAGES["edit_ad_photo"], reply_markup=BUTTON_TYPES["BTN_EDIT_AD"])
        await state.set_state(StateAdmin.STATE_ADMIN_3)


# Получение фото
async def new_photo_ad_1(message: Message, state: FSMContext):
    all_data = await state.get_data()

    try:
        if all_data["type_ad"] == "Изменить рекламный пост №1":
            MESSAGES["ad_1"] = f"{all_data['ad_text']}"
            file_id = message.photo[-1].file_id
            PHOTO_FILE_ID[0] = file_id
        else:
            MESSAGES["ad_2"] = f"{all_data['ad_text']}"
            file_id = message.photo[-1].file_id
            PHOTO_FILE_ID[1] = file_id

        await message.answer("Текст и картинка изменина!")
        await message.answer(MESSAGES['start_admin'], reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
        await state.clear()

    except:
        if message.text.lower() == "отмена":
            await message.answer(MESSAGES['start_admin'], reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
            await state.clear()

        elif message.text.lower() == "пропустить":
            if all_data["type_ad"] == "Изменить рекламный пост №1":
                MESSAGES["ad_1"] = f"{all_data['ad_text']}"
            else:
                MESSAGES["ad_2"] = f"{all_data['ad_text']}"

            await message.answer("Текст изменён!")
            await message.answer(MESSAGES['start_admin'], reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
            await state.clear()


# =================== ВЫКЛЮЧЕНИЕ РЕКЛАМЫ №1 или №2 ===================
async def off_or_on(callback: CallbackQuery, state: FSMContext):
    all_data = await state.get_data()
    if callback.data == "off":
        await callback.message.edit_reply_markup(reply_markup=BUTTON_TYPES["BTN_ON"])

        if all_data["type_ad"] == "Изменить рекламный пост №1":
            AD_1_2[0] = False
        else:
            AD_1_2[1] = False
    else:
        await callback.message.edit_reply_markup(reply_markup=BUTTON_TYPES["BTN_OFF"])

        if all_data["type_ad"] == "Изменить рекламный пост №1":
            AD_1_2[0] = True
        else:
            AD_1_2[1] = True


# =================== СДЕЛАТЬ РАССЫЛКУ ===================
async def time_malling(message: Message, state: FSMContext):
    await message.answer(MESSAGES["malling_time"], reply_markup=BUTTON_TYPES["BTN_CANCEL"])
    await state.set_state(StateAdmin.STATE_ADMIN_4)


# Получение даты
async def date_malling(message: Message, state: FSMContext):
    match = re.match(r'\d{2}\.\d{2}\.\d{4} \d{2}\.\d{2}', message.text)

    if message.text.lower() == "отмена":
        await message.answer(MESSAGES['start_admin'], reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
        await state.clear()

    elif message.text == "0" or match is not None:
        await message.answer(MESSAGES["malling_text"], reply_markup=BUTTON_TYPES["BTN_CANCEL"])
        await state.update_data(time_ad=f"{message.text}")
        await state.set_state(StateAdmin.STATE_ADMIN_5)

    elif match is None:
        await message.answer("Неверный формат")
        await message.answer(MESSAGES["malling_time"], reply_markup=BUTTON_TYPES["BTN_CANCEL"])
        await state.set_state(StateAdmin.STATE_ADMIN_4)


# Получение текста
async def text_malling(message: Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await message.answer(MESSAGES['start_admin'], reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
        await state.clear()

    else:
        await state.update_data(text_malling_post=f"{message.text}")
        await message.answer('Текст добавлен, скинь фото \nили \nжми "Пропустить"', reply_markup=BUTTON_TYPES["BTN_EDIT_AD"])
        await state.set_state(StateAdmin.STATE_ADMIN_6)


# Получение фото
async def photo_malling(message: Message, state: FSMContext, bot: Bot):
    all_data = await state.get_data()

    try:
        file_id = message.photo[-1].file_id
        if all_data["time_ad"] == "0":
            await message.answer(f"Рассылка с текстом и картинкой создана, будет отправлена сейчас")
            await malling_now(bot, all_data["text_malling_post"], file_id, True)

        else:
            await message.answer(f"Рассылка с текстом и картинкой создана, будет отправлена в {all_data['time_ad']}")
            await malling_postponed(bot, all_data["text_malling_post"], file_id, True, all_data["time_ad"])

        await message.answer(MESSAGES['start_admin'], reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
        await state.clear()

    except:
        if message.text.lower() == "отмена":
            await message.answer(MESSAGES['start_admin'], reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
            await state.clear()

        elif message.text.lower() == "пропустить":
            if all_data["time_ad"] == "0":
                await message.answer("Рассылка с текстом создана, будет отправлена сейчас")
                await malling_now(bot, all_data["text_malling_post"], "", False)

            else:
                await message.answer(f"Рассылка с текстом и картинкой создана, будет отправлена в {all_data['time_ad']}")
                await malling_postponed(bot, all_data["text_malling_post"], "", False, all_data["time_ad"])

            await message.answer(MESSAGES['start_admin'], reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
            await state.clear()


# =================== ИЗМЕНЕНИЕ КНОПКИ ПОЛЬЗОВАТЕЛЯ ===================
async def edit_btn(message: Message, state: FSMContext, bot: Bot):
    if message.from_user.id in ADMIN_ID:
        await message.answer(f"Сейчас кнопка у пользователя такая:\n\n{BTN_TEXT_START[0]}", reply_markup=BUTTON_TYPES["BTN_CANCEL"])
        await state.set_state(StateAdmin.STATE_ADMIN_7)
    else:
        await send_ad(bot, message)


# Сохранение новой кнопки
async def save_btn(message: Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await message.answer(MESSAGES['start_admin'], reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
        await state.clear()
    else:
        BTN_TEXT_START[0] = f"{message.text}"
        await message.answer("Изменил!", reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
        await state.clear()


# =================== ИЗМЕНЕНИЕ ТЕКСТА ПОСЛЕ НАЖАТИЯ НА КНОПКУ ===================
async def edit_text_post(message: Message, state: FSMContext, bot: Bot):
    if message.from_user.id in ADMIN_ID:
        await message.answer(f"Сейчас установлен такой текст после нажатия на кнопку:\n\n{MESSAGES['subscription_try']}", reply_markup=BUTTON_TYPES["BTN_CANCEL"])
        await state.set_state(StateAdmin.STATE_ADMIN_8)
    else:
        await send_ad(bot, message)


# Сохранение нового текста
async def save_text_post(message: Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await message.answer(MESSAGES['start_admin'], reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
        await state.clear()
    else:
        MESSAGES["subscription_try"] = f"{message.text}"
        await message.answer("Изменил!", reply_markup=BUTTON_TYPES["BTN_HOME_ADMIN"])
        await state.clear()