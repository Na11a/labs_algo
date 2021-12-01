import unittest

from words import Words
from io_data import input_data


class Tests(unittest.TestCase):

    def test(self):

        data = input_data("./IO/wchain1.in")
        words = Words(data['words'],data['count'])
        words.counter()
        self.assertEqual(words.get_max_chain(), 2)

        data = input_data("./IO/wchain2.in")
        words = Words(data['words'], data['count'])
        words.counter()
        self.assertEqual(words.get_max_chain(), 4)

        data = input_data("./IO/wchain3.in")
        words = Words(data['words'], data['count'])
        words.counter()
        self.assertEqual(words.get_max_chain(), 7)

        data = input_data("./IO/wchain4.in")
        words = Words(data['words'], data['count'])
        words.counter()
        self.assertEqual(words.get_max_chain(), 7)



if __name__ == '__main__':
    unittest.main()
