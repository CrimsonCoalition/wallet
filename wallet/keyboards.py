# импортируем из библиотеки aiogram все нужное.
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Кнопка пополнить средства
inline_btn_1 = InlineKeyboardButton('Пополнить', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

# Кнопка вывести средства
inline_btn_2 = InlineKeyboardButton('Вывести', callback_data='button2')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_2)

# 
inline_btn_3 = InlineKeyboardButton('Отправить', callback_data='button3')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_3)
