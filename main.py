"""

 __      __        .__  .__          __    
/  \    /  \_____  |  | |  |   _____/  |_ 
\   \/\/   /\__  \ |  | |  | _/ __ \   __\  by @CrimsonCoalition
 \        /  / __ \|  |_|  |_\  ___/|  |  
  \__/\  /  (____  /____/____/\___  >__|  
       \/        \/               \/      

"""

# Imports
import logging
import json
import random
import codecs
import redis
import os
import importlib

import aiogram
import jinja2


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level = logging.INFO)

# Создаем класс Bot
class Bot:
    def __init__(self, bot_name="super-bot", debug=False):
        self.logger = logging.getLogger(bot_name)
        self.logger.info("Запускаю бота.../")

        self.handlers = {}
        self.debug = debug
        self.callback_handlers = {}

        self.logger.info("Загружаю config.../")
        self.admin = int(os.environ["ADMIN"])
        self.const = {}
        self.const.update(json.loads(codecs.open("config/init.json", "r", "utf-8").read()))
        self.const["messages"] = json.loads(codecs.open("config/messages.json", "r", "utf-8").read())
        self.const["keyboards"] = json.loads(codecs.open("config/keyboards.json", "r", "utf-8").read())

        self.logger.info("Подключаюсь к Telegram.../")
        self.telegram = telebot.TeleBot(os.environ["BOT_TOKEN"])
        self.telegram.set_update_listener(self.proсess_updates)

        self.redis = redis.from_url(os.environ.get("REDIS_URL","redis://localhost:6379"))
        self.data = {}

        self.logger.info("Собираю модули.../")
        self._collect_modules()

        self.logger.info("Готов!")

    def _collect_modules(self):
        for module_name in os.listdir("modules"):
            if module_name.endswith(".py"):
                module = importlib.import_module("modules.%s" % module_name[:-3])
                module.init(self)
