import telebot 
import config
import markups
from myvollparser import volleyballpars
from mybasketparser import basketballpars
import database
from telebot import types
import schedule
from threading import Thread
from time import sleep
import os
bot = telebot.TeleBot(config.TOKEN)
database.DELETE(TOT_MAX=1000)
database.DELETE(TOT_MAX=2000)

# Изменение фильтров волейбола
def ChangeVoll(message):
	database.DELETE(TOT_MAX=1000)
	database.UPDATEVOLLEY(TOT_MIN=float(message.text.split('@')[0]), TOT_MAX=float(message.text.split('@')[1]))
	bot.send_message(message.chat.id, 'Фильтр изменен')

# Изменение фильтров баскетбола
def ChangeBasket(message):
	database.DELETE(TOT_MAX=2000)
	database.UPDATEBASKET(F_1=float(message.text.split('@')[0]),F_2=float(message.text.split('@')[1]),TOT_MIN=float(message.text.split('@')[2]), TOT_MAX=float(message.text.split('@')[3]))
	bot.send_message(message.chat.id, 'Фильтр изменен')

# Отправка команд боту в телеграм
@bot.message_handler(commands=['start'])
def Welcome(message):
	markups.startmarkup(bot, message)

@bot.message_handler(commands=['volparam'])    # Параметры для волейбола
def vollinfo(message):
	inlinemark = types.InlineKeyboardMarkup(row_width=1)
	changeinfo = types.InlineKeyboardButton('Изменить настройки', callback_data='changevolleyball')
	inlinemark.add(changeinfo)
	bot.send_message(message.chat.id, str(database.vollinfo()['TOT_MIN'])+'@'+str(database.vollinfo()['TOT_MAX']), reply_markup=inlinemark)

@bot.message_handler(commands=['basketparam'])   # Параметры для волейбола
def basketinfo(message):
	inlinemark = types.InlineKeyboardMarkup(row_width=1)
	changeinfo = types.InlineKeyboardButton('Изменить настройки', callback_data='changebasketball')
	inlinemark.add(changeinfo)
	bot.send_message(message.chat.id, str(database.basketinfo()['F_1'])+'@'+ str(database.basketinfo()['F_2'])+'@'+ str(database.basketinfo()['TOT_MIN'])+'@'+ str(database.basketinfo()['TOT_MAX']), reply_markup=inlinemark)

@bot.message_handler(content_types=['text'])   # Кнопки с параметрами
def lalala(message):
	if message.text == 'Волейбол':
		volleyballpars(bot, database.vollinfo()['TOT_MAX'], database.vollinfo()['TOT_MIN'])
	if message.text == 'Баскетбол':
		basketballpars(bot, database.basketinfo()['TOT_MAX'], database.basketinfo()['TOT_MIN'], database.basketinfo()['F_1'], database.basketinfo()['F_2'])
	if message.text == 'Очистить базы матчей':
		database.DELETE(TOT_MAX=1000)
		database.DELETE(TOT_MAX=2000)

# Отправка параметров боту
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.message:
        	if call.data == 'changevolleyball':
        		message = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Введите новые значения вида(totalmin@totalmax)', reply_markup=None)
        		try:
        			bot.register_next_step_handler(message, ChangeVoll)
        		except:
        			bot.send_message(call.message.chat.id, 'Ошибка, попробуйте снова')
        	if call.data == 'changebasketball':
        		message = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Введите новые значения вида(Ф1@Ф2@ТОТмин@ТОТмакс)', reply_markup=None)
        		try:
        			bot.register_next_step_handler(message, ChangeBasket)
        		except:
        			bot.send_message(call.message.chat.id, 'Ошибка, попробуйте снова')

# Парсинг
def startparsing():
	volleyballpars(bot, database.vollinfo()['TOT_MAX'], database.vollinfo()['TOT_MIN'])
	basketballpars(bot, database.basketinfo()['TOT_MAX'], database.basketinfo()['TOT_MIN'], database.basketinfo()['F_1'], database.basketinfo()['F_2'])
schedule.every(float(os.environ.get("TIME"))).minutes.do(startparsing) #для хоста
#schedule.every(2).minutes.do(startparsing) #для теста

# Настройки
def main():
	bot.polling(none_stop=True)
def check():
	while True:
		schedule.run_pending()
		sleep(60)
p1 = Thread(target=main)
p2 = Thread(target=check)
p1.start()
sleep(5)
p2.start()
p1.join()
p2.join()