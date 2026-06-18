
import pytest
from pascals_triangle import generate, get_row, get_element


def test_generate_basic():
    assert generate(5) == [
        [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]
    ]

def test_generate_single_row():
    assert generate(1) == [[1]]

def test_generate_two_rows():
    assert generate(2) == [[1], [1,1]]

def test_generate_zero_rows():
    assert generate(0) == []

def test_get_row_basic():
    assert get_row(4) == [1,4,6,4,1]

def test_get_row_zero():
    assert get_row(0) == [1]

def test_get_row_one():
    assert get_row(1) == [1,1]

def test_get_row_matches_generate():
    full = generate(8)
    for i in range(8):
        assert get_row(i) == full[i]

def test_get_element_basic():
    assert get_element(4, 2) == 6

def test_get_element_edge():
    assert get_element(5, 0) == 1
    assert get_element(5, 5) == 1

def test_get_element_invalid():
    assert get_element(3, 5) == 0

def test_get_element_matches_row():
    row = get_row(6)
    for col in range(7):
        assert get_element(6, col) == row[col]

@pytest.mark.parametrize("n, expected_last_row", [
    (1, [1]),
    (3, [1,2,1]),
    (6, [1,5,10,10,5,1]),
])
def test_parametrized(n, expected_last_row):
    assert generate(n)[-1] == expected_last_row
