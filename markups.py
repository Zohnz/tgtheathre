from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')

# ------ Main Menu ------
btnRandom = KeyboardButton('')
btnOther = KeyboardButton('')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom, btnOther)

# -------- Other Menu -------
btnInfo = KeyboardButton('')
btnMoney = KeyboardButton('')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnMoney, btnMain)