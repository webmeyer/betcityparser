# Настройка кнопока для интерфейса бота

from telebot import types

def startmarkup(bot, messagge):
	markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	valley = types.KeyboardButton('Волейбол')
	basket = types.KeyboardButton('Баскетбол')
	delete = types.KeyboardButton('Очистить базы матчей')
	markup.add(valley, basket, delete)
	bot.send_message(messagge.chat.id, 'Выберите, что хотите парсить', reply_markup=markup)