
# Algorithm: Dynamic Programming (Build Row by Row)
# Time Complexity:  O(n^2) — n rows, each row up to n elements
# Space Complexity: O(n^2) — storing all rows

def generate(num_rows: int) -> list[list[int]]:
    """
    Generate the first num_rows of Pascal's Triangle.

    Each number is the sum of the two numbers directly above it.
    Row i has i+1 elements. First and last element of every row is 1.

    Example:
        num_rows = 5
        [[1],
         [1,1],
         [1,2,1],
         [1,3,3,1],
         [1,4,6,4,1]]
    """
    triangle = []

    for row_num in range(num_rows):
        row = [1] * (row_num + 1)

        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        triangle.append(row)

    return triangle


def get_row(row_index: int) -> list[int]:
    """
    Return only the row at row_index (0-indexed), space-optimised.
    Builds the row in-place using O(k) space instead of O(n^2).
    Time: O(k^2), Space: O(k)
    """
    row = [1] * (row_index + 1)

    for i in range(2, row_index + 1):
        for j in range(i - 1, 0, -1):
            row[j] += row[j - 1]

    return row


def get_element(row: int, col: int) -> int:
    """
    Return a single element using the binomial coefficient formula.
    C(row, col) = row! / (col! * (row-col)!)
    Time: O(col)
    """
    if col > row:
        return 0
    result = 1
    for i in range(col):
        result = result * (row - i) // (i + 1)
    return result


if __name__ == "__main__":
    for row in generate(5):
        print(row)
    # [1]
    # [1,1]
    # [1,2,1]
    # [1,3,3,1]
    # [1,4,6,4,1]

    print(get_row(4))          # [1,4,6,4,1]
    print(get_element(4, 2))   # 6
