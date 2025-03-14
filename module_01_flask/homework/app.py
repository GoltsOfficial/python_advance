import datetime
from flask import Flask
import random
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
    pass


@app.route('/get_random_word')
def test_function():
    pass


@app.route('/counter')
def test_function():
    pass


if __name__ == '__main__':
    app.run(debug=True)
