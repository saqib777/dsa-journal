import pytest
from level_order_traversal import level_order, level_order_flat, TreeNode


def test_basic():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(root) == [[3],[9,20],[15,7]]

def test_single_node():
    assert level_order(TreeNode(1)) == [[1]]

def test_empty():
    assert level_order(None) == []

def test_left_skewed():
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert level_order(root) == [[1],[2],[3]]

def test_right_skewed():
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert level_order(root) == [[1],[2],[3]]

def test_complete_tree():
    root = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7)))
    assert level_order(root) == [[1],[2,3],[4,5,6,7]]

def test_flat_basic():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order_flat(root) == [3,9,20,15,7]

def test_flat_empty():
    assert level_order_flat(None) == []

def test_level_count():
    root = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7)))
    levels = level_order(root)
    assert len(levels) == 3
    assert len(levels[2]) == 4

@pytest.mark.parametrize("vals, expected_levels", [
    ([1], 1),
    ([1,2,3], 2),
    ([1,2,3,4,5,6,7], 3),
])
def test_depth_parametrized(vals, expected_levels):
    nodes = [TreeNode(v) for v in vals]
    for i in range(len(nodes)):
        li = 2*i+1; ri = 2*i+2
        if li < len(nodes): nodes[i].left  = nodes[li]
        if ri < len(nodes): nodes[i].right = nodes[ri]
    assert len(level_order(nodes[0])) == expected_levels
