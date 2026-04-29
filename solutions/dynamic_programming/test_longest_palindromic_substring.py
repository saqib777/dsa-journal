import pytest
from longest_palindromic_substring import (
    longest_palindrome_expand,
    longest_palindrome_dp,
    count_palindromic_substrings,
)


def is_palindrome(s):
    return s == s[::-1]


def test_expand_basic():
    result = longest_palindrome_expand("babad")
    assert result in ("bab", "aba")
    assert is_palindrome(result)

def test_expand_even():
    assert longest_palindrome_expand("cbbd") == "bb"

def test_expand_single():
    assert longest_palindrome_expand("a") == "a"

def test_expand_full():
    assert longest_palindrome_expand("racecar") == "racecar"

def test_expand_all_same():
    result = longest_palindrome_expand("aaaa")
    assert result == "aaaa"

def test_dp_basic():
    result = longest_palindrome_dp("babad")
    assert result in ("bab", "aba")

def test_dp_even():
    assert longest_palindrome_dp("cbbd") == "bb"

def test_dp_single():
    assert longest_palindrome_dp("a") == "a"

def test_dp_full():
    assert longest_palindrome_dp("racecar") == "racecar"

def test_both_agree():
    cases = ["babad","cbbd","a","racecar","abcba","noon","xyz"]
    for s in cases:
        r1 = longest_palindrome_expand(s)
        r2 = longest_palindrome_dp(s)
        assert len(r1) == len(r2)
        assert is_palindrome(r1)
        assert is_palindrome(r2)

def test_count_abc():
    assert count_palindromic_substrings("abc") == 3

def test_count_aaa():
    assert count_palindromic_substrings("aaa") == 6

def test_count_racecar():
    assert count_palindromic_substrings("racecar") == 10

@pytest.mark.parametrize("s, min_len", [
    ("bananas", 5),
    ("abcba",   5),
    ("noon",    4),
])
def test_parametrized_length(s, min_len):
    assert len(longest_palindrome_expand(s)) >= min_len
