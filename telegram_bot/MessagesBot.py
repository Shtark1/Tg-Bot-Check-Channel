from cfg.config import BTN_TEXT_START


# СООБЩЕНИЯ ОТ БОТА
start_admin_message = "Приветствую админ 👋"
start_bot_message = "Бот запущен!"
stop_bot_message = "Бот остановлен!"

star_new_users_message = """Для вход в канал пиши команду /start

И тогда бот примет тебя в канал!"""

subscription_try_message = "Твоя подписка на канал одобрена!\nhttps://t.me/+VavtQcodUzM2NDMy"

ad_1_message = "Рекламный пост №1"
ad_2_message = "Рекламный пост №2"

not_command_message = "Админ, такой команды нет("
add_admin_message = """ID состоит только из чисел, его можно получить тут https://t.me/getmyid_bot

Вводи ID пользователя:"""
not_admin_id_message = """Это не число, ID состоит только из чисел, его можно получить тут https://t.me/getmyid_bot

Вводи ID пользователя:"""
edit_hi_message = """Отправь текст если хочешь изменить приветствие, 
если нет, то жми "Отмена"

Сейчас стоит такое приветствие:"""
edit_ad_message = """Отправь текст если хочешь изменить рекламный пост, 
если нет, то жми "Отмена"

Сейчас стоит такая реклама:"""
edit_ad_photo_message = "Вы хотите добавить фото к рекламе?"
malling_time_message = """Укажи дату когда сделать рассылку в таком формате 
"26.02.2023 15.00"

Если рассылку надо сделать сейчас то пиши 0"""
malling_text_message = """Впиши текст который будет у рассылки 
или
жми "Отмена" """

MESSAGES = {
    "start_admin": start_admin_message,
    "start_bot": start_bot_message,
    "stop_bot": stop_bot_message,
    "star_new_users": star_new_users_message,
    "subscription_try": subscription_try_message,
    "ad_1": ad_1_message,
    "ad_2": ad_2_message,
    "not_command": not_command_message,
    "add_admin": add_admin_message,
    "not_admin_id": not_admin_id_message,
    "edit_hi": edit_hi_message,
    "edit_ad": edit_ad_message,
    "edit_ad_photo": edit_ad_photo_message,
    "malling_time": malling_time_message,
    "malling_text": malling_text_message,

}
