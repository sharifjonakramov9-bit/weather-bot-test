import time
import requests
from config import TOKEN

x = "https://home.openweathermap.org"

payload = {
    'key': 'cee5904a2758be014a16512c293688f6'
    'q': 'Samarqand'
}


javob = requests.get(x, params=payload)

print(javob.json())

# boshqatan yana qilmoqchi buldim va bitta print qiganimni bilaman hatto print ham ishlamadi