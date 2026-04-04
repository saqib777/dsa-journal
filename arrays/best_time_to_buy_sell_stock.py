# Algorithm: Greedy (Single Pass)
# Time Complexity: O(n) - one pass through prices
# Space Complexity: O(1) - only two variables tracked

def max_profit(prices: list[int]) -> int:
    """
    Given an array of stock prices where prices[i] is the price on day i,
    return the maximum profit from one buy and one sell.
    Return 0 if no profit is possible.
    """
    if not prices:
        return 0

    min_price = float('inf')
    max_profit_val = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit_val:
            max_profit_val = price - min_price

    return max_profit_val


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))   # 5
    print(max_profit([7, 6, 4, 3, 1]))       # 0
    print(max_profit([2, 4, 1]))             # 2
