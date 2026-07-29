
# Algorithm: Two Pointers
# Time Complexity:  O(n) — single inward pass
# Space Complexity: O(1) — two pointers only

def max_area(height: list[int]) -> int:
    """
    Given n vertical lines, find two that together with the x-axis
    form a container that holds the most water.

    Width  = right - left (distance between the two lines)
    Height = min(height[left], height[right]) (shorter line is the limit)
    Area   = width * height

    Two pointer greedy:
    Start from the widest container (left=0, right=end).
    Move the pointer with the SHORTER line inward — this is the only
    move that could possibly find a larger area.
    Moving the taller line inward guarantees a smaller or equal area
    (width decreases, height bounded by same short line or shorter).

    Example:
        [1,8,6,2,5,4,8,3,7] → 49  (lines at index 1 and 8: min(8,7)*7=49)
    """
    left   = 0
    right  = len(height) - 1
    result = 0

    while left < right:
        width  = right - left
        h      = min(height[left], height[right])
        result = max(result, width * h)

        if height[left] <= height[right]:
            left  += 1
        else:
            right -= 1

    return result


def max_area_with_positions(height: list[int]) -> tuple[int, int, int]:
    """
    Variant: return (max_area, left_index, right_index) of the best pair.
    """
    left   = 0
    right  = len(height) - 1
    result = 0
    best_l = 0
    best_r = len(height) - 1

    while left < right:
        area = (right - left) * min(height[left], height[right])
        if area > result:
            result = area
            best_l = left
            best_r = right
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return result, best_l, best_r


if __name__ == "__main__":
    print(max_area([1,8,6,2,5,4,8,3,7]))   # 49
    print(max_area([1,1]))                  # 1
    print(max_area([4,3,2,1,4]))            # 16
    print(max_area([1,2,1]))                # 2

    area, l, r = max_area_with_positions([1,8,6,2,5,4,8,3,7])
    print(f"Area={area} between index {l} and {r}")  # Area=49 between 1 and 8
