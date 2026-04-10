import pytest
from invert_binary_tree import invert_tree, TreeNode, tree_to_list


def test_basic():
    root = TreeNode(4,
             TreeNode(2, TreeNode(1), TreeNode(3)),
             TreeNode(7, TreeNode(6), TreeNode(9)))
    assert tree_to_list(invert_tree(root)) == [4, 7, 2, 9, 6, 3, 1]

def test_single_node():
    root = TreeNode(1)
    assert tree_to_list(invert_tree(root)) == [1]

def test_empty_tree():
    assert invert_tree(None) is None

def test_only_left_child():
    root = TreeNode(1, TreeNode(2), None)
    assert tree_to_list(invert_tree(root)) == [1, None, 2]

def test_only_right_child():
    root = TreeNode(1, None, TreeNode(2))
    assert tree_to_list(invert_tree(root)) == [1, 2]

def test_two_levels():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert tree_to_list(invert_tree(root)) == [1, 3, 2]
