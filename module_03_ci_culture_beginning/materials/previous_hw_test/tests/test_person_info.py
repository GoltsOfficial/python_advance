import unittest
import datetime
from module_03_ci_culture_beginning.homework.hw4.person import Person  # Импортируем ваш класс Person

class TestPerson(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Метод для установки начальных данных для всех тестов"""
        cls.person = Person(name="John", year_of_birth=1990)

    def test_get_age(self):
        """Тестируем метод get_age"""
        now = datetime.datetime.now()
        expected_age = now.year - 1990  # Возраст должен быть рассчитан правильно
        self.assertEqual(self.person.get_age(), expected_age)

    def test_get_name(self):
        """Тестируем метод get_name"""
        self.assertEqual(self.person.get_name(), "John")

    def test_set_name(self):
        """Тестируем метод set_name"""
        self.person.set_name("Jane")
        self.assertEqual(self.person.get_name(), "Jane")

    def test_set_address(self):
        """Тестируем метод set_address"""
        self.person.set_address("123 Main St")
        self.assertEqual(self.person.get_address(), "123 Main St")

    def test_get_address(self):
        """Тестируем метод get_address"""
        self.person.set_address("456 Elm St")
        self.assertEqual(self.person.get_address(), "456 Elm St")

    def test_is_homeless_when_address_is_set(self):
        """Тестируем is_homeless, когда адрес установлен"""
        self.person.set_address("789 Oak St")
        self.assertFalse(self.person.is_homeless())

    def test_is_homeless_when_address_is_not_set(self):
        """Тестируем is_homeless, когда адрес не установлен"""
        self.person.set_address("")  # Пустой адрес
        self.assertTrue(self.person.is_homeless())

    def test_is_homeless_when_address_is_none(self):
        """Тестируем is_homeless, когда адрес равен None"""
        self.person.set_address(None)
        self.assertTrue(self.person.is_homeless())

if __name__ == "__main__":
    unittest.main()