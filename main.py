import config as cfg
import logging
from aiogram import Bot, Dispatcher, executor, types
from background import keep_alive

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


with open('books.txt', 'r') as file:
    books = file.readlines()


@dp.message_handler(commands=['book'])
async def send_random_book(message: types.Message):
    random_book = random.choice(books)
    await message.reply(random_book)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Привет! Данный бот предлагает погрузиться в театральную атмосферу и заглянуть в закулисье. С помощью команды /quote Вы можете получить любую цитату о театре, а также задать любой вопрос боту напрямую.".format(
                               message.from_user),
                           reply_markup=nav.btnMain)


@dp.message_handler()
async def mess(message: types.Message):
    answer_id = fc.recognize_question(message.text, db.get_questions())
    await bot.send_message(message.from_user.id, db.get_answer(answer_id))


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Спектакль онлайн}':
        await bot.send_message(message.from_user.id,
                               "Для того, чтобы посмотреть знаменитые спектакли не выходя из дома рекомендуем Вам сервис https://www.mos.ru/city/projects/kulturaonline/theatre/ ! Теперь не нужно ездить в другой город и тратить деньги. Приятного просмотра!".format(
                                   message.from_user),
                               reply_markup=nav.btnOnline)


keep_alive()
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

