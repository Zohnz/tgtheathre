import config as cfg
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)
from db import Database
import functions as fc
import markups as nav
import random

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)
db = Database('database.db')

with open('quotes.txt', 'r') as file:
    quotes = file.readlines()

@dp.message_handler(commands=['quote'])
async def send_random_quote(message: types.Message):
    random_quote = random.choice(quotes)
    await message.reply(random_quote)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет {0.first_name} введи свой вопрос".format(message.from_user),
                           reply_markup=nav.mainMenu)


@dp.message_handler()
async def mess(message: types.Message):
    answer_id = fc.recognize_question(message.text, db.get_questions())
    await bot.send_message(message.from_user.id, db.get_answer(answer_id))


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Число удачи':
        await bot.send_message(message.from_user.id, 'Ваше удачное число на день: ' + str(random.randint(1, 10)))

    # elif message.text == '':
    #     await bot.send_message(message.from_user.id, '', reply_markup + nav.mainMenu)
    #
    # elif message.text == '':
    #     await bot.send_message(message.from_user.id, '', reply_markup + nav.otherMenu)
    #
    # elif message.text == '':
    #     await bot.send_message(message.from_user.id, '')
    #
    # elif message.text == '':
    #     await bot.send_message(message.from_user.id, '')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
