'''
    pip install requests
    pip install pyTelegramBotAPI

    Telegram Documentation: https://core.telegram.org/bots/api
    Bot: https://api.telegram.org/bot{API}
    
    Weather webpage: https://openweathermap.org/api
'''
import requests
import telebot
import re
import os
from dotenv import load_dotenv
load_dotenv()


TOKEN = os.getenv('API_TOKEN')
URL = 'https://api.telegram.org/bot'

KEY = os.getenv('WEATHER_KEY')


response = requests.get(f'{ URL }{ TOKEN }/getUpdates')
result = dict(response.json())

chat_id = result['result'][0]['message']['chat']['id']

bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_command_user(message):
    bot.send_message(message.chat.id, 'This is weather bot. Enter: City, state_name (For example: Almaty, kz)')

@bot.message_handler(content_types=['text'])
def send_message_user(message):
    text_user = message.text
    print(text_user)

    pattern = re.compile(r'^[A-Z][a-z]+\,\s+[a-z]{2,3}$')
    matched = pattern.match(text_user)
    if matched:
        import pprint

        temp = matched.group().split(', ')
        city = temp[0]
        code = temp[1]
        
        WEATHER_URL = f'https://api.openweathermap.org/data/2.5/weather?q={city},{code}&appid={KEY}'
        response = requests.get(WEATHER_URL)
        result = response.json()
        # printing weather data json
        pprint.pprint(result)

        # Weather params
        city_name = result['name']
        country = result['sys']['country']
        temp = (result['main']['temp'] - 273.15)
        weather_main = result['weather'][0]['main']
        weather_description = result['weather'][0]['description']
        icon = result['weather'][0]['icon']
        pattern_message = f'City: {city_name}, {country}\nTemperature: {temp:2f}\nDescription: {weather_main} {weather_description}\n{icon}'
        # print(pattern_message)
        bot.send_message(message.chat.id, pattern_message)
    else:
        bot.reply_to(message, 'Could not get location')

@bot.message_handler(content_types=['sticker'])
def send_sticker_user(sticker):
    pass

# for getting updates automatically creates loop
bot.polling()
