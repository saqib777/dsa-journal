import pytest
from validate_bst import is_valid_bst, TreeNode


def test_valid_bst():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert is_valid_bst(root) == True

def test_invalid_bst():
    root = TreeNode(5,
             TreeNode(1),
             TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid_bst(root) == False

def test_single_node():
    assert is_valid_bst(TreeNode(1)) == True

def test_empty_tree():
    assert is_valid_bst(None) == True

def test_left_subtree_violation():
    # right child of left subtree is greater than root — invalid
    root = TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(15)), TreeNode(20))
    assert is_valid_bst(root) == False

def test_valid_three_levels():
    root = TreeNode(8,
             TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
             TreeNode(10, None, TreeNode(14, TreeNode(13), None)))
    assert is_valid_bst(root) == True

def test_duplicate_values():
    # duplicates are not allowed in a BST
    root = TreeNode(2, TreeNode(2), TreeNode(3))
    assert is_valid_bst(root) == False
