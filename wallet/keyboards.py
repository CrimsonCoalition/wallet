# Импортируем из библиотеки aiogram все нужное
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



# Кнопка "Кошелёк"
btn_wallet = InlineKeyboardButton

## Кнопка "Пополнить" и кнопка "Вывести"
btn_top_up = InlineKeyboardButton('Пополнить', callback_data='btn_top_up')
btn_withdraw = InlineKeyboardButton('Вывести', callback_data='btn_withdraw')

## Кнопка Рефералы"
btn_referrals = InlineKeyboardButton('Рефералы', callback_data='btn_referrals')

## Кнопка "Уведомления"
btn_notifications = InlineKeyboardButton('🛎 Уведомления', callback_data='btn_notifications')

## Кнопка "Донат"
btn_donate = InlineKeyboardButton('💸 Донат', callback_data='btn_donate')

## Кнопка "Маркет"
btn_market = InlineKeyboardButton('Маркет', callback_data='btn_market')

## Кнопка "Настройки"
btn_settings = InlineKeyboardButton('Настройки', callback_data='btn_settings')


# Клавиатуры
kb_menu = InlineKeyboardMarkup().add(btn_wallet, btn_market, btn_donate, btn_settings)
kb_wallet = InlineKeyboardMarkup().row(btn_top_up, btn_withdraw)
kb_referrals = InlineKeyboardMarkup
kb_notifications = InlineKeyboardMarkup
kb_market = InlineKeyboardMarkup
kb_donate = InlineKeyboardMarkup
kb_settings = InlineKeyboardMarkup().add(btn_notifications, btn_referrals)