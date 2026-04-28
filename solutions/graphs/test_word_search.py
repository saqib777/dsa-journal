import pytest
from word_search import exist, find_all_word_positions


def board():
    return [['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']]


def test_word_exists_diagonal_path():
    assert exist(board(), "ABCCED") == True

def test_word_exists_short():
    assert exist(board(), "SEE") == True

def test_word_not_exists_revisit():
    assert exist(board(), "ABCB") == False

def test_single_character_exists():
    assert exist([['A']], "A") == True

def test_single_character_not_exists():
    assert exist([['A']], "B") == False

def test_word_longer_than_board():
    assert exist([['a','b'],['c','d']], "abcde") == False

def test_entire_board_word():
    assert exist([['a','b'],['d','c']], "abcd") == True

def test_cannot_reuse_cell():
    assert exist([['a','a']], "aaa") == False

def test_empty_word():
    assert exist(board(), "") == True

def test_single_row():
    assert exist([['a','b','c','d']], "abcd") == True

def test_single_column():
    assert exist([['a'],['b'],['c']], "abc") == True

def test_find_positions_basic():
    positions = find_all_word_positions(board(), "SEE")
    assert (1, 3) in positions

@pytest.mark.parametrize("word, expected", [
    ("ABCCED", True),
    ("SEE",    True),
    ("ABCB",   False),
    ("A",      True),
    ("Z",      False),
])
def test_parametrized(word, expected):
    assert exist(board(), word) == expected
