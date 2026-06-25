# Algorithm: Bucket Sort by Frequency
# Time Complexity:  O(n) — bucket sort avoids O(n log n) sorting
# Space Complexity: O(n) — frequency map + buckets

from collections import Counter
import heapq


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Return the k most frequent elements.

    Bucket sort approach: index = frequency, value = list of numbers
    with that frequency. Since max frequency is bounded by len(nums),
    we can bucket sort in O(n) instead of O(n log n) sorting.

    Example:
        nums = [1,1,1,2,2,3], k = 2 → [1, 2]
    """
    count   = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result

    return result


def top_k_frequent_heap(nums: list[int], k: int) -> list[int]:
    """
    Min-heap approach.
    Time: O(n log k), Space: O(n)
    Better when k is much smaller than n.
    """
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)


def top_k_frequent_words(words: list[str], k: int) -> list[str]:
    """
    Variant: top k frequent words, tie-broken alphabetically.
    Uses heap with custom comparator (frequency desc, alpha asc).
    """
    count = Counter(words)
    # heapq is min-heap, so negate frequency for max-heap-like behaviour
    heap  = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == "__main__":
    print(top_k_frequent([1,1,1,2,2,3], 2))         # [1, 2]
    print(top_k_frequent([1], 1))                     # [1]
    print(top_k_frequent_heap([1,1,1,2,2,3], 2))     # [1, 2]

    print(top_k_frequent_words(
        ["i","love","leetcode","i","love","coding"], 2
    ))  # ['i', 'love']
