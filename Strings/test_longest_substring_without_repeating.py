
import pytest
from longest_substring_without_repeating import length_of_longest_substring


def test_basic_case():
    assert length_of_longest_substring("abcabcbb") == 3

def test_all_same():
    assert length_of_longest_substring("bbbbb") == 1

def test_mixed():
    assert length_of_longest_substring("pwwkew") == 3

def test_empty_string():
    assert length_of_longest_substring("") == 0

def test_single_char():
    assert length_of_longest_substring("a") == 1

def test_all_unique():
    assert length_of_longest_substring("abcdef") == 6

def test_spaces():
    assert length_of_longest_substring("ab c") == 4

def test_numbers_in_string():
    assert length_of_longest_substring("1234512") == 5
