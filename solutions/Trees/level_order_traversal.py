# Algorithm: Breadth-First Search (Queue-based Level Order)
# Time Complexity:  O(n) — every node visited exactly once
# Space Complexity: O(w) — w = maximum width of the tree (queue size)

from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right


def level_order(root: TreeNode) -> list[list[int]]:
    """
    Return all node values level by level as a list of lists.
    Each inner list is one level of the tree.

    Example:
            3
           / \\
          9  20
             / \\
            15   7

    Output: [[3], [9, 20], [15, 7]]
    """
    if not root:
        return []

    result = []
    queue  = deque([root])

    while queue:
        level_size = len(queue)
        level      = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)

        result.append(level)

    return result


def level_order_flat(root: TreeNode) -> list[int]:
    """Variant: returns flat list — all values in level order."""
    return [val for level in level_order(root) for val in level]


if __name__ == "__main__":
    root = TreeNode(3,
             TreeNode(9),
             TreeNode(20, TreeNode(15), TreeNode(7)))
    print(level_order(root))       # [[3], [9, 20], [15, 7]]
    print(level_order_flat(root))  # [3, 9, 20, 15, 7]
    print(level_order(None))       # []
