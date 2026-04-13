import pytest
from group_anagrams import group_anagrams


def sorted_groups(result):
    """Sort each group and sort groups for deterministic comparison."""
    return sorted([sorted(group) for group in result])


def test_basic():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted_groups(result) == [
        ["ate", "eat", "tea"],
        ["bat"],
        ["nat", "tan"],
    ]

def test_single_word():
    assert sorted_groups(group_anagrams(["hello"])) == [["hello"]]

def test_empty_strings():
    result = group_anagrams(["", ""])
    assert sorted_groups(result) == [["", ""]]

def test_all_unique():
    result = group_anagrams(["abc", "def", "ghi"])
    assert sorted_groups(result) == [["abc"], ["def"], ["ghi"]]

def test_all_anagrams():
    result = group_anagrams(["abc", "bca", "cab"])
    assert sorted_groups(result) == [["abc", "bca", "cab"]]

def test_empty_input():
    assert group_anagrams([]) == []

def test_mixed_lengths():
    result = group_anagrams(["a", "b", "ab", "ba"])
    assert sorted_groups(result) == [["a"], ["ab", "ba"], ["b"]]
