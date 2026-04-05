# DSA Journal

A personal journal of Data Structures and Algorithms solutions written in Python.
Each solution includes time/space complexity analysis and pytest test cases - structured
to reflect SDET-oriented thinking.

---

## Structure
```
dsa-journal/
├── solutions/
│   ├── arrays/
│   ├── strings/
│   ├── linked_lists/
│   └── binary_search/
├── notes/
│   ├── complexity_cheatsheet.md
│   └── patterns.md
├── progress/
│   └── tracker.md
├── requirements.txt
└── README.md

```
---

## Solutions

### Arrays

| # | Problem | Solution | Tests | Difficulty | Algorithm | Time | Space |
|---|---------|----------|-------|------------|-----------|------|-------|
| 1 | Two Sum | [two_sum.py](solutions/arrays/two_sum.py) | [test](solutions/arrays/test_two_sum.py) | Easy | Hash Map | O(n) | O(n) |

### Strings

| # | Problem | Solution | Tests | Difficulty | Algorithm | Time | Space |
|---|---------|----------|-------|------------|-----------|------|-------|
| 1 | Valid Anagram | [valid_anagram.py](solutions/strings/valid_anagram.py) | [test](solutions/strings/test_valid_anagram.py) | Easy | Frequency Map | O(n) | O(1) |

### Linked Lists

| # | Problem | Solution | Tests | Difficulty | Algorithm | Time | Space |
|---|---------|----------|-------|------------|-----------|------|-------|
| 1 | Reverse Linked List | [reverse_linked_list.py](solutions/linked_lists/reverse_linked_list.py) | - | Easy | Iterative Reversal | O(n) | O(1) |

### Binary Search

| # | Problem | Solution | Tests | Difficulty | Algorithm | Time | Space |
|---|---------|----------|-------|------------|-----------|------|-------|

### Trees

| # | Problem | Solution | Tests | Difficulty | Algorithm | Time | Space |
|---|---------|----------|-------|------------|-----------|------|-------|

### Dynamic Programming

| # | Problem | Solution | Tests | Difficulty | Algorithm | Time | Space |
|---|---------|----------|-------|------------|-----------|------|-------|

### Graphs

| # | Problem | Solution | Tests | Difficulty | Algorithm | Time | Space |
|---|---------|----------|-------|------------|-----------|------|-------|

---

## Progress

| Category | Solved | Easy | Medium | Hard |
|----------|--------|------|--------|------|
| Arrays | 1 | 1 | 0 | 0 |
| Strings | 1 | 1 | 0 | 0 |
| Linked Lists | 1 | 1 | 0 | 0 |
| Binary Search | 0 | 0 | 0 | 0 |
| Trees | 0 | 0 | 0 | 0 |
| Dynamic Programming | 0 | 0 | 0 | 0 |
| Graphs | 0 | 0 | 0 | 0 |
| **Total** | **3** | **3** | **0** | **0** |

---

## Running Tests
```bash
pip install pytest
pytest solutions/ -v
```

---

## Notes

- [Complexity Cheatsheet](notes/complexity_cheatsheet.md)
- [Patterns & Techniques](notes/patterns.md)
- [Progress Tracker](progress/tracker.md)

---

## Tech Stack

- Language: Python 3.x
- Testing: pytest
- Focus: SDET preparation, clean code, complexity awareness
