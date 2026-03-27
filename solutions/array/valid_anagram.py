# Algorithm: Hash Map (Character Frequency Count)
# Time Complexity: O(n) - where n is the length of the string
# Space Complexity: O(1) - at most 26 keys in the map (fixed alphabet)

def valid_anagram(s: str, t: str) -> bool:
    """
    Given two strings s and t, return True if t is an anagram of s,
    and False otherwise.
    An anagram uses the same characters in the same frequency, different order.
    """
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True


if __name__ == "__main__":
    print(valid_anagram("anagram", "nagaram"))  # True
    print(valid_anagram("rat", "car"))          # False
    print(valid_anagram("listen", "silent"))    # True
