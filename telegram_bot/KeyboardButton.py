from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from cfg.config import BTN_TEXT_START

# КНОПКИ МЕНЮ
btn_edit_hi = KeyboardButton(text="Изменить приветствие")
btn_edit_ad_1 = KeyboardButton(text="Изменить рекламный пост №1")
btn_edit_ad_2 = KeyboardButton(text="Изменить рекламный пост №2")
btn_edit_btn = KeyboardButton(text="Изменить кнопку")
btn_edit_text = KeyboardButton(text="Изменить текст")
btn_mailing = KeyboardButton(text="Сделать рассылку")
btn_add_admin = KeyboardButton(text="Добавить админа")
btn_miss = KeyboardButton(text="Пропустить")
btn_cancel = KeyboardButton(text="Отмена")
btn_start = KeyboardButton(text=f"{BTN_TEXT_START[0]}")

btn_off = InlineKeyboardButton(text="❎ Отключить ❎", callback_data="off")
btn_on = InlineKeyboardButton(text="✅ Включить ✅", callback_data="on")


# ДЛЯ ГОТОВОГО ПОСТА
btn_add_btn_url = InlineKeyboardButton(text="Добавить URL-кнопку", callback_data="btn_url")


BUTTON_TYPES = {
    "BTN_HOME_ADMIN": ReplyKeyboardMarkup(keyboard=[[btn_edit_hi],
                                                    [btn_edit_ad_1, btn_edit_ad_2],
                                                    [btn_edit_btn, btn_edit_text],
                                                    [btn_mailing],
                                                    [btn_add_admin]], resize_keyboard=True, one_time_keyboard=True),
    "BTN_CANCEL": ReplyKeyboardMarkup(keyboard=[[btn_cancel]], resize_keyboard=True, one_time_keyboard=True),
    "BTN_EDIT_AD": ReplyKeyboardMarkup(keyboard=[[btn_miss], [btn_cancel]], resize_keyboard=True, one_time_keyboard=True),
    "BTN_START": ReplyKeyboardMarkup(keyboard=[[btn_start]], resize_keyboard=True, one_time_keyboard=True),

    "BTN_OFF": InlineKeyboardMarkup(inline_keyboard=[[btn_off]]),
    "BTN_ON": InlineKeyboardMarkup(inline_keyboard=[[btn_on]]),

    # "BTN_REFERENCE": InlineKeyboardMarkup(),
}
