import pytest
from word_break import word_break, word_break_paths


def test_basic_true():
    assert word_break("leetcode", ["leet","code"]) == True

def test_basic_false():
    assert word_break("catsandog", ["cats","dog","sand","an","cat"]) == False

def test_apple_pen():
    assert word_break("applepenapple", ["apple","pen"]) == True

def test_single_word_match():
    assert word_break("dog", ["dog"]) == True

def test_single_word_no_match():
    assert word_break("dog", ["cat"]) == False

def test_empty_string():
    assert word_break("", ["cat","dog"]) == True

def test_empty_dict():
    assert word_break("cat", []) == False

def test_repeated_words():
    assert word_break("aaaaaaa", ["aaaa","aaa"]) == True

def test_paths_basic():
    paths = word_break_paths("catsanddog", ["cat","cats","and","sand","dog"])
    assert "cats and dog" in paths
    assert "cat sand dog" in paths

def test_paths_no_solution():
    assert word_break_paths("abc", ["def"]) == []

def test_paths_single():
    paths = word_break_paths("leetcode", ["leet","code"])
    assert paths == ["leet code"]

@pytest.mark.parametrize("s, words, expected", [
    ("cars",       ["car","ca","rs"],      True),
    ("goalspecial",["go","goal","goals","special"], True),
    ("abcd",       ["a","abc","b","cd"],   True),
    ("aaab",       ["a","b"],              True),
])
def test_parametrized(s, words, expected):
    assert word_break(s, words) == expected
