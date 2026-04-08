# Algorithm: Dynamic Programming (Track Min and Max)
# Time Complexity:  O(n) — single pass
# Space Complexity: O(1) — four variables only

def max_product(nums: list[int]) -> int:
    """
    Find the contiguous subarray with the largest product.
    Must track both max and min because a negative * negative = positive.
    """
    global_max = nums[0]
    local_max  = nums[0]
    local_min  = nums[0]

    for num in nums[1:]:
        candidates = (num, local_max * num, local_min * num)
        local_max  = max(candidates)
        local_min  = min(candidates)
        global_max = max(global_max, local_max)

    return global_max


if __name__ == "__main__":
    print(max_product([2, 3, -2, 4]))        # 6
    print(max_product([-2, 0, -1]))           # 0
    print(max_product([-2, 3, -4]))           # 24
