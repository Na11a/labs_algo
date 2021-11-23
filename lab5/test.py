import unittest
from max_flow import *


class Test(unittest.TestCase):
    def test_max_flow(self):
        self.assertEqual(get_max_flow([[20, 0, 1], [30, 0, 1], [10, 0, 1]]), 10)

    def test_get_max_vertex(self):
        self.assertEqual(get_max_vertex(2,[
            [[0, 0, 1], [10, 10, 1], [10, 20, 1], [10, 0, 1], [0, 0, 1]],
            [[10, 10, -1], [0, 0, 1], [30, 10, 1], [0, 0, 1], [30, 0, 1]],
            [[10, 20, -1], [30, 10, -1], [0, 0, 1], [0, 10, 1], [0, 20, 1]],
            [[10, 0, -1], [0, 0, 1], [0, 10, -1], [0, 0, 1], [10, 10, 1]],
            [[0, 0, 1], [30, 0, -1], [0, 20, -1], [10, 10, -1], [0, 0, 1]]], {0, 1, 2}), -1)


if __name__ == "__main__":
    unittest.main()
