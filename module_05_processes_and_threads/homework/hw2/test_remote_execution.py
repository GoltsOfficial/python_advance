import unittest
from remote_execution import app


class CodeExecutionTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  # Отключаем CSRF для тестов
        self.client = app.test_client()

    def test_successful_execution(self):
        response = self.client.post('/run_code', data={
            'code': "print('Hello, world!')",
            'timeout': 2
        }, follow_redirects=True)
        self.assertIn('Hello, world!', response.get_data(as_text=True))

    def test_timeout(self):
        response = self.client.post('/run_code', data={
            'code': "while True: pass",
            'timeout': 1
        }, follow_redirects=True)
        self.assertIn('❌ Время выполнения истекло', response.get_data(as_text=True))

    def test_invalid_timeout(self):
        response = self.client.post('/run_code', data={
            'code': "print('test')",
            'timeout': 999  # вне диапазона
        }, follow_redirects=True)
        self.assertIn('Number must be between 1 and 30', response.get_data(as_text=True))

    def test_empty_code(self):
        response = self.client.post('/run_code', data={
            'code': "",
            'timeout': 5
        }, follow_redirects=True)
        self.assertIn('This field is required', response.get_data(as_text=True))

    def test_unsafe_code(self):
        response = self.client.post('/run_code', data={
            'code': "import os; os.system('echo hello')",
            'timeout': 2
        }, follow_redirects=True)
        self.assertIn('🚫 Небезопасный код обнаружен!', response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
