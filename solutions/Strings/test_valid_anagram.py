
import pytest
from valid_anagram import valid_anagram


def test_basic_anagram():
    assert valid_anagram("anagram", "nagaram") == True

def test_not_anagram():
    assert valid_anagram("rat", "car") == False

def test_different_lengths():
    assert valid_anagram("hello", "hell") == False

def test_same_string():
    assert valid_anagram("python", "python") == True

def test_mixed_case():
    assert valid_anagram("Listen", "Silent") == False

def test_empty_strings():
    assert valid_anagram("", "") == True

def test_single_char_match():
    assert valid_anagram("a", "a") == True

def test_single_char_no_match():
    assert valid_anagram("a", "b") == False
