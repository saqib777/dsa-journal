# Algorithm: DFS Recursive
# Time Complexity:  O(n) — every node visited once
# Space Complexity: O(h) — h = height of tree (recursion stack)

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    """
    Return the maximum depth (number of nodes along the longest
    path from root down to the farthest leaf node).
    """
    if root is None:
        return 0
    left_depth  = max_depth(root.left)
    right_depth = max_depth(root.right)
    return 1 + max(left_depth, right_depth)


if __name__ == "__main__":
    #       3
    #      / \
    #     9  20
    #        / \
    #       15   7
    root = TreeNode(3,
             TreeNode(9),
             TreeNode(20, TreeNode(15), TreeNode(7)))
    print(max_depth(root))   # 3
    print(max_depth(None))   # 0
