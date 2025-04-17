"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from hw1_registration import app


class RegistrationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Настройка тестового клиента для Flask"""
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False  # Отключаем CSRF защиту
        cls.client = app.test_client()

    def post_registration_data(self, data):
        """Отправка данных в форму с fake CSRF токеном"""
        data['csrf_token'] = 'fake_csrf_token'  # fake CSRF токен
        return self.client.post("/registration", data=data)

    def test_valid_data(self):
        data = {
            'email': 'test@example.com',
            'phone': '1234567890',
            'name': 'Test User',
            'address': 'Test Address',
            'index': '123456',
            'comment': ''
        }
        response = self.post_registration_data(data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Successfully registered user test@example.com', response.data)

    def test_invalid_email(self):
        data = {
            'email': 'invalid-email',
            'phone': '1234567890',
            'name': 'Test User',
            'address': 'Test Address',
            'index': '123456',
            'comment': ''
        }
        response = self.post_registration_data(data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid input', response.data)

    def test_empty_name(self):
        data = {
            'email': 'test@example.com',
            'phone': '1234567890',
            'name': '',
            'address': 'Test Address',
            'index': '123456',
            'comment': ''
        }
        response = self.post_registration_data(data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid input', response.data)

    def test_valid_phone(self):
        data = {
            'email': 'test@example.com',
            'phone': '1234567890',
            'name': 'Test User',
            'address': 'Test Address',
            'index': '123456',
            'comment': ''
        }
        response = self.post_registration_data(data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_phone(self):
        data = {
            'email': 'test@example.com',
            'phone': '123',
            'name': 'Test User',
            'address': 'Test Address',
            'index': '123456',
            'comment': ''
        }
        response = self.post_registration_data(data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid input', response.data)

if __name__ == "__main__":
    unittest.main()