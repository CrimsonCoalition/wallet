# Импортируем из библиотеки aiogram все нужное
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Кнопка "Пополнить"
inline_btn_1 = InlineKeyboardButton('Пополнить', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

# Кнопка "Вывести"
inline_btn_2 = InlineKeyboardButton('Вывести', callback_data='button2')
inline_kb2 = InlineKeyboardMarkup().add(inline_btn_2)

# Кнопка "Отправить"
inline_btn_3 = InlineKeyboardButton('Отправить', callback_data='button3')
inline_kb3 = InlineKeyboardMarkup().add(inline_btn_3)

## Кнопка Рефералы в разделе "Рефералы"
inline_btn_4 = InlineKeyboardButton('Рефералы', callback_data='button4')
inline_kb4 = InlineKeyboardMarkup().add(inline_btn_4)

## Кнопка Уведомления в разделе "Настройки"
inline_btn_5 = InlineKeyboardButton('🛎 Уведомления', callback_data='button5')
inline_kb5 = InlineKeyboardMarkup().add(inline_btn_5)

## Кнопка "Донат"
inline_btn_6 = InlineKeyboardButton('💸 Донат', callback_data='button6')
inline_kb6 = InlineKeyboardMarkup().add(inline_btn_6)

## Кнопка "Маркет"
inline_btn_7 = InlineKeyboardButton('Маркет', callback_data='button7')
inline_kb7 = InlineKeyboardMarkup().add(inline_btn_7)
