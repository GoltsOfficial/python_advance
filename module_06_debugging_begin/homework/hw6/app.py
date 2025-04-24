"""
Заменим сообщение "The requested URL was not found on the server" на что-то более информативное.
Например, выведем список всех доступных страниц с возможностью перехода по ним.

Создайте Flask Error Handler, который при отсутствии запрашиваемой страницы будет выводить
список всех доступных страниц на сайте с возможностью перехода на них.
"""

from flask import Flask, url_for, render_template, request
app = Flask(__name__)


@app.route('/dogs')
def dogs():
    return f'''
        <h1>Страница с пёсиками<h1>
        <button onclick="window.history.back()">Вернуться назад</button>
    '''


@app.route('/cats')
def cats():
    return '''
        <h1>Страница с котиками</h1>
        <button onclick="window.history.back()">Вернуться назад</button>
    '''


@app.route('/cats/<int:cat_id>')
def cat_page(cat_id: int):
    return f'''
        <h1>Страница с котиком {cat_id}</h1>
        <button onclick="window.history.back()">Вернуться назад</button>
    '''


@app.route('/index')
def index():
    return f'''
        <h1>Главная страница</h1>
        <button onclick="window.history.back()">Вернуться назад</button>
    '''


@app.errorhandler(404)
def page_not_found(e):
    routes = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods:
            defaults = {arg: 1 for arg in rule.arguments}
            try:
                url = url_for(rule.endpoint, **defaults)
                routes.append((rule.endpoint, url))
            except Exception:
                pass

    routes.sort(key=lambda x: x[0])

    return render_template('404_error.html', routes=routes), 404


if __name__ == '__main__':
    app.run(debug=True)
