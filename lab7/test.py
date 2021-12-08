from knut_morris import kmp,prefix
import unittest

class TestKnutMorris(unittest.TestCase):
    def testPrefixWithOut(self):
        self.assertEqual(prefix('abcbc'),[0,0,0,0,0])
    def testPrefix(self):
        self.assertEqual(prefix('abcafab'),[0,0,0,1,0,1,2])
    def testKnuMoris(self):
        self.assertEqual(kmp('mamas','sadfmamaadfmamas'),11)
unittest.main()