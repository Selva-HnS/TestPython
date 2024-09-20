# tests/test_addition.py

import unittest
from src.math_functions import add
import HtmlTestRunner

class TestAddition(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertNotEqual(add(1, 1), 3)

if __name__ == '__main__':
    #unittest.main()
    try:
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test-reports'))
    except Exception as e:
        print(f"An error occurred: {e}")
