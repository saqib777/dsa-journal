# Algorithm: Sort + Two Pointers
# Time Complexity:  O(n^2) — outer loop O(n), inner two-pointer O(n)
# Space Complexity: O(1)   — ignoring output list, sorting is in-place

def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Find all unique triplets in the array that sum to zero.
    No duplicate triplets in the output.

    Approach:
    1. Sort the array
    2. Fix one element, use two pointers for the remaining two
    3. Skip duplicates at every level
    """
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # skip duplicate values for the fixed element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left  = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left  += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
    print(three_sum([0, 0, 0]))               # [[0,0,0]]
    print(three_sum([1, 2, -2, -1]))          # []
