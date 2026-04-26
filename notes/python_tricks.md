# Python Tricks for DSA

Patterns and built-ins that appear constantly in problem solving.
Knowing these saves time and reduces code length significantly.

---

## Collections Module

```python
from collections import defaultdict, Counter, deque

# defaultdict — no KeyError on missing keys
freq = defaultdict(int)
freq['a'] += 1   # works even if 'a' not present

graph = defaultdict(list)
graph['A'].append('B')

# Counter — instant frequency map
from collections import Counter
count = Counter("aabbccc")  # Counter({'c':3,'a':2,'b':2})
count.most_common(2)        # [('c',3),('a',2)]

# deque — O(1) append and popleft (use for BFS, sliding window)
from collections import deque
q = deque([1, 2, 3])
q.appendleft(0)   # [0,1,2,3]
q.popleft()       # 0 in O(1) — list.pop(0) is O(n)
```

---

## heapq — Min Heap

```python
import heapq

nums = [3, 1, 4, 1, 5, 9]
heapq.heapify(nums)          # in-place, O(n)
heapq.heappush(nums, 2)      # O(log n)
smallest = heapq.heappop(nums)  # O(log n)

# Max heap — negate values
max_heap = [-n for n in [3,1,4,1,5]]
heapq.heapify(max_heap)
largest = -heapq.heappop(max_heap)

# K largest elements
k_largest = heapq.nlargest(3, [3,1,4,1,5,9,2,6])  # [9,6,5]

# K smallest elements
k_smallest = heapq.nsmallest(3, [3,1,4,1,5,9])    # [1,1,3]
```

---

## bisect — Binary Search on Sorted Lists

```python
import bisect

arr = [1, 3, 5, 7, 9]
bisect.bisect_left(arr, 5)    # 2 — index where 5 would go (left)
bisect.bisect_right(arr, 5)   # 3 — index where 5 would go (right)
bisect.insort(arr, 6)         # inserts 6 in sorted position O(n)

# Count elements less than target
def count_less_than(arr, target):
    return bisect.bisect_left(arr, target)
```

---

## String Operations

```python
# Reverse a string
s = "hello"
rev = s[::-1]              # "olleh"

# Check palindrome
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Sort characters
sorted_str = ''.join(sorted("banana"))  # "aaabnn"

# Split and join
words  = "the quick brown fox".split()          # ['the','quick','brown','fox']
joined = " ".join(words)                        # "the quick brown fox"

# String to list of chars and back
chars = list("hello")      # ['h','e','l','l','o']
back  = ''.join(chars)     # "hello"
```

---

## List Comprehensions and Generators

```python
# Flatten 2D list
matrix = [[1,2],[3,4],[5,6]]
flat   = [n for row in matrix for n in row]  # [1,2,3,4,5,6]

# Filter and transform
evens_squared = [x**2 for x in range(10) if x % 2 == 0]

# 2D grid creation
grid = [[0]*cols for _ in range(rows)]  # CORRECT
# grid = [[0]*cols]*rows  — WRONG: all rows share the same list

# Generator — memory efficient for large sequences
gen = (x**2 for x in range(1_000_000))
```

---

## Useful Built-ins

```python
# enumerate — index + value together
for i, val in enumerate(['a','b','c']):
    print(i, val)   # 0 a, 1 b, 2 c

# zip — iterate multiple lists in parallel
for a, b in zip([1,2,3], ['x','y','z']):
    print(a, b)

# sorted with custom key
intervals = [[3,6],[1,5],[2,4]]
intervals.sort(key=lambda x: x[1])   # sort by end time

# min/max with key
words = ['banana','apple','cherry']
shortest = min(words, key=len)        # 'apple'

# any/all
any(x > 5 for x in [1,2,6])   # True
all(x > 0 for x in [1,2,3])   # True

# divmod — quotient and remainder together
q, r = divmod(17, 5)   # q=3, r=2

# infinity
INF = float('inf')
NEG_INF = float('-inf')
```

---

## Common DSA Patterns in Python

```python
# Two pointers
left, right = 0, len(arr) - 1
while left < right:
    left += 1; right -= 1

# Sliding window skeleton
left = 0
for right in range(len(s)):
    # expand window
    while window_invalid:
        left += 1  # shrink
    best = max(best, right - left + 1)

# DFS on grid (4 directions)
directions = [(0,1),(0,-1),(1,0),(-1,0)]
def dfs(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols: return
    for dr, dc in directions:
        dfs(r+dr, c+dc)

# Memoisation decorator
from functools import lru_cache
@lru_cache(maxsize=None)
def dp(i, j):
    # your recurrence here
    pass
```

---

## Interview Quick Reference

| Task | Pythonic way |
|---|---|
| Frequency map | `Counter(arr)` |
| Default dict | `defaultdict(list)` |
| Min of k largest | `heapq` size k |
| Binary search | `bisect.bisect_left` |
| BFS queue | `deque` with `popleft()` |
| Memoisation | `@lru_cache(maxsize=None)` |
| Sort by key | `sorted(arr, key=lambda x: x[1])` |
| Infinity | `float('inf')` |
| Swap | `a, b = b, a` |
| Reverse | `arr[::-1]` |
