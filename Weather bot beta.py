import os
import time
import telebot
import requests
import schedule
import threading
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from telebot import types

load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
geolocator = Nominatim(user_agent="my_app")

mode = 'every_minute'
chat_id = None


#  Получение погоды с api.open-meteo.com
def get_weather():
    location = 'Moscow'
    geocoder = geolocator.geocode(location)
    latitude = geocoder.latitude
    longitude = geocoder.longitude
    url = f'https://api.open-meteo.com/v1/forecast?current_weather=true&latitude={latitude}&longitude={longitude}'
    response = requests.get(url)
    data = response.json()
    temperature = data['current_weather']['temperature']
    weathercode = data['current_weather']['weathercode']
    precipitation_strings = {
        0: 'ясно',
        1: 'слабый дождь',
        2: 'умеренный дождь',
        3: 'сильный дождь',
        10: 'гроза',
        45: 'туман',
        48: 'морось',
        51: 'слабый снег',
        52: 'умеренный снег',
        53: 'сильный снег',
        56: 'ледяной дождь',
        57: 'сильный ледяной дождь',
        61: 'слабый дождь со снегом',
        62: 'умеренный дождь со снегом',
        63: 'сильный дождь со снегом',
        65: 'слабый снег с дождем',
        66: 'умеренный снег с дождем',
        67: 'сильный снег с дождем',
        71: 'слабый снег',
        72: 'умеренный снег',
        73: 'сильный снег',
        75: 'сильный снег с ветром',
        77: 'снег с градом',
        80: 'слабый дождь',
        81: 'умеренный дождь',
        82: 'сильный дождь',
        85: 'сильный дождь с градом',
        86: 'сильный дождь с грозой',
    }
    precipitation = precipitation_strings.get(weathercode, 'неизвестно')
    return f'Сейчас такая погода в Москве: температура - {temperature}°C, осадки - {precipitation}'


#  Функция, позволяющая отпрвлять информацию, полученную с api.open-meteo.com
def send_weather_message(chat_idf):
    weather_data = get_weather()
    bot.send_message(chat_idf, weather_data)


#  Кнопки режима
keyboard1 = types.ReplyKeyboardMarkup(row_width=2)
botton1 = types.KeyboardButton('Каждую минуту')
botton2 = types.KeyboardButton('Каждый час')
botton3 = types.KeyboardButton('Каждые 5 часов')
botton4 = types.KeyboardButton('Выключить уведомления')
keyboard1.add(botton1, botton2, botton3, botton4)
types.ReplyKeyboardMarkup(True, True)


#  Старт программы
@bot.message_handler(commands=['start'])
def send_welcome(message):
    global chat_id
    chat_id = message.chat.id
    bot.send_message(chat_id, f'Привет! Я буду отсылать тебе температуру в Москве. У меня есть несколько режимов.\
Можешь ознакомиться со всеми режимами чуть ниже. Сейчас режим стоит: Каждые 5 секунд', reply_markup=keyboard1)
    print(message)
    schedule.every(5).seconds.do(send_weather_message, chat_id).tag('weather_message')


#  Выбор режима
@bot.message_handler(func=lambda message: True)
def choose_mode(message):
    global mode
    chat_idd = message.chat.id
    if message.text == 'Каждую минуту':
        mode = 'Every minute'
        bot.send_message(chat_idd, 'Режим изменён на: Каждую минуту.')
        schedule.clear('weather_message')
        schedule.every(1).minutes.do(send_weather_message, chat_id).tag('weather_message')
        print(mode)
    elif message.text == 'Каждый час':
        mode = 'Every hour'
        bot.send_message(chat_idd, 'Режим изменён на: Каждый час.')
        schedule.clear('weather_message')
        schedule.every(1).hours.do(send_weather_message, chat_id).tag('weather_message')
        print(mode)
    elif message.text == 'Каждые 5 часов':
        mode = 'Каждые 5 часов'
        bot.send_message(chat_idd, 'Режим изменён на: Каждые 5 часов.')
        schedule.clear('weather_message')
        schedule.every(5).hours.do(send_weather_message, chat_id).tag('weather_message')
        print(mode)
    elif message.text == 'Выключить уведомления':
        mode = 'disabled'
        bot.send_message(chat_idd, 'Уведомления выключены.')
        schedule.clear('weather_message')
        print(mode)


# Для проверки работы библиотеки schedule
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


#  Проврека работы задач из библиотеки schedule
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.daemon = True
scheduler_thread.start()

#  Нужно, чтобы бот был на связи и не выключался после выполнения своей функции
bot.polling(none_stop=True)
