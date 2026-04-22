# Algorithm: Modified Binary Search
# Time Complexity:  O(log n) — search space halved each step
# Space Complexity: O(1)     — no extra space

def search_rotated(nums: list[int], target: int) -> int:
    """
    Search for target in a sorted array that has been rotated
    at an unknown pivot point.

    Key insight: one half of the array is always sorted.
    Determine which half is sorted, then check if target
    falls within that half to decide where to search.

    Example:
        nums = [4, 5, 6, 7, 0, 1, 2], target = 0
        Output: 4
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == "__main__":
    print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))   # 4
    print(search_rotated([4, 5, 6, 7, 0, 1, 2], 3))   # -1
    print(search_rotated([1], 0))                       # -1
    print(search_rotated([1], 1))                       # 0
    print(search_rotated([3, 1], 1))                    # 1
