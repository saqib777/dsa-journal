import pytest
from build_tree_from_traversals import (
    build_from_preorder_inorder,
    build_from_postorder_inorder,
    tree_to_inorder,
    tree_to_preorder,
)


def test_preorder_inorder_basic():
    root = build_from_preorder_inorder([3,9,20,15,7], [9,3,15,20,7])
    assert tree_to_inorder(root)  == [9,3,15,20,7]
    assert tree_to_preorder(root) == [3,9,20,15,7]

def test_preorder_inorder_single():
    root = build_from_preorder_inorder([1], [1])
    assert tree_to_inorder(root) == [1]

def test_preorder_inorder_left_skewed():
    root = build_from_preorder_inorder([3,2,1], [1,2,3])
    assert tree_to_inorder(root)  == [1,2,3]
    assert tree_to_preorder(root) == [3,2,1]

def test_preorder_inorder_right_skewed():
    root = build_from_preorder_inorder([1,2,3], [1,2,3])
    assert tree_to_inorder(root) == [1,2,3]

def test_postorder_inorder_basic():
    root = build_from_postorder_inorder([9,3,15,20,7], [9,15,7,20,3])
    assert tree_to_inorder(root) == [9,3,15,20,7]

def test_postorder_inorder_single():
    root = build_from_postorder_inorder([1], [1])
    assert tree_to_inorder(root) == [1]

def test_both_produce_same_tree():
    pre  = [1,2,4,5,3,6,7]
    ino  = [4,2,5,1,6,3,7]
    post = [4,5,2,6,7,3,1]
    r1 = build_from_preorder_inorder(pre, ino)
    r2 = build_from_postorder_inorder(ino, post)
    assert tree_to_inorder(r1) == tree_to_inorder(r2)
    assert tree_to_preorder(r1) == tree_to_preorder(r2)

@pytest.mark.parametrize("pre, ino", [
    ([1,2,3], [2,1,3]),
    ([4,2,1,3,6,5,7], [1,2,3,4,5,6,7]),
])
def test_parametrized(pre, ino):
    root = build_from_preorder_inorder(pre, ino)
    assert tree_to_inorder(root) == sorted(ino)
