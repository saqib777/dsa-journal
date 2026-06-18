
# Algorithm: Boyer-Moore Voting Algorithm
# Time Complexity:  O(n) — single pass
# Space Complexity: O(1) — two variables only

def majority_element(nums: list[int]) -> int:
    """
    Return the element that appears more than n/2 times.
    Assumes a majority element always exists.

    Boyer-Moore Voting intuition:
    - Maintain a candidate and a counter.
    - If current number matches candidate, increment counter.
    - Otherwise decrement counter.
    - If counter hits 0, switch candidate to current number.

    Why it works: the majority element appears more than all
    others combined, so it always "wins" the cancellation process.

    Example:
        [2,2,1,1,1,2,2] → 2
        [3,2,3]          → 3
    """
    candidate = None
    count     = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate


def majority_element_hashmap(nums: list[int]) -> int:
    """
    Simpler hash map approach for comparison.
    Time: O(n), Space: O(n)
    """
    freq = {}
    n    = len(nums)

    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > n // 2:
            return num

    return -1


def majority_element_ii(nums: list[int]) -> list[int]:
    """
    Variant: find all elements appearing more than n/3 times.
    At most 2 such elements can exist.
    Extended Boyer-Moore with two candidates.
    Time: O(n), Space: O(1)
    """
    candidate1 = candidate2 = None
    count1     = count2     = 0

    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    result = []
    n      = len(nums)
    for candidate in (candidate1, candidate2):
        if nums.count(candidate) > n // 3:
            result.append(candidate)

    return result


if __name__ == "__main__":
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))   # 2
    print(majority_element([3, 2, 3]))                # 3
    print(majority_element_hashmap([6, 5, 5]))        # 5

    print(majority_element_ii([3, 2, 3]))             # [3]
    print(majority_element_ii([1, 1, 1, 3, 3, 2, 2, 2]))  # [1, 2] or [2, 1]
