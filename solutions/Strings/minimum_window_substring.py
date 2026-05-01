# Algorithm: Sliding Window with Frequency Maps
# Time Complexity:  O(n + m) — n = len(s), m = len(t)
# Space Complexity: O(n + m) — two frequency maps

from collections import defaultdict


def min_window(s: str, t: str) -> str:
    """
    Find the minimum window substring in s that contains
    all characters of t (including duplicates).
    Returns empty string if no such window exists.

    Approach:
    - need: frequency map of t
    - have: frequency map of current window
    - formed: how many unique chars in t are satisfied
    - Expand right until window is valid, then shrink left
      to find the minimum valid window.

    Example:
        s = "ADOBECODEBANC", t = "ABC" → "BANC"
        s = "a", t = "a"              → "a"
        s = "a", t = "aa"             → ""
    """
    if not s or not t:
        return ""

    need     = defaultdict(int)
    for ch in t:
        need[ch] += 1

    have     = defaultdict(int)
    required = len(need)
    formed   = 0
    left     = 0
    best_len = float('inf')
    best_l   = 0

    for right in range(len(s)):
        ch = s[right]
        have[ch] += 1

        if ch in need and have[ch] == need[ch]:
            formed += 1

        while formed == required:
            window_len = right - left + 1
            if window_len < best_len:
                best_len = window_len
                best_l   = left

            lch = s[left]
            have[lch] -= 1
            if lch in need and have[lch] < need[lch]:
                formed -= 1
            left += 1

    return s[best_l:best_l + best_len] if best_len != float('inf') else ""


def min_window_all(s: str, t: str) -> list[str]:
    """
    Variant: return all minimum window substrings (if multiple exist).
    """
    if not s or not t:
        return []

    need     = defaultdict(int)
    for ch in t:
        need[ch] += 1

    have     = defaultdict(int)
    required = len(need)
    formed   = 0
    left     = 0
    best_len = float('inf')
    results  = []

    for right in range(len(s)):
        ch = s[right]
        have[ch] += 1
        if ch in need and have[ch] == need[ch]:
            formed += 1

        while formed == required:
            window_len = right - left + 1
            if window_len < best_len:
                best_len = window_len
                results  = [s[left:right + 1]]
            elif window_len == best_len:
                results.append(s[left:right + 1])

            lch = s[left]
            have[lch] -= 1
            if lch in need and have[lch] < need[lch]:
                formed -= 1
            left += 1

    return results


if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))  # "BANC"
    print(min_window("a", "a"))                # "a"
    print(min_window("a", "aa"))               # ""
    print(min_window("aa", "aa"))              # "aa"
    print(min_window("cabwefgewcwaefgcf","cae")) # "cwae" or "cae"
