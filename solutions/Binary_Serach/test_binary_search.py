import pytest
from binary_search import binary_search


def test_target_found_middle():
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4

def test_target_not_found():
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1

def test_single_element_found():
    assert binary_search([5], 5) == 0

def test_single_element_not_found():
    assert binary_search([5], 3) == -1

def test_empty_array():
    assert binary_search([], 5) == -1

def test_first_element():
    assert binary_search([1, 3, 5, 7, 9], 1) == 0

def test_last_element():
    assert binary_search([1, 3, 5, 7, 9], 9) == 4

def test_negative_numbers():
    assert binary_search([-10, -5, -3, -1], -3) == 2

def test_large_array():
    arr = list(range(0, 1000, 2))
    assert binary_search(arr, 998) == 499
