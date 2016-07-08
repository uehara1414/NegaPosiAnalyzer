import MeCab
import subprocess
import os

__version__ = '0.1.0'


def _get_declinable_word_dict_path() -> str:
    this_dir, this_filename = os.path.split(__file__)
    return os.path.join(this_dir, "dictionary", "wago.121808.pn")


def _get_noun_dict_path() -> str:
    this_dir, this_filename = os.path.split(__file__)
    return os.path.join(this_dir, "dictionary", "pn.csv.m3.120408.trim")


def _get_neolgd_pass() -> str:
    cmd = 'echo `mecab-config --dicdir`"/mecab-ipadic-neologd"'
    dist = subprocess.getoutput(cmd)
    ls_ret = subprocess.getoutput('ls %s' % dist)
    if "No such" in ls_ret:
        raise FileNotFoundError("mecab-ipadic-neologd not found.")
    else:
        return dist


def _load_declinable_word_dict() -> dict:
    dct = {}
    with open(_get_declinable_word_dict_path(), 'r') as f:
        for l in f.readlines():
            l = l.split('\t')
            l[1] = l[1].replace(" ", "").replace('\n', '')
            value = 1 if l[0].split('（')[0] == "ポジ" else -1
            dct[l[1]] = value
    return dct


def _load_noun_dict() -> dict:
    dct = {}
    with open(_get_noun_dict_path(), 'r') as f:
        for l in f.readlines():
            l = l.split('\t')

            if l[1] == "p":
                dct[l[0]] = 1
            elif l[1] == "e":
                dct[l[0]] = 0
            elif l[1] == "n":
                dct[l[0]] = -1

    return dct


def _load_negaposi_data() -> dict:
    negaposi_dict = {}

    declinable_word_dict = _load_declinable_word_dict()
    noun_dict = _load_noun_dict()

    negaposi_dict.update(declinable_word_dict)
    negaposi_dict.update(noun_dict)

    return negaposi_dict


def _count_negaposi_sum(word_list: list, negative: bool=True,
                        positive: bool=True) -> int:
    negaposi_dict = _load_negaposi_data()
    score = 0
    val_list = []
    for word in word_list:
        if not word:
            continue
        val = negaposi_dict.get(word, 0)
        if positive and val > 0:
            score += val
        elif negative and val < 0:
            score += val
    return score


def _get_word_list(sentence: str) -> list:
    m = None
    try:
        neolgd_pass = _get_neolgd_pass()
        m = MeCab.Tagger("-Ochasen -d %s" % neolgd_pass)
    except FileNotFoundError:
        m = MeCab.Tagger("-Ochasen")
    m.parse('')
    node = m.parseToNode(sentence)
    word_list = []
    while node:
        word_list.append(node.surface)
        node = node.next
    return word_list


def evaluate_sentence(sentence: str, negative: bool=True,
                      positive: bool=True) -> int:
    word_list = _get_word_list(sentence)
    return _count_negaposi_sum(word_list, negative=negative, positive=positive)
