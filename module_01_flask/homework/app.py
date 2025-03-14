import datetime
from flask import Flask, jsonify
import random
import re
import os
app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return "Hello World!"


@app.route('/cars')
def cars():
    cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
    return cars

cat_breeds  = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
@app.route('/cats')
def get_random_cat():
    random_cat = random.choice(cat_breeds)
    return random_cat

current_time = datetime.datetime.now().utcnow()
@app.route('/get_time/now')
def get_time_now():
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = current_time + datetime.timedelta(hours=1)
    return f'Точное время: {current_time_after_hour}'


@app.route('/get_random_word')
def get_random_word():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

    # Загружаем текст книги один раз при старте приложения
    with open(BOOK_FILE, 'r', encoding='utf-8') as book:
        book_text = book.read()

    # Функция для получения списка слов из текста
    def get_word_list(text):
        # Используем регулярное выражение для получения слов
        words = re.findall(r'\b\w+\b', text)
        return words

    # Получаем список слов
    word_list = get_word_list(book_text)

    @app.route('/get_random_word')
    def get_random_word():
        # Получаем случайное слово из списка
        random_word = random.choice(word_list)
        return jsonify({'word': random_word})

visits = 0
@app.route('/counter')
def counter():
    global visits
    visits += 1
    return f'Количество посещений: {visits}'




if __name__ == '__main__':
    app.run(debug=True)
