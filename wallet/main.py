'''
                .__  .__          __   
__  _  _______  |  | |  |   _____/  |_ 
\ \/ \/ /\__  \ |  | |  | _/ __ \   __\
 \     /  / __ \|  |_|  |_\  ___/|  |   
  \/\_/  (____  /____/____/\___  >__|  
              \/               \/      
                                     by Commit404 & salobchyanskiy
'''


# Imports
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


client = Bot(token=token)
dp = Dispatcher(client)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет, {0.first_name}! я *Crimson Coalition Wallet* - Мультивалютный криптокошелек в Telegram. Покупайте, продавайте, храните и платите криптовалютой когда хотите. Подписывайтесь на наш канал @CrimsonCoalition. 💰.\nВаш мультивалютный кошелек создан и вы можете начать пользование системой 🛠. ")




if __name__ == '__main__':
    executor.start_polling(dp)
