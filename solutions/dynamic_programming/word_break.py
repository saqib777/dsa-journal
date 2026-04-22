# Algorithm: Dynamic Programming (Bottom-Up 1D)
# Time Complexity:  O(n^2 * m) — n = string length, m = avg word length check
# Space Complexity: O(n)       — dp array of length n+1

def word_break(s: str, word_dict: list[str]) -> bool:
    """
    Return True if string s can be segmented into a space-separated
    sequence of one or more words from the dictionary.

    Example:
        s = "leetcode", wordDict = ["leet", "code"]
        Output: True  →  "leet code"

    Approach:
    dp[i] = True if s[:i] can be segmented using the dictionary.
    For each position i, try all words — if dp[i - len(w)] is True
    and s ends with word w at position i, then dp[i] = True.
    """
    word_set = set(word_dict)
    n        = len(s)
    dp       = [False] * (n + 1)
    dp[0]    = True   # empty string is always segmentable

    for i in range(1, n + 1):
        for word in word_set:
            w_len = len(word)
            if i >= w_len and dp[i - w_len] and s[i - w_len:i] == word:
                dp[i] = True
                break

    return dp[n]


def word_break_paths(s: str, word_dict: list[str]) -> list[str]:
    """
    Variant: return all valid segmentations.
    Uses backtracking with memoisation.
    """
    word_set = set(word_dict)
    memo     = {}

    def backtrack(start: int) -> list[str]:
        if start in memo:
            return memo[start]
        if start == len(s):
            return [""]
        results = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_set:
                for rest in backtrack(end):
                    results.append(word + (" " + rest if rest else ""))
        memo[start] = results
        return results

    return backtrack(0)


if __name__ == "__main__":
    print(word_break("leetcode", ["leet", "code"]))           # True
    print(word_break("applepenapple", ["apple", "pen"]))      # True
    print(word_break("catsandog", ["cats", "dog", "sand"]))   # False

    print(word_break_paths("catsanddog", ["cat","cats","and","sand","dog"]))
    # ['cats and dog', 'cat sand dog']
