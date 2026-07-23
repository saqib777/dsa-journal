# Algorithm: Sliding Window with Frequency Map
# Time Complexity:  O(n) — single pass, 26-character max map
# Space Complexity: O(1) — at most 26 keys in frequency map

from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
    """
    Return the length of the longest substring containing only
    one distinct letter after replacing at most k characters.

    Key insight:
    A window is valid if:
        (window_length - count_of_most_frequent_char) <= k

    The replacements needed = window size minus the dominant character count.
    If replacements needed exceed k, shrink from the left.

    We never shrink max_count below its highest value seen — this works
    because a smaller window with a lower max_count cannot give a
    longer valid window than what we have already found.

    Example:
        s = "AABABBA", k = 1 → 4  ("AABA" or "ABBA" with one replacement)
        s = "ABAB",    k = 2 → 4  (replace both Bs or both As)
    """
    count     = defaultdict(int)
    max_count = 0
    left      = 0
    result    = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_count        = max(max_count, count[s[right]])

        window_size      = right - left + 1
        replacements     = window_size - max_count

        if replacements > k:
            count[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result


def character_replacement_all_windows(s: str, k: int) -> list[str]:
    """
    Variant: return all longest valid substrings (not just length).
    Useful for debugging and visualization.
    """
    max_len = character_replacement(s, k)
    results = []

    count     = defaultdict(int)
    max_count = 0
    left      = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_count        = max(max_count, count[s[right]])

        if right - left + 1 - max_count > k:
            count[s[left]] -= 1
            left += 1

        window = s[left:right + 1]
        if len(window) == max_len:
            results.append(window)

    return results


if __name__ == "__main__":
    print(character_replacement("AABABBA", 1))   # 4
    print(character_replacement("ABAB",    2))   # 4
    print(character_replacement("AAAA",    2))   # 4
    print(character_replacement("AABCCBB", 2))   # 5

    print(character_replacement_all_windows("AABABBA", 1))
