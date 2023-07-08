from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')

btnOnline = KeyboardButton('Спектакль онлайн')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOnline)

