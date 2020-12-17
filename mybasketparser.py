from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from time import sleep
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
def basketballpars(bot,TOTAL_MAX, TOTAL_MIN, F_1, F_2):
	url = 'https://betcity.ru/ru/live/basketball'
	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options) #для хоста
	#driver = webdriver.Chrome(chrome_options=chrome_options) #для теста
	driver.get(url)
	driver.implicitly_wait(30)
	sleep(10)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	soup = BeautifulSoup(driver.page_source, 'html.parser')
	items = soup.findAll('div', class_='line__champ')
	for item in items:
		if item.text.split('.')[0] == 'Баскетбол' and item.text.split('.')[3]!=' Статистика':
			game_tittle = item.find('a', class_='line-champ__header-link').find('span').text
			matches = item.findAll('div', class_='line-event line-event_more')
			scores = item.findAll('span', class_='line-event__score-total')
			totals = item.findAll('span', class_='line-event__main-bets-button line-event__main-bets-button_left line-event__main-bets-button_no-value')
			for match in matches:
				try:
					team1 = match.findAll('div', class_='line-event__name-text bold-nowrap-text')[0].text
					team2 = match.findAll('div', class_='line-event__name-text bold-nowrap-text')[1].text
					game_score = match.find('span', class_='line-event__score-total').text
					game_f1 = match.findAll('span', class_='line-event__main-bets-button line-event__main-bets-button_left line-event__main-bets-button_no-value')[0].text
					game_f2 = match.findAll('span', class_='line-event__main-bets-button line-event__main-bets-button_left line-event__main-bets-button_no-value')[1].text
					game_total = match.findAll('span', class_='line-event__main-bets-button line-event__main-bets-button_left line-event__main-bets-button_no-value')[2].text
					if TOTAL_MAX>float(game_total) and float(game_total)>TOTAL_MIN and float(game_f1)>F_1 and float(game_f2)>F_2:
						bot.send_message('@basketballbottest', '*Стартовый тотал*\n*Событие*: '+str(game_tittle)+'\n*Команды*: '+team1+'--vs--'+team2+'\n*Счет*: '+str(game_score)+'\n*TOTAL*:'+str(game_total)+'\n*Ф1*:'+game_f1+'\n*Ф2*:'+game_f2,parse_mode='Markdown')
				except Exception as  e:
					print(e)
			try:
				last_match = item.find('div', class_='line-event line-event_more line-event_last')
				team1 = last_match.findAll('div', class_='line-event__name-text bold-nowrap-text')[0].text
				team2 = last_match.findAll('div', class_='line-event__name-text bold-nowrap-text')[1].text
				game_f1 = last_match.findAll('span', class_='line-event__main-bets-button line-event__main-bets-button_left line-event__main-bets-button_no-value')[0].text
				game_f2 = last_match.findAll('span', class_='line-event__main-bets-button line-event__main-bets-button_left line-event__main-bets-button_no-value')[1].text
				game_score = last_match.find('span', class_='line-event__score-total').text
				game_total = last_match.findAll('span', class_='line-event__main-bets-button line-event__main-bets-button_left line-event__main-bets-button_no-value')[2].text
				if TOTAL_MAX>float(game_total) and float(game_total)>TOTAL_MIN and float(game_f1)>F_1 and float(game_f2)>F_2:
						bot.send_message('@basketballbottest', '*Стартовый тотал*\n*Событие*: '+str(game_tittle)+'\n*Команды*: '+team1+'--vs--'+team2+'\n*Счет*: '+str(game_score)+'\n*TOTAL*:'+str(game_total)+'\n*Ф1*:'+game_f1+'\n*Ф2*:'+game_f2,parse_mode='Markdown')
			except Exception as  e:
					print(e)
	driver.quit()