# Algorithm: Greedy (Track Maximum Reachable Index)
# Time Complexity:  O(n) — single pass
# Space Complexity: O(1) — one variable

def can_jump(nums: list[int]) -> bool:
    """
    Determine if you can reach the last index.
    nums[i] = maximum jump length from position i.

    Greedy: track the furthest index reachable so far.
    If current index exceeds that, we are stuck.

    Example:
        [2,3,1,1,4] → True  (jump 1→3→4 or 1→2→3→4)
        [3,2,1,0,4] → False (always land on index 3 which has 0)
    """
    max_reach = 0

    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)

    return True


def min_jumps(nums: list[int]) -> int:
    """
    Variant: return the minimum number of jumps to reach the last index.
    Assumes it is always possible to reach the end.

    BFS-style greedy: track current window end and furthest reachable.
    When we exhaust the current window, we must jump — increment count.

    Time: O(n), Space: O(1)
    """
    jumps       = 0
    current_end = 0
    farthest    = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps      += 1
            current_end = farthest

    return jumps


if __name__ == "__main__":
    print(can_jump([2, 3, 1, 1, 4]))  # True
    print(can_jump([3, 2, 1, 0, 4]))  # False
    print(can_jump([0]))               # True
    print(can_jump([1, 0, 1, 0]))     # False

    print(min_jumps([2, 3, 1, 1, 4]))    # 2
    print(min_jumps([2, 3, 0, 1, 4]))    # 2
    print(min_jumps([1, 1, 1, 1]))       # 3
