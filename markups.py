from telebot import types

def startmarkup(bot, messagge):
	markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	valley = types.KeyboardButton('Волейбол')
	basket = types.KeyboardButton('Баскетбол')
	markup.add(valley, basket)
	bot.send_message(messagge.chat.id, 'Выберите, что хотите парсить', reply_markup=markup)