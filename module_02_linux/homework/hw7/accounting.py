"""
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""

from flask import Flask

app = Flask(__name__)


storage = {}

def calculate(year: int, month: int = None) -> int:
    key_prefix = f"{year}" if month is None else f"{year}{month:02}"
    return sum(v for k, v in storage.items() if k.startswith(key_prefix))

@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    storage[date] = storage.get(date, 0) + number
    return f"Добавлено {number} рублей за {date}"

@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    return f"Сумма за {year}: {calculate(year)} рублей"

@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    return f"Сумма за {year}-{month}: {calculate(year, month)} рублей"

if __name__ == "__main__":
    app.run(debug=True)