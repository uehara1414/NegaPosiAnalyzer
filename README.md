# NegaPosiAnalyzer
[![Build Status](https://travis-ci.org/uehara1414/NegaPosiAnalyzer.svg?branch=master)](https://travis-ci.org/uehara1414/NegaPosiAnalyzer)

日本語文章の感情分析ライブラリになる予定

## インストール
### インストール準備
- [MeCab](http://taku910.github.io/mecab/)のインストール

### インストール
```shell
pip install NegaPosiAnalyzer
```

## 使い方
現状実装されてるのはevaluate_sentenceのみです。

文章中に出てくるネガティブ・ポジティブワードのポイントをそれぞれ-1, 1として加算した和を返します。

negative, positive オプションでネガティブ・ポジティブのみの加算も可能です。

```python
>>> from NegaPosiAnalyzer import evaluate_sentence
>>> evaluate_sentence("醜いより美しいほうがいい。")
1
>>> evaluate_sentence("醜いより美しいほうがいい。", negative=False)
2
>>> evaluate_sentence("醜いより美しいほうがいい。", positive=False)
-1
```
