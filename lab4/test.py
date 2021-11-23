import unittest
from bellman_ford import Graph


class BellmanFordTest(unittest.TestCase):
    def setUp(self):
        self.g = Graph(4)
        self.g.add_edge(0, 1, 2)
        self.g.add_edge(1, 2, -3)
        self.g.add_edge(1, 3, -2)
        self.g.add_edge(2, 3, -3)

    def test_bellman_ford_(self):
        self.assertEqual(self.g.bellman_ford(0), [0, 2, -1, -4])

    def test_bellman_ford_with_ing(self):
        self.assertEqual(self.g.bellman_ford(1),[float("Inf"), 0, -3, -6])

unittest.main()