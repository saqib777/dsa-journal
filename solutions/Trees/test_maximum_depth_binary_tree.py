import pytest
from maximum_depth_binary_tree import max_depth, TreeNode


def test_basic():
    root = TreeNode(3,
             TreeNode(9),
             TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3

def test_empty():
    assert max_depth(None) == 0

def test_single_node():
    assert max_depth(TreeNode(1)) == 1

def test_only_left():
    root = TreeNode(1, TreeNode(2, TreeNode(3), None), None)
    assert max_depth(root) == 3

def test_balanced():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert max_depth(root) == 2

def test_skewed_right():
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    assert max_depth(root) == 4
