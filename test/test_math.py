import unittest
from lib import math


class TestMath(unittest.TestCase):

    def test_math_add(self):
        self.assertEqual(10, math.add(6, 4))
        self.assertEqual(0, math.add(1, -1))
        self.assertEqual(0, math.add(-1, 1))
        self.assertEqual(-2, math.add(-1, -1))


if __name__ == '__main__':
    unittest.main()
