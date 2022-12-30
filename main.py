"""
                .__  .__          __
__  _  _______  |  | |  |   _____/  |_
\ \/ \/ /\__  \ |  | |  | _/ __ \   __\
 \     /  / __ \|  |_|  |_\  ___/|  |
  \/\_/  (____  /____/____/\___  >__|
              \/               \/
                                     by Commit404 & salobchyanskiy
"""

# Импорты / Imports
import requests
import time
import copy
import random
import os
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
import logging
import sqlite3
from config import token, admin
from keyboards import kb_menu, btn_wallet, btn_market, btn_donate, \
    kb_wallet, btn_top_up, btn_withdraw, \
    kb_referrals, btn_referrals, \
    kb_notifications, btn_notifications, \
    kb_donate, btn_donate, \
    kb_market, btn_market, \
    kb_settings, btn_settings, \
    kb_admin, btn_mailing # Импорты клавиатур и кнопок



client = Bot(token=token)
dp = Dispatcher(client)


logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)



# Приветствие / Welcome
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply(
        f"👋 Привет, {message.from_user.full_name}! Я *Crimson Coalition Wallet* - Мультивалютный криптокошелек в Telegram."
        f" Покупайте, продавайте, храните и платите криптовалютой когда хотите."
        f" Подписывайтесь на наш канал @CrimsonCoalition 💰"
        f"\nВаш мультивалютный кошелек создан и вы можете начать пользование системой 🛠", reply_markup=kb_menu)


# Wallet / Кошелек
@dp.message_handler(commands=["wallet"])
async def wallet_command(message: types.Message):
    await message.reply(f"{message.from_user.full_name}, это ваш счет:", reply_markup=kb_wallet)


# Settings / Настройки
@dp.message_handler(commands=["settings"])
async def settings_command(message: types.Message):
    await message.reply(f"{message.from_user.full_name}, Добро пожаловать в настройки:", reply_markup=kb_settings)


# Donate / Донат
@dp.message_handler(commands=["donate"])
async def donate_command(message: types.Message):
    await message.reply(
        f"{message.from_user.full_name}, мы постоянно занимаемся развитием этого проекта и стараемся делать регулярные обновления, если тебе нравится этот кошелек - отправь любую сумму пожертвования разработчикам на кофе:",
        reply_markup=kb_donate)


# Admin / Админка
@dp.message_handler(commands=["admin"])
async def adm_start_command(message: types.Message):
    if message.from_user.id == admin:
        await message.reply('Добро пожаловать в Админ-Панель!', reply_markup=kb_admin)
    else:
        await message.reply(f"{message.from_user.full_name}, ты не админ")

# Market / Маркет
@dp.message_handler(commands=["market"])
async def market_command(message: types.Message):
    await message.reply(
        "💠 Здесь вы можете купить или продать криптовалюту с помощью перевода на карту или электронный кошелёк.")


# Делаем так, чтобы бот работал постоянно
if __name__ == '__main__':
    executor.start_polling(dp)
