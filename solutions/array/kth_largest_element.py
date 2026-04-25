# Algorithm: Min-Heap of size k
# Time Complexity:  O(n log k) — heap maintains size k
# Space Complexity: O(k)       — heap stores k elements

import heapq
import random


def kth_largest_heap(nums: list[int], k: int) -> int:
    """
    Find the kth largest element in an unsorted array.
    Does NOT sort — uses a min-heap of size k.

    The heap always holds the k largest elements seen so far.
    The top of the heap (smallest of the k largest) is the answer.
    """
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


def kth_largest_quickselect(nums: list[int], k: int) -> int:
    """
    QuickSelect — average O(n), worst O(n^2).
    Works like QuickSort but only recurses into ONE partition.

    Target index in sorted descending order: len(nums) - k
    """
    target = len(nums) - k

    def quickselect(left: int, right: int) -> int:
        pivot = nums[right]
        store = left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[i], nums[store] = nums[store], nums[i]
                store += 1

        nums[store], nums[right] = nums[right], nums[store]

        if store == target:
            return nums[store]
        elif store < target:
            return quickselect(store + 1, right)
        else:
            return quickselect(left, store - 1)

    return quickselect(0, len(nums) - 1)


if __name__ == "__main__":
    print(kth_largest_heap([3,2,1,5,6,4], 2))          # 5
    print(kth_largest_heap([3,2,3,1,2,4,5,5,6], 4))    # 4
    print(kth_largest_quickselect([3,2,1,5,6,4], 2))   # 5
    print(kth_largest_quickselect([3,2,3,1,2,4,5,5,6],4)) # 4
