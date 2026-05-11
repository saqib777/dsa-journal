# Algorithm: Prefix Sum + Hash Map
# Time Complexity:  O(n) — single pass
# Space Complexity: O(n) — prefix sum frequency map

from collections import defaultdict


def subarray_sum(nums: list[int], k: int) -> int:
    """
    Count the number of continuous subarrays whose sum equals k.

    Key insight: if prefix_sum[j] - prefix_sum[i] == k,
    then subarray nums[i+1..j] sums to k.

    Equivalently: prefix_sum[j] - k == prefix_sum[i]
    So for each j, we look up how many previous prefix sums
    equal prefix_sum[j] - k.

    Works with negative numbers — unlike sliding window.

    Example:
        nums = [1, 1, 1], k = 2 → 2
        nums = [1, 2, 3], k = 3 → 2  ([1,2] and [3])
    """
    count      = 0
    prefix_sum = 0
    freq       = defaultdict(int)
    freq[0]    = 1   # empty prefix

    for num in nums:
        prefix_sum += num
        count      += freq[prefix_sum - k]
        freq[prefix_sum] += 1

    return count


def max_subarray_sum_k(nums: list[int], k: int) -> int:
    """
    Variant: find the maximum length subarray with sum exactly k.
    Uses prefix sum + hash map storing first occurrence index.
    Time: O(n), Space: O(n)
    """
    prefix_sum  = 0
    first_seen  = {0: -1}
    max_length  = 0

    for i, num in enumerate(nums):
        prefix_sum += num
        if prefix_sum - k in first_seen:
            max_length = max(max_length, i - first_seen[prefix_sum - k])
        if prefix_sum not in first_seen:
            first_seen[prefix_sum] = i

    return max_length


def subarray_sum_divisible_by_k(nums: list[int], k: int) -> int:
    """
    Variant: count subarrays whose sum is divisible by k.
    Uses remainder frequency map.
    Time: O(n), Space: O(k)
    """
    count      = 0
    prefix_sum = 0
    remainders = defaultdict(int)
    remainders[0] = 1

    for num in nums:
        prefix_sum = (prefix_sum + num) % k
        if prefix_sum < 0:
            prefix_sum += k
        count += remainders[prefix_sum]
        remainders[prefix_sum] += 1

    return count


if __name__ == "__main__":
    print(subarray_sum([1, 1, 1], 2))          # 2
    print(subarray_sum([1, 2, 3], 3))          # 2
    print(subarray_sum([-1, -1, 1], 0))        # 1

    print(max_subarray_sum_k([1, -1, 5, -2, 3], 3))   # 4
    print(max_subarray_sum_k([-2, -1, 2, 1], 1))       # 2

    print(subarray_sum_divisible_by_k([4,5,0,-2,-3,1], 5))  # 7
