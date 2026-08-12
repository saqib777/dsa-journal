# Algorithm: Dynamic Programming (Bottom-Up, Space-Optimised)
# Time Complexity:  O(n) — single pass
# Space Complexity: O(1) — two variables only

def min_cost_climbing_stairs(cost: list[int]) -> int:
    """
    Each index of cost[] is a stair step. cost[i] is the cost
    to step on that stair. You can start from step 0 or step 1.
    After stepping on a stair you can climb 1 or 2 steps.
    Return the minimum cost to reach the top (past the last step).

    Recurrence:
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    Answer: min(dp[n-1], dp[n-2])

    Optimised: only track previous two dp values.

    Example:
        cost = [10,15,20] → 15  (start at step 1, cost 15, jump 2 to top)
        cost = [1,100,1,1,1,100,1,1,100,1] → 6
    """
    n = len(cost)
    if n == 0: return 0
    if n == 1: return cost[0]

    prev2 = cost[0]
    prev1 = cost[1]

    for i in range(2, n):
        curr  = cost[i] + min(prev1, prev2)
        prev2 = prev1
        prev1 = curr

    return min(prev1, prev2)


def min_cost_climbing_stairs_dp(cost: list[int]) -> int:
    """
    Full DP array version — easier to understand for learning.
    Space: O(n)
    """
    n  = len(cost)
    if n == 0: return 0
    if n == 1: return cost[0]

    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    return min(dp[n-1], dp[n-2])


def min_cost_with_path(cost: list[int]) -> tuple[int, list[int]]:
    """
    Variant: return (min_cost, path_of_steps_taken).
    Backtracks through dp to reconstruct the optimal path.
    """
    n  = len(cost)
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    # Backtrack from the cheaper of the last two steps
    path = []
    i    = n-1 if dp[n-1] < dp[n-2] else n-2

    while i >= 0:
        path.append(i)
        if i < 2:
            break
        i = i-1 if dp[i-1] < dp[i-2] else i-2

    return min(dp[n-1], dp[n-2]), path[::-1]


if __name__ == "__main__":
    print(min_cost_climbing_stairs([10, 15, 20]))                    # 15
    print(min_cost_climbing_stairs([1,100,1,1,1,100,1,1,100,1]))     # 6
    print(min_cost_climbing_stairs_dp([10, 15, 20]))                 # 15

    cost, path = min_cost_with_path([10, 15, 20])
    print(cost, path)   # 15  [1]
