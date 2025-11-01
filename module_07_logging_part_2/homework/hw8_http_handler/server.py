import json
from flask import Flask, request


app = Flask(__name__)

logs_storage = []


@app.route('/log', methods=['POST'])
def log():
    """
    Записываем полученные логи которые пришли к нам на сервер
    return: текстовое сообщение об успешной записи, статус код успешной работы

    """
    try:
        # Получаем JSON данные из запроса
        log_data = request.get_json()

        if not log_data:
            return "No JSON data provided", 400

        # Добавляем лог в хранилище
        logs_storage.append(log_data)

        print(f"Received log: {log_data}")  # Для отладки

        return "Log received successfully", 200

    except Exception as e:
        print(f"Error processing log: {e}")
        return f"Error: {str(e)}", 500


@app.route('/logs', methods=['GET'])
def logs():
    """
    Рендерим список полученных логов
    return: список логов обернутый в тег HTML <pre></pre>
    """
    # Форматируем логи как красивый JSON
    formatted_logs = json.dumps(logs_storage, indent=2, ensure_ascii=False)

    # Оборачиваем в HTML тег <pre> для красивого отображения
    html_response = f"<pre>{formatted_logs}</pre>"

    return html_response

# TODO запустить сервер
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)