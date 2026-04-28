# Algorithm: Backtracking DFS on 2D Grid
# Time Complexity:  O(m * n * 4^L) — L = word length, 4 directions each step
# Space Complexity: O(L)           — recursion stack depth equals word length

def exist(board: list[list[str]], word: str) -> bool:
    """
    Return True if word exists in the 2D grid of characters.
    Word must be formed by sequentially adjacent cells
    (horizontally or vertically). Same cell cannot be reused.

    Approach: for each cell, try DFS backtracking.
    Mark visited cells temporarily to avoid reuse,
    restore them after backtracking.

    Example:
        board = [['A','B','C','E'],
                 ['S','F','C','S'],
                 ['A','D','E','E']]
        word = "ABCCED" → True
        word = "SEE"    → True
        word = "ABCB"   → False
    """
    rows = len(board)
    cols = len(board[0])

    def dfs(r: int, c: int, idx: int) -> bool:
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[idx]:
            return False

        temp         = board[r][c]
        board[r][c]  = '#'          # mark visited

        found = (dfs(r+1, c, idx+1) or
                 dfs(r-1, c, idx+1) or
                 dfs(r, c+1, idx+1) or
                 dfs(r, c-1, idx+1))

        board[r][c] = temp          # restore (backtrack)
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True

    return False


def find_all_word_positions(board: list[list[str]], word: str) -> list[tuple]:
    """
    Variant: return starting positions of all occurrences of word.
    """
    rows    = len(board)
    cols    = len(board[0])
    starts  = []

    def dfs(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[idx]:
            return False
        temp        = board[r][c]
        board[r][c] = '#'
        found = (dfs(r+1,c,idx+1) or dfs(r-1,c,idx+1) or
                 dfs(r,c+1,idx+1) or dfs(r,c-1,idx+1))
        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                starts.append((r, c))

    return starts


if __name__ == "__main__":
    board = [['A','B','C','E'],
             ['S','F','C','S'],
             ['A','D','E','E']]

    print(exist(board, "ABCCED"))   # True
    print(exist(board, "SEE"))      # True
    print(exist(board, "ABCB"))     # False

    print(find_all_word_positions(board, "SEE"))  # [(1,3)]
