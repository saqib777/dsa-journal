# Algorithm: Expand Around Centre
# Time Complexity:  O(n^2) — expand from each of 2n-1 centres
# Space Complexity: O(1)   — no extra space beyond result string

def longest_palindrome_expand(s: str) -> str:
    """
    Find the longest palindromic substring using
    expand-around-centre technique.

    For each index, try expanding outward treating it as:
    - Odd-length palindrome centre (single character)
    - Even-length palindrome centre (between two characters)

    Track the longest found so far.
    """
    if not s:
        return ""

    start = end = 0

    def expand(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left  -= 1
            right += 1
        return right - left - 1   # length of palindrome found

    for i in range(len(s)):
        odd_len  = expand(i, i)       # odd length
        even_len = expand(i, i + 1)   # even length
        best     = max(odd_len, even_len)

        if best > end - start + 1:
            start = i - (best - 1) // 2
            end   = i + best // 2

    return s[start:end + 1]


def longest_palindrome_dp(s: str) -> str:
    """
    DP approach — O(n^2) time, O(n^2) space.
    dp[i][j] = True if s[i:j+1] is a palindrome.

    Base cases:
        Single chars: dp[i][i] = True
        Two chars:    dp[i][i+1] = (s[i] == s[i+1])

    Transition:
        dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
    """
    n     = len(s)
    if n == 0:
        return ""

    dp    = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start   = i
            max_len = 2

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    start   = i
                    max_len = length

    return s[start:start + max_len]


def count_palindromic_substrings(s: str) -> int:
    """
    Count all palindromic substrings using expand around centre.
    Time: O(n^2), Space: O(1)
    """
    count = 0

    def expand_count(left: int, right: int):
        nonlocal count
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left  -= 1
            right += 1

    for i in range(len(s)):
        expand_count(i, i)
        expand_count(i, i + 1)

    return count


if __name__ == "__main__":
    for fn in [longest_palindrome_expand, longest_palindrome_dp]:
        print(fn("babad"))     # "bab" or "aba"
        print(fn("cbbd"))      # "bb"
        print(fn("a"))         # "a"
        print(fn("racecar"))   # "racecar"
        print("---")

    print(count_palindromic_substrings("abc"))      # 3
    print(count_palindromic_substrings("aaa"))      # 6
    print(count_palindromic_substrings("racecar"))  # 10
