# Algorithm: Dynamic Programming (Bottom-Up, Space Optimised)
# Time Complexity:  O(n) — single pass
# Space Complexity: O(1) — two variables, same idea as Fibonacci

def climb_stairs(n: int) -> int:
    """
    You can climb 1 or 2 steps at a time.
    Return the number of distinct ways to reach the top (n steps).

    Pattern: climb_stairs(n) = climb_stairs(n-1) + climb_stairs(n-2)
    This is exactly the Fibonacci sequence offset by one.
    """
    if n <= 2:
        return n

    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr

    return curr


if __name__ == "__main__":
    print(climb_stairs(2))   # 2  → [1+1, 2]
    print(climb_stairs(3))   # 3  → [1+1+1, 1+2, 2+1]
    print(climb_stairs(5))   # 8
    print(climb_stairs(10))  # 89
