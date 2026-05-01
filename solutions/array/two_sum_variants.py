# Algorithm: Various — Hash Map, Two Pointer, Binary Search
# All variants of the classic Two Sum problem

def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """
    Two Sum II — input array is sorted ascending.
    Use two pointers instead of a hash map.
    Time: O(n), Space: O(1)

    Returns 1-indexed positions as per the classic problem.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1

    return []


def two_sum_count_pairs(nums: list[int], target: int) -> int:
    """
    Count the number of pairs that sum to target.
    Pairs (i,j) where i < j.
    Time: O(n), Space: O(n)
    """
    seen  = {}
    count = 0

    for num in nums:
        complement = target - num
        if complement in seen:
            count += seen[complement]
        seen[num] = seen.get(num, 0) + 1

    return count


def two_sum_all_pairs(nums: list[int], target: int) -> list[list[int]]:
    """
    Return ALL unique pairs (not indices) that sum to target.
    Handles duplicates. Returns sorted pairs.
    Time: O(n log n), Space: O(n)
    """
    nums.sort()
    result = []
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            result.append([nums[left], nums[right]])
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            left  += 1
            right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1

    return result


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    """
    Find all unique quadruplets that sum to target.
    Extension: fix two pointers, use two-pointer for inner pair.
    Time: O(n^3), Space: O(1) ignoring output
    """
    nums.sort()
    n      = len(nums)
    result = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left]  == nums[left + 1]:  left  += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    left  += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result


if __name__ == "__main__":
    print(two_sum_sorted([2, 7, 11, 15], 9))          # [1, 2]
    print(two_sum_sorted([2, 3, 4], 6))                # [1, 3]

    print(two_sum_count_pairs([1, 5, 3, 3, 3], 6))    # 4
    print(two_sum_all_pairs([1,1,2,2,3,4,4,5], 5))    # [[1,4],[2,3]]

    print(four_sum([1,0,-1,0,-2,2], 0))
    # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
