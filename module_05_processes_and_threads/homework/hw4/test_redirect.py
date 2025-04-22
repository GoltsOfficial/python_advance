import unittest
import sys
from io import StringIO
from redirect import Redirect


class TestRedirect(unittest.TestCase):

    def test_stdout_redirect(self):
        stdout_file = StringIO()
        with Redirect(stdout=stdout_file):
            print("Hello stdout")
        self.assertEqual(stdout_file.getvalue(), "Hello stdout\n")

    def test_stderr_redirect(self):
        stderr_file = StringIO()
        with Redirect(stderr=stderr_file):
            print("Hello stderr", file=sys.stderr)
        self.assertEqual(stderr_file.getvalue(), "Hello stderr\n")

    def test_both_redirect(self):
        stdout_file = StringIO()
        stderr_file = StringIO()
        with Redirect(stdout=stdout_file, stderr=stderr_file):
            print("Hello stdout", file=sys.stdout)
            print("Hello stderr", file=sys.stderr)
        self.assertEqual(stdout_file.getvalue(), "Hello stdout\n")
        self.assertEqual(stderr_file.getvalue(), "Hello stderr\n")

    def test_no_redirect(self):
        stdout_file = StringIO()
        stderr_file = StringIO()
        with Redirect():
            print("Hello stdout")
            print("Hello stderr", file=sys.stderr)
        # Now check the original stdout and stderr
        self.assertEqual(stdout_file.getvalue(), "")
        self.assertEqual(stderr_file.getvalue(), "")

    def test_exception_in_redirect(self):
        stdout_file = StringIO()
        stderr_file = StringIO()
        with self.assertRaises(Exception):
            with Redirect(stdout=stdout_file, stderr=stderr_file):
                print("Hello stdout")
                raise Exception("Test Exception")
        self.assertEqual(stdout_file.getvalue(), "Hello stdout\n")
        self.assertIn("Test Exception", stderr_file.getvalue())  # Ensure exception output is redirected



if __name__ == '__main__':
    unittest.main()
    # with open('test_results.txt', 'a') as test_file_stream:
    #     runner = unittest.TextTestRunner(stream=test_file_stream)
    #     unittest.main(testRunner=runner)
