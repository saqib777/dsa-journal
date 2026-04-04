
import pytest
from maximum_subarray import max_subarray


def test_mixed_positive_negative():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_single_element():
    assert max_subarray([1]) == 1

def test_all_positive():
    assert max_subarray([5, 4, -1, 7, 8]) == 23

def test_all_negative():
    assert max_subarray([-3, -2, -1, -4]) == -1

def test_single_negative():
    assert max_subarray([-1]) == -1

def test_zeros_and_positives():
    assert max_subarray([0, 0, 3, 0]) == 3

def test_large_values():
    assert max_subarray([100, -1, 100]) == 199
