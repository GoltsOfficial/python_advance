import datetime
from flask import Flask, jsonify
import random
import re
import os
app = Flask(__name__)


@app.route('/hello_world')
def test_function():
    return "Hello World!"


@app.route('/cars')
def test_function():
    cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
    return cars

cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
@app.route('/cats')
def test_function():
    random_cat = random.randit(cats[0],cats[4])
    return random_cat


@app.route('/get_time/now')
def test_function():
    current_time = datetime.datetime.now().utcnow()
    return print(f'Точное время: {current_time}')


@app.route('/get_time/future')
def test_function():
    current_time = datetime.datetime.now().utcnow()
    current_time_after_hour = current_time + datetime.timedelta(hours=1)
    return print(f'Точное время: {current_time_after_hour}')


@app.route('/get_random_word')
def test_function():
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


@app.route('/counter')
def test_function():
    pass


if __name__ == '__main__':
    app.run(debug=True)
