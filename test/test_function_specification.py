import unittest
import NegaPosiAnalyzer


class Test(unittest.TestCase):

    def test_accessible(self):
        NegaPosiAnalyzer.evaluate_sentence

    def test_evaluate_sentence_specification(self):
        with self.assertRaises(TypeError):
            NegaPosiAnalyzer.evaluate_sentence()
