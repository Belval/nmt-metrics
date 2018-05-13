import unittest

from nmt_metrics import (
    Bleu,
    RougeN,
    Meteor,
)

class TestNMTMetrics(unittest.TestCase):
    def test_bleu_1(self):
        c = "the cat sat on the mat".split(' ')
        r = "on the mat sat the cat".split(' ')
        self.assertEqual(round(Bleu.evaluate(c, r), 4), 1.0)

    def test_bleu_2(self):
        c = "the cat sat on the mat".split(' ')
        r = "the cat sat on the mat".split(' ')
        self.assertEqual(round(Bleu.evaluate(c, r), 4), 1.0)
    
    def test_bleu_3(self):
        c = "the cat sat on the mat".split(' ')
        r = "the cat was sat on the mat".split(' ')
        self.assertEqual(round(Bleu.evaluate(c, r), 4), 1.0)

    def test_bleu_4(self):
        c = "the the the the".split(' ')
        r = "the cat was sat on the mat".split(' ')
        self.assertEqual(round(Bleu.evaluate(c, r), 4), 0.5)

    def test_rougen_1(self):
        c = "the cat sat on the mat".split(' ')
        r = "on the mat sat the cat".split(' ')
        self.assertEqual(round(RougeN.evaluate(c, r), 4), 1.0)

    def test_rougen_2(self):
        c = "the cat sat on the mat".split(' ')
        r = "the cat sat on the mat".split(' ')
        self.assertEqual(round(RougeN.evaluate(c, r), 4), 1.0)
    
    def test_rougen_3(self):
        c = "the cat sat on the mat".split(' ')
        r = "the cat was sat on the mat".split(' ')
        self.assertEqual(round(RougeN.evaluate(c, r), 4), 0.8571)

    def test_meteor_1(self):
        c = "the cat sat on the mat".split(' ')
        r = "on the mat sat the cat".split(' ')
        self.assertEqual(round(Meteor.evaluate(c, r), 4), 0.5)

    def test_meteor_2(self):
        c = "the cat sat on the mat".split(' ')
        r = "the cat sat on the mat".split(' ')
        self.assertEqual(round(Meteor.evaluate(c, r), 4), 0.9977)
    
    def test_meteor_3(self):
        c = "the cat sat on the mat".split(' ')
        r = "the cat was sat on the mat".split(' ')
        self.assertEqual(round(Meteor.evaluate(c, r), 4), 0.9654)
    
if __name__ == '__main__':
    unittest.main()
