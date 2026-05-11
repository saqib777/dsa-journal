import pytest
from encode_decode_strings import encode, decode, encode_chunked, decode_chunked


def roundtrip(strs):
    return decode(encode(strs))


def roundtrip_chunked(strs):
    return decode_chunked(encode_chunked(strs))


def test_basic():
    assert roundtrip(["hello", "world"]) == ["hello", "world"]

def test_empty_string_in_list():
    assert roundtrip(["", "abc", ""]) == ["", "abc", ""]

def test_all_empty():
    assert roundtrip(["", "", ""]) == ["", "", ""]

def test_delimiter_in_string():
    assert roundtrip(["5#tricky", "hello"]) == ["5#tricky", "hello"]

def test_single_string():
    assert roundtrip(["only"]) == ["only"]

def test_empty_list():
    assert roundtrip([]) == []

def test_special_characters():
    strs = ["hello\nworld", "tab\there", "quote\"here"]
    assert roundtrip(strs) == strs

def test_unicode():
    strs = ["こんにちは", "🦁", "café"]
    assert roundtrip(strs) == strs

def test_with_spaces():
    assert roundtrip(["with spaces", "and more"]) == ["with spaces", "and more"]

def test_chunked_basic():
    assert roundtrip_chunked(["hello", "world"]) == ["hello", "world"]

def test_chunked_empty_string():
    assert roundtrip_chunked(["", "abc"]) == ["", "abc"]

def test_chunked_delimiter_in_string():
    assert roundtrip_chunked(["5#trick"]) == ["5#trick"]

def test_both_methods_agree():
    cases = [
        ["hello", "world"],
        ["", "abc", ""],
        ["5#tricky"],
        ["single"],
    ]
    for strs in cases:
        assert roundtrip(strs) == roundtrip_chunked(strs)

@pytest.mark.parametrize("strs", [
    ["a", "b", "c"],
    ["", ""],
    ["long string with spaces and 5#delimiter"],
    ["one"],
])
def test_parametrized(strs):
    assert roundtrip(strs) == strs
