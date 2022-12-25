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
    await message.reply("тест")




if __name__ == '__main__':
    executor.start_polling(dp)
