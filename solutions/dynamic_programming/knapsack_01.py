# Algorithm: Dynamic Programming (2D Tabulation + Space Optimised)
# Time Complexity:  O(n * W) — n items, W = capacity
# Space Complexity: O(n * W) full | O(W) optimised

def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    """
    Classic 0/1 Knapsack — each item either taken or not (no fractions).

    dp[i][w] = max value using first i items with capacity w.

    Recurrence:
        If weights[i-1] > w:  dp[i][w] = dp[i-1][w]
        Else: dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])

    Unlike fractional knapsack, greedy does NOT work here.
    DP is required.
    """
    n  = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )

    return dp[n][capacity]


def knapsack_01_optimised(weights: list[int], values: list[int], capacity: int) -> int:
    """
    Space-optimised version using single 1D array.
    Traverse capacity right to left to avoid using same item twice.
    Space: O(W)
    """
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


def knapsack_with_items(weights: list[int], values: list[int], capacity: int) -> tuple:
    """
    Returns (max_value, list_of_selected_item_indices).
    Backtracks through dp table to identify chosen items.
    """
    n  = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )

    # Backtrack
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], selected[::-1]


if __name__ == "__main__":
    weights  = [1, 3, 4, 5]
    values   = [1, 4, 5, 7]
    capacity = 7

    print(knapsack_01(weights, values, capacity))           # 9
    print(knapsack_01_optimised(weights, values, capacity)) # 9

    val, items = knapsack_with_items(weights, values, capacity)
    print(val, items)   # 9  [1, 2]  (items at index 1 and 2)
