import unittest
from block_errors import BlockErrors


class TestBlockErrors(unittest.TestCase):
    def test_ignore_allowed_error(self):
        try:
            with BlockErrors({ZeroDivisionError}):
                _ = 1 / 0
        except ZeroDivisionError:
            self.fail("ZeroDivisionError не должен был быть поднят")

    def test_raises_unexpected_error(self):
        with self.assertRaises(TypeError):
            with BlockErrors({ZeroDivisionError}):
                _ = 1 / '0'

    def test_nested_blocks(self):
        try:
            with BlockErrors({TypeError}):
                with BlockErrors({ZeroDivisionError}):
                    _ = 1 / '0'
                print("Внутренний блок завершён без ошибок")
        except TypeError:
            self.fail("TypeError должен был быть подавлен внешним блоком")

    def test_subclass_of_exception(self):
        try:
            with BlockErrors({Exception}):
                _ = 1 / '0'  # TypeError будет подавлен
        except Exception:
            self.fail("Exception должен был быть подавлен")

    def test_raise_when_not_in_list(self):
        with self.assertRaises(ZeroDivisionError):
            with BlockErrors({TypeError}):
                _ = 1 / 0


if __name__ == '__main__':
    unittest.main()
