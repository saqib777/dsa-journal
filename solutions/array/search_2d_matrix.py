# Algorithm: Binary Search (Treat Matrix as Flat Sorted Array)
# Time Complexity:  O(log(m*n)) — single binary search over m*n elements
# Space Complexity: O(1)

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """
    Search for target in an m x n matrix where:
    - Each row is sorted ascending left to right
    - First element of each row > last element of previous row
    (The matrix is essentially one sorted array laid out in rows)

    Approach: treat the 2D matrix as a flat 1D sorted array.
    Use virtual index mid, convert to (row, col) on the fly.
    Binary search runs in O(log(m*n)).

    Example:
        matrix = [[1,3,5,7],
                  [10,11,16,20],
                  [23,30,34,60]]
        target = 3  → True
        target = 13 → False
    """
    if not matrix or not matrix[0]:
        return False

    m, n   = len(matrix), len(matrix[0])
    left   = 0
    right  = m * n - 1

    while left <= right:
        mid     = left + (right - left) // 2
        row     = mid // n
        col     = mid %  n
        element = matrix[row][col]

        if element == target:
            return True
        elif element < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def search_matrix_ii(matrix: list[list[int]], target: int) -> bool:
    """
    Variant: matrix where rows AND columns are sorted,
    but first element of row is NOT necessarily > last of previous row.
    Uses staircase search starting from top-right corner.

    Time: O(m + n), Space: O(1)

    At each step: if current > target → move left (smaller)
                  if current < target → move down (larger)
    """
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    row, col   = 0, cols - 1   # start top-right

    while row < rows and col >= 0:
        element = matrix[row][col]
        if element == target:
            return True
        elif element > target:
            col -= 1   # move left
        else:
            row += 1   # move down

    return False


if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(search_matrix(matrix, 3))    # True
    print(search_matrix(matrix, 13))   # False
    print(search_matrix(matrix, 1))    # True
    print(search_matrix(matrix, 60))   # True

    matrix2 = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]
    print(search_matrix_ii(matrix2, 5))   # True
    print(search_matrix_ii(matrix2, 20))  # False
