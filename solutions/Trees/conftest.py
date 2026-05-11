# Shared fixtures for tree test files

import pytest
from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right


def build_tree(values: list) -> TreeNode:
    """Build tree from level-order list. None = missing node."""
    if not values or values[0] is None:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    for i in range(len(nodes)):
        if nodes[i]:
            li = 2 * i + 1
            ri = 2 * i + 2
            if li < len(nodes): nodes[i].left  = nodes[li]
            if ri < len(nodes): nodes[i].right = nodes[ri]
    return nodes[0]


def tree_to_list(root: TreeNode) -> list:
    """Level-order traversal to list."""
    if not root:
        return []
    result = []
    queue  = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


@pytest.fixture
def balanced_tree():
    return build_tree([1, 2, 3, 4, 5, 6, 7])


@pytest.fixture
def single_node():
    return TreeNode(42)


@pytest.fixture
def left_skewed():
    return build_tree([1, 2, None, 3, None, None, None])


@pytest.fixture
def right_skewed():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    return root


@pytest.fixture
def bst_tree():
    return build_tree([4, 2, 6, 1, 3, 5, 7])
