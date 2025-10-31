import time
import requests
from config import TOKEN

TG_BO_BASE_URL = f'https://api.telegram.org/bot{TOKEN}'
WEATHER_URL = 'http://api.weatherapi.com/v1'


def get_last_update():
    get_updates_url = f"{TG_BO_BASE_URL}/getUpdates"

    response = requests.get(get_updates_url)
    data = response.json()

    return data['result'][-1]


def send_message(chat_id, text):
    send_message_url = f"{TG_BO_BASE_URL}/sendMessage"

    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.get(send_message_url, params=payload)


def get_current_weather(city):
    get_current_wather_url = f"{WEATHER_URL}/current.json"

    payload = {
        'key': 'c852ebca46f148469f3172212250707',
        'q': city
    }
    response = requests.get(get_current_wather_url, params=payload)

    print(response.json())
    data = response.json()
    return data['current']['feelslike_c']


while True:
    last_update = get_last_update()
    text = last_update['message']['text']

    if text == '/start':
        send_message(last_update['message']['chat']['id'], 'salom')
    elif text in ['toshkent', 'samarqand', 'jizzax']:
        weather = get_current_weather(text)
        text = f"Hozir {text} da ob-havo {weather}"
        send_message('1258594598', text)

    time.sleep(3)

