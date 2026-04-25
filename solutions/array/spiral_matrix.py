# Algorithm: Layer-by-Layer Boundary Shrinking
# Time Complexity:  O(m * n) — every cell visited exactly once
# Space Complexity: O(1)     — output array not counted as extra space

def spiral_order(matrix: list[list[int]]) -> list[int]:
    """
    Return all elements of a 2D matrix in spiral order
    (clockwise from the outermost layer inward).

    Example:
        Input:  [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
        Output: [1,2,3,6,9,8,7,4,5]

    Approach: maintain four boundaries (top, bottom, left, right).
    Traverse each boundary in order, then shrink it inward.
    """
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse right across the top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse down the right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Traverse left across the bottom row (if still valid)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Traverse up the left column (if still valid)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


def generate_spiral(n: int) -> list[list[int]]:
    """
    Variant: generate an n x n matrix filled in spiral order.
    Uses the same boundary approach, filling values 1 to n^2.
    """
    matrix  = [[0] * n for _ in range(n)]
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            matrix[top][col] = num; num += 1
        top += 1
        for row in range(top, bottom + 1):
            matrix[row][right] = num; num += 1
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num; num += 1
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num; num += 1
            left += 1

    return matrix


if __name__ == "__main__":
    print(spiral_order([[1,2,3],[4,5,6],[7,8,9]]))        # [1,2,3,6,9,8,7,4,5]
    print(spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]
    print(spiral_order([[1]]))                              # [1]

    for row in generate_spiral(4):
        print(row)
