# Algorithm: Hash Map with Sorted String as Key
# Time Complexity:  O(n * k log k) — n = number of strings, k = max string length
# Space Complexity: O(n * k)       — storing all strings in the hash map

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Group strings that are anagrams of each other.
    Key insight: anagrams have identical sorted characters.

    Example:
        Input:  ["eat","tea","tan","ate","nat","bat"]
        Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    """
    anagram_map = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))   # sorted tuple is hashable
        anagram_map[key].append(word)

    return list(anagram_map.values())


if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    for group in result:
        print(sorted(group))
    # ['ate', 'eat', 'tea']
    # ['nat', 'tan']
    # ['bat']
