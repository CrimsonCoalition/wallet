# Donate / Донат 

#
#
#

# Imports / Импорты
import asyncio
import logging

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType

from config import BOT_TOKEN, PAYMENTS_PROVIDER_TOKEN, TIME_MACHINE_IMAGE_URL


logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO)

loop = asyncio.get_event_loop() # Получаем текущий event loop. Тоесть запускаем работу нужных нам процессов.
bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot, loop=loop)

## Устанавливаем цену.
PRICE = types.LabeledPrice(label='Поддержать разработку', amount=50)
