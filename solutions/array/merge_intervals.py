# Algorithm: Sort by Start Time + Linear Merge
# Time Complexity:  O(n log n) — dominated by sorting
# Space Complexity: O(n)       — output array

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Merge all overlapping intervals.

    Two intervals [a,b] and [c,d] overlap if c <= b.
    After sorting by start time, we only need to compare
    each interval with the last merged interval.

    Example:
        [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]
        [[1,4],[4,5]]               → [[1,5]]
    """
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


def insert_interval(intervals: list[list[int]],
                    new_interval: list[int]) -> list[list[int]]:
    """
    Insert a new interval into a sorted non-overlapping list.
    Merge if necessary. Does not re-sort — uses linear scan.
    Time: O(n), Space: O(n)

    Example:
        intervals = [[1,3],[6,9]], new = [2,5] → [[1,5],[6,9]]
        intervals = [[1,2],[3,5],[6,7]], new = [4,8] → [[1,2],[3,8]]
    """
    result = []
    i      = 0
    n      = len(intervals)

    # Add all intervals that end before new_interval starts
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals with new_interval
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    result.append(new_interval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


if __name__ == "__main__":
    print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
    print(merge_intervals([[1,4],[4,5]]))                  # [[1,5]]
    print(merge_intervals([[1,4],[2,3]]))                  # [[1,4]]
    print(merge_intervals([]))                             # []

    print(insert_interval([[1,3],[6,9]], [2,5]))           # [[1,5],[6,9]]
    print(insert_interval([[1,2],[3,5],[6,7],[8,10]], [4,8])) # [[1,2],[3,10]]
