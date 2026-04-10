# Algorithm: DFS Recursive Post-order
# Time Complexity:  O(n) — every node visited once
# Space Complexity: O(h) — h = height of tree (recursion stack)

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right


def invert_tree(root: TreeNode) -> TreeNode:
    """
    Invert a binary tree (mirror it) and return the root.
    """
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def tree_to_list(root: TreeNode) -> list:
    """Level-order traversal — useful for test assertions."""
    if not root:
        return []
    from collections import deque
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    #       4
    #      / \
    #     2   7
    #    /\   /\
    #   1  3 6  9
    root = TreeNode(4,
             TreeNode(2, TreeNode(1), TreeNode(3)),
             TreeNode(7, TreeNode(6), TreeNode(9)))
    inverted = invert_tree(root)
    print(tree_to_list(inverted))  # [4, 7, 2, 9, 6, 3, 1]
