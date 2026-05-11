# Algorithm: Length-Prefix Encoding
# Time Complexity:  O(n) encode | O(n) decode
# Space Complexity: O(n)

def encode(strs: list[str]) -> str:
    """
    Encode a list of strings into a single string.
    Uses length-prefix format: {length}#{string}

    This handles all edge cases:
    - Empty strings
    - Strings containing the delimiter character
    - Strings with special characters

    Example:
        ["hello", "world"] → "5#hello5#world"
        ["", "abc"]        → "0#3#abc"
        ["5#tricky"]       → "8#5#tricky"
    """
    return "".join(f"{len(s)}#{s}" for s in strs)


def decode(encoded: str) -> list[str]:
    """
    Decode a length-prefix encoded string back to a list.
    Reads length, skips delimiter, reads exactly that many chars.
    """
    result = []
    i      = 0

    while i < len(encoded):
        j = encoded.index('#', i)
        length = int(encoded[i:j])
        result.append(encoded[j + 1: j + 1 + length])
        i = j + 1 + length

    return result


def encode_chunked(strs: list[str]) -> str:
    """
    Variant: use a 4-byte fixed-length header instead of variable length.
    More robust for binary-like data.
    Length stored as 4 chars zero-padded.
    """
    return "".join(f"{len(s):04d}|{s}" for s in strs)


def decode_chunked(encoded: str) -> list[str]:
    """Decode fixed 4-byte header encoded string."""
    result = []
    i      = 0
    while i < len(encoded):
        length = int(encoded[i:i + 4])
        result.append(encoded[i + 5: i + 5 + length])
        i += 5 + length
    return result


if __name__ == "__main__":
    strs = ["hello", "world", "", "5#tricky", "with spaces"]
    encoded = encode(strs)
    print(encoded)
    decoded = decode(encoded)
    print(decoded)
    print(decoded == strs)   # True

    encoded2 = encode_chunked(strs)
    decoded2 = decode_chunked(encoded2)
    print(decoded2 == strs)  # True
