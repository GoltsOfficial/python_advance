"""
Напишите GET-эндпоинт /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:

/ps?arg=a&arg=u&arg=x
"""
from flask import Flask, request
import subprocess
import platform

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps():
    args = request.args.getlist("arg")

    if platform.system() == "Windows":
        # Выполним команду через cmd и установим кодировку UTF-8
        command = ["cmd", "/c", "chcp 65001 > nul && tasklist"]
    else:
        command = ["ps"] + args

    try:
        result = subprocess.check_output(
            " ".join(command),
            shell=True,
            encoding="utf-8",
            errors="ignore"
        )
        return f"<pre>{result}</pre>"
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e}", 400

if __name__ == "__main__":
    app.run(debug=True)
