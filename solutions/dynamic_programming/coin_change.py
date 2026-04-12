# Algorithm: Dynamic Programming (Bottom-Up Tabulation)
# Time Complexity:  O(n * m) — n = amount, m = number of coin denominations
# Space Complexity: O(n)     — dp array of size amount + 1

def coin_change(coins: list[int], amount: int) -> int:
    """
    Return the minimum number of coins needed to make up the amount.
    Return -1 if the amount cannot be made with the given coins.

    Approach: build dp array where dp[i] = min coins to make amount i.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # base case: 0 coins needed to make amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    print(coin_change([1, 5, 10, 25], 36))  # 3  → 25+10+1
    print(coin_change([2], 3))              # -1 → impossible
    print(coin_change([1, 2, 5], 11))       # 3  → 5+5+1
    print(coin_change([1], 0))              # 0
