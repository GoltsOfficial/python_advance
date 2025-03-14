import datetime

import pytz
from flask import Flask, jsonify
import random
import re
import os
app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return "Hello World!"

cars_brands = ['Chevrolet', 'Renault', 'Ford', 'Lada']
@app.route('/cars')
def print_cars():
    return ', '.join(cars_brands)

cat_breeds  = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
@app.route('/cats')
def get_random_cat():
    random_cat = random.choice(cat_breeds)
    return random_cat

utc_0 = datetime.datetime.now().utcnow()
utc_plus_3 = pytz.timezone('Europe/Moscow')  # Например, Московское время
# Переводим текущее время в UTC+3
current_time = utc_0.replace(tzinfo=pytz.utc).astimezone(utc_plus_3)
@app.route('/get_time/now')
def get_time_now():
    return f'Точное время: {current_time}'

current_time_after_hour = current_time + datetime.timedelta(hours=1)
@app.route('/get_time/future')
def get_time_future():
    return f'Точное время: {current_time_after_hour}'

with open('war_and_peace.txt', 'r', encoding='utf-8') as book:
    words = re.findall(r'\b\w+\b', book.read())  # Достаём все слова из файла
@app.route('/get_random_word')
def get_random_word():
    return random.choice(words) if words else "Файл пуст"

visits = 0
@app.route('/counter')
def counter():
    global visits
    visits += 1
    return f'Количество посещений: {visits}'




if __name__ == '__main__':
    app.run(debug=True)
