import pytest
from longest_common_subsequence import lcs_length, lcs_reconstruct, lcs_space_optimised


def test_basic():
    assert lcs_length("abcde", "ace") == 3

def test_identical_strings():
    assert lcs_length("abc", "abc") == 3

def test_no_common():
    assert lcs_length("abc", "def") == 0

def test_empty_first():
    assert lcs_length("", "abc") == 0

def test_empty_second():
    assert lcs_length("abc", "") == 0

def test_both_empty():
    assert lcs_length("", "") == 0

def test_single_char_match():
    assert lcs_length("a", "a") == 1

def test_single_char_no_match():
    assert lcs_length("a", "b") == 0

def test_reconstruct_basic():
    assert lcs_reconstruct("abcde", "ace") == "ace"

def test_reconstruct_identical():
    assert lcs_reconstruct("abc", "abc") == "abc"

def test_reconstruct_no_common():
    assert lcs_reconstruct("abc", "def") == ""

def test_space_optimised_matches():
    cases = [("abcde","ace"),("abc","abc"),("abc","def"),("","abc")]
    for t1, t2 in cases:
        assert lcs_space_optimised(t1, t2) == lcs_length(t1, t2)

@pytest.mark.parametrize("t1, t2, expected", [
    ("oxcpqrsvwf", "shmtulqrypy", 2),
    ("bsbininm",   "jmjkbkjkv",  2),
    ("abcba",      "abcbcba",    5),
])
def test_parametrized(t1, t2, expected):
    assert lcs_length(t1, t2) == expected
