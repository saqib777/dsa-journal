
# Algorithm: Sliding Window + Hash Set
# Time Complexity: O(n) - each character visited at most twice
# Space Complexity: O(min(n, m)) - where m is the charset size

def length_of_longest_substring(s: str) -> int:
    """
    Given a string, return the length of the longest substring
    without repeating characters.
    """
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3
    print(length_of_longest_substring("bbbbb"))     # 1
    print(length_of_longest_substring("pwwkew"))    # 3
    print(length_of_longest_substring(""))          # 0
