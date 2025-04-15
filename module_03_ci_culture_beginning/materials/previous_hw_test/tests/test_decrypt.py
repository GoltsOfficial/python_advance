import unittest
from module_03_ci_culture_beginning.homework.hw2 import decrypt


class TestDecryptBasic(unittest.TestCase):
    def test_two_dots_removes_one_char(self):
        self.assertEqual(decrypt.decrypt("абраа..-кадабра"), "абра-кадабра")

    def test_two_dots_with_separator(self):
        self.assertEqual(decrypt.decrypt("абраа..-.кадабра"), "абра-кадабра")

    def test_two_dots_after_dashes(self):
        self.assertEqual(decrypt.decrypt("абра--..кадабра"), "абра-кадабра")

    def test_three_dots_removes_one(self):
        self.assertEqual(decrypt.decrypt("абрау...-кадабра"), "абра-кадабра")

    def test_remove_and_add(self):
        self.assertEqual(decrypt.decrypt("абр......a."), "a")


class TestDecryptDotsOnly(unittest.TestCase):
    def test_one_dot_only(self):
        self.assertEqual(decrypt.decrypt("."), "")

    def test_many_dots(self):
        self.assertEqual(decrypt.decrypt("абра........"), "")

    def test_many_dots_only(self):
        self.assertEqual(decrypt.decrypt("1......................."), "")


class TestDecryptMixedInputs(unittest.TestCase):
    def test_digits_mixed(self):
        with self.subTest("Digits and dots"):
            self.assertEqual(decrypt.decrypt("1..2.3"), "23")

        with self.subTest("Letters and digits"):
            self.assertEqual(decrypt.decrypt("a1..2.3"), "a23")

        with self.subTest("Dots before any symbol"):
            self.assertEqual(decrypt.decrypt("..abc"), "abc")

        with self.subTest("Only dots"):
            self.assertEqual(decrypt.decrypt("...."), "")

        with self.subTest("Edge case with no deletions"):
            self.assertEqual(decrypt.decrypt("hello.world"), "helloworld")  # т.к. одна точка


if __name__ == '__main__':
    unittest.main()