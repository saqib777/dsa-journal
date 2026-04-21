# Algorithm: Depth-First Search (Flood Fill)
# Time Complexity:  O(m * n) — every cell visited at most once
# Space Complexity: O(m * n) — recursion stack in worst case

def num_islands(grid: list[list[str]]) -> int:
    """
    Given a 2D grid of '1's (land) and '0's (water),
    count the number of islands.

    An island is surrounded by water and formed by connecting
    adjacent land cells horizontally or vertically.

    Approach: DFS flood-fill — when we find a '1', increment
    the counter and sink the entire connected island to '0'
    to avoid counting it twice.
    """
    if not grid:
        return 0

    rows    = len(grid)
    cols    = len(grid[0])
    count   = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'          # sink the land
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count


if __name__ == "__main__":
    grid1 = [
        ['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0'],
    ]
    print(num_islands(grid1))  # 1

    grid2 = [
        ['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1'],
    ]
    print(num_islands(grid2))  # 3
