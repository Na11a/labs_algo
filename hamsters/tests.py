from model import Hamster
import unittest

class TestHamster(unittest.TestCase):
    def test_need_food_for_hamster(self):
        self.assertEqual(Hamster(5,10).need_food_for_hamster(2),25)

    def test_get_hamster(self):
        self.assertEqual(Hamster.can_buy('hamsters_in_test1.txt'),2)

if __name__=="__main__":
    unittest.main()
