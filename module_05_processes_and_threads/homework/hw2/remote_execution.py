"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, что исполнение кода не уложилось в данное время.
"""

from flask import Flask, request, render_template_string
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from subprocess import Popen, PIPE, TimeoutExpired
import tempfile
import os

app = Flask(__name__)
app.secret_key = 'secret'


class CodeForm(FlaskForm):
    code = StringField("Код", validators=[DataRequired()])
    timeout = IntegerField("Тайм-аут (сек)", validators=[DataRequired(),
                                                         NumberRange(min=1, max=10)])


def run_python_code_in_subproccess(code: str, timeout: int) -> str:
    with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False) as f:
        f.write(code)
        filename = f.name

    try:
        process = Popen(
            ['prlimit', '--nproc=1:1', 'python3', filename],
            stdout=PIPE,
            stderr=PIPE,
            text=True
        )
        stdout, stderr = process.communicate(timeout=timeout)
        return f"Вывод:\n{stdout}\nОшибки:\n{stderr}"
    except TimeoutExpired:
        process.kill()
        stdout, stderr = process.communicate()
        return f"❌ Время выполнения истекло\nЧастичный вывод:\n{stdout}\nОшибки:\n{stderr}"
    finally:
        os.remove(filename)


@app.route('/run_code', methods=['GET','POST'])
def run_code():
    form = CodeForm()
    result = None
    if form.validate_on_submit():
        code = form.code.data
        timeout = form.timeout.data

        if 'shell=' in code or '__import__' in code or 'os.system' in code:
            result = "🚫 Небезопасный код обнаружен!"
        else:
            result = run_python_code_in_subproccess(code, timeout)

    return render_template_string('''
        <form method="post">
            {{ form.hidden_tag() }}
            <p>{{ form.code.label }}<br>{{ form.code(rows=10, cols=60) }}</p>
            <p>{{ form.timeout.label }}<br>{{ form.timeout() }}</p>
            <p><input type="submit" value="Выполнить код"></p>
        </form>

        {% if result %}
        <h3>Результат выполнения:</h3>
        <pre>{{ result }}</pre>
        {% endif %}
        ''', form=form, result=result)


if __name__ == '__main__':
    app.run(debug=True)
