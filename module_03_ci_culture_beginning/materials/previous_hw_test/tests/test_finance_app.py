import unittest
from finance_app import app, storage


class TestFinanceApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        cls.client = app.test_client()

    def setUp(self):
        storage.clear()
        storage.update({
            '20250401': [1000, -200],
            '20250402': [500, -100],
        })

    def test_add_valid_data(self):
        response = self.client.post('/add/', json={
            'date': '20250403',
            'amount': 300
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(300, storage['20250403'])

    def test_add_invalid_date_format(self):
        with self.assertRaises(TypeError):
            self.client.post('/add/', json={
                'date': '03-04-2025',
                'amount': 100
            })

    def test_calculate_day(self):
        response = self.client.get('/calculate/?date=20250401')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['total'], 800)

    def test_calculate_all(self):
        response = self.client.get('/calculate/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['total'], 1200)

    def test_calculate_day_no_data(self):
        response = self.client.get('/calculate/?date=20250101')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['total'], 0)

    def test_calculate_all_empty_storage(self):
        storage.clear()
        response = self.client.get('/calculate/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['total'], 0)