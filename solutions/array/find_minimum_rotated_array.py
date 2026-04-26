# Algorithm: Binary Search
# Time Complexity:  O(log n) — search space halved each step
# Space Complexity: O(1)     — no extra space

def find_minimum(nums: list[int]) -> int:
    """
    Find the minimum element in a rotated sorted array.

    The array was originally sorted ascending then rotated
    at some unknown pivot. No duplicates.

    Key insight: the minimum is the only element smaller
    than its predecessor. Binary search on which half
    is unsorted — the minimum always lives there.

    Example:
        [3, 4, 5, 1, 2] → 1
        [4, 5, 6, 7, 0, 1, 2] → 0
        [11, 13, 15, 17] → 11  (no rotation)
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            # Minimum is in the right half
            left = mid + 1
        else:
            # Minimum is in the left half (including mid)
            right = mid

    return nums[left]


def find_minimum_with_duplicates(nums: list[int]) -> int:
    """
    Variant: handles duplicates.
    When nums[mid] == nums[right], we cannot determine which
    half the minimum is in — shrink right by 1 to eliminate
    one duplicate safely.
    Time: O(n) worst case when all duplicates, O(log n) average.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right -= 1   # cannot determine — shrink safely

    return nums[left]


if __name__ == "__main__":
    print(find_minimum([3, 4, 5, 1, 2]))          # 1
    print(find_minimum([4, 5, 6, 7, 0, 1, 2]))    # 0
    print(find_minimum([11, 13, 15, 17]))          # 11
    print(find_minimum([1]))                       # 1
    print(find_minimum([2, 1]))                    # 1

    print(find_minimum_with_duplicates([2,2,2,0,1]))  # 0
    print(find_minimum_with_duplicates([1,3,5]))      # 1
