import pytest
from longest_repeating_character_replacement import (
    character_replacement,
    character_replacement_all_windows,
)


def test_basic_aababba():
    assert character_replacement("AABABBA", 1) == 4

def test_basic_abab():
    assert character_replacement("ABAB", 2) == 4

def test_all_same_chars():
    assert character_replacement("AAAA", 2) == 4

def test_aabccbb():
    assert character_replacement("AABCCBB", 2) == 5

def test_k_zero():
    assert character_replacement("AABABBA", 0) == 2

def test_k_larger_than_string():
    assert character_replacement("ABCD", 10) == 4

def test_single_char():
    assert character_replacement("A", 0) == 1

def test_empty():
    assert character_replacement("", 0) == 0

def test_two_chars_k1():
    assert character_replacement("AB", 1) == 2

def test_all_replaceable():
    assert character_replacement("BAAAC", 2) == 5

def test_windows_variant_returns_correct_length():
    windows = character_replacement_all_windows("AABABBA", 1)
    assert all(len(w) == 4 for w in windows)

def test_windows_not_empty():
    windows = character_replacement_all_windows("ABAB", 2)
    assert len(windows) > 0

@pytest.mark.parametrize("s, k, expected", [
    ("AABABBA", 1, 4),
    ("ABAB",    2, 4),
    ("AAAA",    2, 4),
    ("A",       0, 1),
    ("AB",      1, 2),
])
def test_parametrized(s, k, expected):
    assert character_replacement(s, k) == expected
