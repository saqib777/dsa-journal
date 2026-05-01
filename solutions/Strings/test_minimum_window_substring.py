import pytest
from minimum_window_substring import min_window, min_window_all
from collections import Counter


def contains_all(window: str, t: str) -> bool:
    wc = Counter(window)
    tc = Counter(t)
    return all(wc[ch] >= tc[ch] for ch in tc)


def test_basic():
    result = min_window("ADOBECODEBANC", "ABC")
    assert result == "BANC"

def test_single_char():
    assert min_window("a", "a") == "a"

def test_not_possible():
    assert min_window("a", "aa") == ""

def test_both_same():
    assert min_window("aa", "aa") == "aa"

def test_empty_s():
    assert min_window("", "abc") == ""

def test_empty_t():
    assert min_window("abc", "") == ""

def test_t_longer_than_s():
    assert min_window("ab", "abc") == ""

def test_result_valid():
    s = "cabwefgewcwaefgcf"
    t = "cae"
    result = min_window(s, t)
    assert contains_all(result, t)
    assert len(result) <= 4

def test_t_is_s():
    assert min_window("abc", "abc") == "abc"

def test_duplicates_in_t():
    result = min_window("aaabbbccc", "abc")
    assert contains_all(result, "abc")
    assert len(result) == 3

def test_window_at_start():
    assert min_window("abcdef", "abc") == "abc"

def test_window_at_end():
    assert min_window("defabc", "abc") == "abc"

@pytest.mark.parametrize("s, t", [
    ("ADOBECODEBANC", "ABC"),
    ("a",             "a"),
    ("aa",            "aa"),
    ("bba",           "ab"),
])
def test_parametrized_valid(s, t):
    result = min_window(s, t)
    if result:
        assert contains_all(result, t)
