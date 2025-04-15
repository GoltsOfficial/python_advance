import unittest
from calendar import weekday
from datetime import datetime

from module_03_ci_culture_beginning.materials.previous_hw_test.hello_word_with_day import app


class TestMaxNumberApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_greeting_includes_username_and_weekday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()

        # Проверка, что имя пользователя есть в ответе
        self.assertIn(username, response_text)

        # Список приветствий по дням недели
        greetings = [
            'Хорошего понедельника',
            'Хорошего вторника',
            'Хорошей среды',
            'Хорошего четверга',
            'Хорошей пятницы',
            'Хорошей субботы',
            'Хорошего воскресенья'
        ]

        # Получаем текущий день недели и соответствующее приветствие
        weekday_index = datetime.today().weekday()
        expected_greeting = greetings[weekday_index]

        # Проверка, что приветствие на текущий день есть в ответе
        self.assertIn(expected_greeting, response_text)