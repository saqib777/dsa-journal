
# Algorithm: Iterative Binary Search
# Time Complexity: O(log n) - search space halved each iteration
# Space Complexity: O(1) - no extra space used

def binary_search(arr: list[int], target: int) -> int:
    """
    Given a sorted array and a target value, return the index
    of the target if found, otherwise return -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    print(binary_search([-1, 0, 3, 5, 9, 12], 9))   # 4
    print(binary_search([-1, 0, 3, 5, 9, 12], 2))   # -1
    print(binary_search([5], 5))                      # 0
    print(binary_search([], 5))                       # -1
