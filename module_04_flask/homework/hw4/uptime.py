"""
Напишите GET-эндпоинт /uptime, который в ответ на запрос будет выводить строку вида f"Current uptime is {UPTIME}",
где UPTIME — uptime системы (показатель того, как долго текущая система не перезагружалась).

Сделать это можно с помощью команды uptime.
"""
import time
from datetime import timedelta, datetime

import psutil
from flask import Flask
from psutil import boot_time

app = Flask(__name__)


@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    boot_time = psutil.boot_time()

    uptime_seconds = time.time() - boot_time

    uptime_timedelta = timedelta(seconds=uptime_seconds)

    uptime_correct_format = str(uptime_timedelta)

    current_time = datetime.now().strftime("%Y")  # Текущий год

    response = f"Current uptime is {uptime_correct_format} {current_time}"

    return response

if __name__ == '__main__':
    app.run(debug=True)
