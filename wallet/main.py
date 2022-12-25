'''
                .__  .__          __   
__  _  _______  |  | |  |   _____/  |_ 
\ \/ \/ /\__  \ |  | |  | _/ __ \   __\
 \     /  / __ \|  |_|  |_\  ___/|  |   
  \/\_/  (____  /____/____/\___  >__|  
              \/               \/      
                                     by Commit404 & salobchyanskiy
'''


# Импорты / Imports
import requests
import time
import copy
import random
import os
import json
from config import token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import config


client = Bot(token=token)
dp = Dispatcher(client)

# Приветствие / Welcome
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("👋 Привет, {message.from_user.full_name}! я *Crimson Coalition Wallet* - Мультивалютный криптокошелек в Telegram. Покупайте, продавайте, храните и платите криптовалютой когда хотите. Подписывайтесь на наш канал @CrimsonCoalition. 💰.\nВаш мультивалютный кошелек создан и вы можете начать пользование системой 🛠. ")

 # Wallet / Кошелек
@dp.message_handler(commands=["wallet"])
async def start_command(message: types.Message):
    await message.reply("{0.first_name}, это ваш счет:", reply_markup=inline_kb1)
    
# Settings / Настройки
@dp.message_handler(commands=["settings"])
async def start_command(message: types.Message):
  await message.reply("{0.first_name}, Добро пожаловать в настройки:")

# Делаем так чтобы бот работал постоянно
if __name__ == '__main__':
    executor.start_polling(dp)
