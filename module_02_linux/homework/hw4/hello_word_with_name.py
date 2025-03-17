"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""

from flask import Flask
from datetime import datetime
app = Flask(__name__)

DAYS_RU = {
    "понедельника", "вторника", "среды", "четверга",
    "пятницы", "субботы", "воскресенья"
}
@app.route('/hello-world/...')
def hello_world(name: str) -> str:
    day = DAYS_RU[datetime.datetime.today().weekday()]
    return f"Привет, {name}. Хорошей {day}!"


if __name__ == '__main__':
    app.run(debug=True)