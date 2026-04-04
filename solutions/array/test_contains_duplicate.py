
import pytest
from contains_duplicate import contains_duplicate


def test_has_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) == True

def test_no_duplicate():
    assert contains_duplicate([1, 2, 3, 4]) == False

def test_multiple_duplicates():
    assert contains_duplicate([1, 1, 1, 3, 3, 4]) == True

def test_single_element():
    assert contains_duplicate([1]) == False

def test_empty_array():
    assert contains_duplicate([]) == False

def test_negative_numbers():
    assert contains_duplicate([-1, -2, -3, -1]) == True

def test_large_unique():
    assert contains_duplicate(list(range(1000))) == False

def test_large_with_duplicate():
    arr = list(range(999)) + [0]
    assert contains_duplicate(arr) == True
