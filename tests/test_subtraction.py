# tests/test_subtraction.py

import unittest
from src.math_functions import subtract
import HtmlTestRunner

class TestSubtraction(unittest.TestCase):

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 1), -1)
        self.assertNotEqual(subtract(2, 2), 1)

if __name__ == '__main__':
    #unittest.main()
	try:
		unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test-reports'))
	except Exception as e:
		print(f"An error occurred: {e}")