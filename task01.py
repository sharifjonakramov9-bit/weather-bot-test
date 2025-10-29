import time
import requests
from config import TOKEN


WEATHER_URL = "https://home.openweathermap.org"
TG_BO_BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

last_update_id = 0

ALLOWED_CITIES = ['toshkent', 'samarqand', 'jizzax']

def get_last_update():
    global last_update_id
    get_updates_url = f"{TG_BO_BASE_URL}/getUpdates"

    response = requests.get(get_updates_url, params={"offset": last_update_id + 1})
    data = response.json()

    if data["result"]:
        update = data["result"][-1]
        last_update_id = update["update_id"]
        return update
    return None


def send_message(chat_id, text):
    send_message_url = f"{TG_BO_BASE_URL}/sendMessage"

    requests.get(send_message_url, params={"chat_id": chat_id, "text": text})


def get_current_weather(city):
    get_current_wather_url = f"{WEATHER_URL}/current.json"

    payload = {
        'key': 'cee5904a2758be014a16512c293688f6',
        'q': city
    }
    response = requests.get(get_current_wather_url, params=payload)

    data = response.json()
    if "error" in data:
        return None

    return data['current']['feelslike_c']


while True:
    last_update = get_last_update()
    if last_update:
        chat_id = last_update['message']['chat']['id']

        text = last_update['message']['text'].lower()

        if text == '/start':
            send_message(chat_id, 'Salom! Xush kelibsiz')
        elif text in ALLOWED_CITIES:
            weather = get_current_weather(text)
            if weather is None:
                send_message(chat_id, "Shahar nomini to'g'ri yozing!")
            else:
                send_message(chat_id, f"Hozir {text} da ob-havo {weather}")
        else:
            send_message(chat_id, f"Bu shahar ro'yxatda yo'q iltimos {ALLOWED_CITIES} ni birini tanlang!")

    time.sleep(1)

