# Algorithm: Dynamic Programming (2D Grid Tabulation)
# Time Complexity:  O(m * n)
# Space Complexity: O(m * n) full | O(n) space-optimised

def unique_paths(m: int, n: int) -> int:
    """
    Count distinct paths from top-left to bottom-right of an m x n grid.
    Can only move RIGHT or DOWN at each step.

    Recurrence:
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        (paths from above + paths from left)

    Base case: first row and first column are all 1
    (only one way to reach any cell in the first row/column).

    Example:
        m=3, n=7 → 28 unique paths
    """
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]


def unique_paths_optimised(m: int, n: int) -> int:
    """
    Space-optimised: only one row needed at a time.
    Space: O(n)
    """
    dp = [1] * n

    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]

    return dp[n-1]


def unique_paths_with_obstacles(grid: list[list[int]]) -> int:
    """
    Variant: grid has obstacles (1 = blocked, 0 = open).
    Count paths avoiding blocked cells.

    If start or end is blocked, return 0.
    """
    m, n = len(grid), len(grid[0])

    if grid[0][0] == 1 or grid[m-1][n-1] == 1:
        return 0

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    for j in range(1, n):
        dp[0][j] = 0 if grid[0][j] == 1 else dp[0][j-1]

    for i in range(1, m):
        dp[i][0] = 0 if grid[i][0] == 1 else dp[i-1][0]

    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]


def unique_paths_math(m: int, n: int) -> int:
    """
    Mathematical approach using combinations.
    Total moves = (m-1) down + (n-1) right = m+n-2 moves.
    Choose which (m-1) moves are downward.
    Answer = C(m+n-2, m-1)
    Time: O(min(m,n)), Space: O(1)
    """
    from math import comb
    return comb(m + n - 2, m - 1)


if __name__ == "__main__":
    print(unique_paths(3, 7))            # 28
    print(unique_paths(3, 2))            # 3
    print(unique_paths_optimised(3, 7))  # 28
    print(unique_paths_math(3, 7))       # 28

    grid = [[0,0,0],[0,1,0],[0,0,0]]
    print(unique_paths_with_obstacles(grid))   # 2
