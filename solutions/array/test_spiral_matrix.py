import pytest
from spiral_matrix import spiral_order, generate_spiral


def test_3x3():
    assert spiral_order([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]

def test_3x4():
    assert spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]

def test_single_element():
    assert spiral_order([[1]]) == [1]

def test_single_row():
    assert spiral_order([[1,2,3,4]]) == [1,2,3,4]

def test_single_column():
    assert spiral_order([[1],[2],[3]]) == [1,2,3]

def test_empty():
    assert spiral_order([]) == []

def test_2x2():
    assert spiral_order([[1,2],[3,4]]) == [1,2,4,3]

def test_generate_1x1():
    assert generate_spiral(1) == [[1]]

def test_generate_3x3():
    expected = [[1,2,3],[8,9,4],[7,6,5]]
    assert generate_spiral(3) == expected

def test_generate_4x4():
    result = generate_spiral(4)
    # Verify all values 1-16 present and first row correct
    assert result[0] == [1, 2, 3, 4]
    flat = [n for row in result for n in row]
    assert sorted(flat) == list(range(1, 17))
