import unittest
import NegaPosiAnalyzer


class Test(unittest.TestCase):

    def setUp(self):
        self.text = """
        醜いより美しいほうがいい。
        暗示するより明示するほうがいい。
        複雑であるよりは平易であるほうがいい。
        それでも、込み入っているよりは複雑であるほうがまし。
        ネストは浅いほうがいい。
        密集しているよりは隙間があるほうがいい。
        読みやすいことは善である。
        特殊であることはルールを破る理由にならない。
        しかし、実用性を求めると自然さが失われることがある。
        エラーは隠すな、無視するな。
        ただし、わざと隠されているのなら見逃せ。
        曖昧なものに出逢ったら、その意味を適当に推測してはいけない。
        たったひとつの冴えたやりかたがあるはずだ。
        そのやり方は一目見ただけではわかりにくいかもしれない。オランダ人にだけわかりやすいなんてこともあるかもしれない。
        ずっとやらないでいるよりは、今やれ。
        でも、今"すぐ"にやるよりはやらないほうがマシなことが多い。
        コードの内容を説明するのが難しいのなら、それは悪い実装である。
        コードの内容を容易に説明できるのなら、おそらくそれはよい実装である。
        名前空間は優れたアイデアであるため、積極的に利用すべきである
        """

    def test_accessible(self):
        NegaPosiAnalyzer.evaluate_sentence

    def test_evaluate_sentence_specification(self):
        evaluate_sentence = NegaPosiAnalyzer.evaluate_sentence

        with self.assertRaises(TypeError):
            evaluate_sentence()

        with self.assertRaises(TypeError):
            evaluate_sentence([])

        self.assertIsInstance(evaluate_sentence(self.text), int)

        self.assertIsInstance(evaluate_sentence(self.text, True), int)

        self.assertIsInstance(evaluate_sentence(self.text, False), int)

        self.assertIsInstance(evaluate_sentence(self.text, True, True), int)

        self.assertIsInstance(evaluate_sentence(self.text, True, False), int)

        self.assertIsInstance(evaluate_sentence(self.text, False, True), int)

        self.assertIsInstance(evaluate_sentence(self.text, False, False), int)

        self.assertTrue(evaluate_sentence(self.text, negative=False) >= 0)

        self.assertTrue(evaluate_sentence(self.text, positive=False) <= 0)
