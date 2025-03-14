import datetime
from flask import Flask, jsonify
import random
import re
import os
app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return "Hello World!"

cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
@app.route('/cars')
def cars():
    return cars

cat_breeds  = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
random_cat = random.choice(cat_breeds)
@app.route('/cats')
def get_random_cat():
    return random_cat

current_time = datetime.datetime.now().utcnow()
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
