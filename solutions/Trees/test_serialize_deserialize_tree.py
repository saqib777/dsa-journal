import pytest
from serialize_deserialize_tree import serialize, deserialize, TreeNode, tree_to_list


def make_tree(values: list) -> TreeNode:
    """Build tree from level-order list with None for missing nodes."""
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    for i in range(len(nodes)):
        if nodes[i]:
            li = 2*i+1; ri = 2*i+2
            if li < len(nodes): nodes[i].left  = nodes[li]
            if ri < len(nodes): nodes[i].right = nodes[ri]
    return nodes[0]


def roundtrip(root):
    return deserialize(serialize(root))


def test_basic_roundtrip():
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    assert tree_to_list(roundtrip(root)) == tree_to_list(root)

def test_none_tree():
    assert serialize(None) == "N"
    assert deserialize("N") is None

def test_single_node():
    root = TreeNode(42)
    rt   = roundtrip(root)
    assert rt.value == 42
    assert rt.left is None
    assert rt.right is None

def test_left_skewed():
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert tree_to_list(roundtrip(root)) == [1, 2, 3]

def test_right_skewed():
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert tree_to_list(roundtrip(root)) == [1, 2, 3]

def test_complete_tree():
    root = make_tree([1,2,3,4,5,6,7])
    assert tree_to_list(roundtrip(root)) == [1,2,3,4,5,6,7]

def test_serialize_deterministic():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert serialize(root) == serialize(root)

def test_negative_values():
    root = TreeNode(-1, TreeNode(-2), TreeNode(-3))
    rt   = roundtrip(root)
    assert rt.value == -1
    assert rt.left.value  == -2
    assert rt.right.value == -3

def test_large_values():
    root = TreeNode(10**6, TreeNode(-(10**6)))
    rt   = roundtrip(root)
    assert rt.value == 10**6
    assert rt.left.value == -(10**6)

@pytest.mark.parametrize("vals", [
    [1],
    [1,2,3],
    [1,None,2,None,3],
    [5,4,6,3,None,None,7],
])
def test_parametrized_roundtrip(vals):
    root = make_tree(vals)
    assert tree_to_list(roundtrip(root)) == tree_to_list(root)
