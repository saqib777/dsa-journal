# Algorithm: Two Pointers
# Time Complexity:  O(n) — single pass
# Space Complexity: O(1) — no extra arrays

def trap(height: list[int]) -> int:
    """
    Calculate total water trapped after raining.

    Two pointer approach:
    - Maintain left_max and right_max as we move inward
    - Water at position i = min(left_max, right_max) - height[i]
    - Process whichever side has the smaller maximum —
      that side's water amount is already determined

    Example:
        height = [0,1,0,2,1,0,1,3,2,1,2,1] → 6
        height = [4,2,0,3,2,5]              → 9
    """
    if not height:
        return 0

    left, right     = 0, len(height) - 1
    left_max        = height[left]
    right_max       = height[right]
    water           = 0

    while left < right:
        if left_max <= right_max:
            left     += 1
            left_max  = max(left_max, height[left])
            water    += left_max - height[left]
        else:
            right    -= 1
            right_max = max(right_max, height[right])
            water    += right_max - height[right]

    return water


def trap_dp(height: list[int]) -> int:
    """
    DP approach — precompute left_max and right_max arrays.
    More intuitive but uses O(n) space.
    Time: O(n), Space: O(n)
    """
    if not height:
        return 0

    n         = len(height)
    left_max  = [0] * n
    right_max = [0] * n

    left_max[0]    = height[0]
    right_max[n-1] = height[n-1]

    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])

    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    return sum(
        min(left_max[i], right_max[i]) - height[i]
        for i in range(n)
    )


if __name__ == "__main__":
    for fn in [trap, trap_dp]:
        print(fn([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
        print(fn([4,2,0,3,2,5]))               # 9
        print(fn([1,0,1]))                     # 1
        print(fn([3,0,0,2,0,4]))               # 10
        print("---")
