from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from flask import Flask, request
from config import *
import logging
import os


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
server = Flask(__name__)
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.DEBUG)


async def start_on(_):
    print("Бот запущен")
    await bot.send_message(775171777, "abu")


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    # if not bd.user_exists(message.chat.id):
    #     bd.add_user(message.chat.id)
    #     await message.answer("Добро пожаловать")
    #     print(f'Новый пользователь: {message.chat.id}')
    #     return
    name = message.from_user.username
    await message.answer(f"Привет {name}")
    # await message.answer("Давно не виделись")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text[::-1])


# @server.route(f"/{TOKEN}", methods=["POST"])
# def redirect_message():
#     json_string = request.get_data().decode("utf-8")
#     update = telebot.types.Update.de_json(json_string)
#     bot.process_new_updates([update])
#     return "!", 200


if __name__ == "__main__":
    # executor.start_polling(dp, skip_updates=True, on_startup=start_on)
    bot.remote_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
