# Algorithm: Dynamic Programming (Space-Optimised)
# Time Complexity:  O(n) — single pass
# Space Complexity: O(1) — two variables, no array needed

def rob(nums: list[int]) -> int:
    """
    You are a robber. Houses are in a line. Adjacent houses
    have a security system — robbing two adjacent houses triggers an alarm.
    Return the maximum amount you can rob tonight.

    Recurrence:
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    Optimised: only need the previous two values, not a full array.
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2   = prev1
        prev1   = current

    return prev1


if __name__ == "__main__":
    print(rob([1, 2, 3, 1]))        # 4  → rob house 0 and 2
    print(rob([2, 7, 9, 3, 1]))     # 12 → rob house 0, 2, 4
    print(rob([2, 1, 1, 2]))        # 4  → rob house 0 and 3
    print(rob([5]))                  # 5
