# Data Structures Reference

A concise reference covering internal workings, complexities,
and Python implementations of every core data structure.

---

## 1. Array / List

**Internal:** Contiguous block of memory. Random access via index.

| Operation | Complexity |
|-----------|------------|
| Access    | O(1)       |
| Search    | O(n)       |
| Insert end| O(1) amort.|
| Insert mid| O(n)       |
| Delete end| O(1)       |
| Delete mid| O(n)       |

```python
arr = [1, 2, 3, 4, 5]
arr.append(6)        # O(1)
arr.insert(2, 99)    # O(n) — shifts elements
arr.pop()            # O(1)
arr.pop(0)           # O(n) — use deque for O(1) popleft
```

**When to use:** random access by index, fixed-size collections,
cache-friendly iteration.

---

## 2. Linked List

**Internal:** Nodes with value + pointer to next node.
No contiguous memory — elements scattered in heap.

| Operation    | Singly | Doubly |
|--------------|--------|--------|
| Access by idx| O(n)   | O(n)   |
| Insert head  | O(1)   | O(1)   |
| Insert tail  | O(n)*  | O(1)** |
| Delete head  | O(1)   | O(1)   |
| Search       | O(n)   | O(n)   |

*O(1) if tail pointer maintained. **With tail pointer.

```python
class Node:
    def __init__(self, val):
        self.val  = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, val):
        node      = Node(val)
        node.next = self.head
        self.head = node

    def to_list(self):
        result, cur = [], self.head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result
```

**When to use:** frequent insertions/deletions at head,
implementing stacks and queues, when size is dynamic.

---

## 3. Stack

**Internal:** LIFO — Last In First Out. Backed by a list in Python.

| Operation | Complexity |
|-----------|------------|
| Push      | O(1)       |
| Pop       | O(1)       |
| Peek      | O(1)       |
| Search    | O(n)       |

```python
stack = []
stack.append(1)    # push
stack.append(2)
top = stack[-1]    # peek — O(1)
val = stack.pop()  # pop  — O(1)
```

**When to use:** DFS, bracket matching, expression evaluation,
undo operations, monotonic stack problems.

---

## 4. Queue

**Internal:** FIFO — First In First Out.
Use `deque` — list.pop(0) is O(n), deque.popleft() is O(1).

| Operation | Complexity |
|-----------|------------|
| Enqueue   | O(1)       |
| Dequeue   | O(1)       |
| Peek      | O(1)       |

```python
from collections import deque
q = deque()
q.append(1)       # enqueue
q.append(2)
front = q[0]      # peek
val   = q.popleft()  # dequeue O(1)
```

**When to use:** BFS, task scheduling, sliding window,
producer-consumer problems.

---

## 5. Hash Map (Dictionary)

**Internal:** Hash table — hash function maps key to bucket.
Collisions handled by chaining or open addressing.

| Operation | Average | Worst |
|-----------|---------|-------|
| Insert    | O(1)    | O(n)  |
| Delete    | O(1)    | O(n)  |
| Search    | O(1)    | O(n)  |

```python
freq = {}
freq['a'] = freq.get('a', 0) + 1

# defaultdict avoids KeyError
from collections import defaultdict
graph = defaultdict(list)
graph['A'].append('B')

# Counter for frequency
from collections import Counter
count = Counter([1, 2, 2, 3, 3, 3])  # {3:3, 2:2, 1:1}
```

**When to use:** frequency counting, caching, two-sum complement
lookup, grouping, graph adjacency lists.

---

## 6. Hash Set

**Internal:** Hash table storing only keys (no values).

| Operation | Average |
|-----------|---------|
| Add       | O(1)    |
| Remove    | O(1)    |
| Contains  | O(1)    |

```python
seen = set()
seen.add(1)
1 in seen        # O(1)
seen.discard(1)  # no error if missing
seen.remove(1)   # raises KeyError if missing

# Set operations
a = {1,2,3}; b = {2,3,4}
a & b   # intersection {2,3}
a | b   # union {1,2,3,4}
a - b   # difference {1}
```

**When to use:** duplicate detection, visited tracking in BFS/DFS,
membership testing.

---

## 7. Binary Heap (Priority Queue)

**Internal:** Complete binary tree stored as array.
Min-heap: parent ≤ children. Max-heap: parent ≥ children.

| Operation    | Complexity |
|--------------|------------|
| Insert       | O(log n)   |
| Extract min  | O(log n)   |
| Peek min     | O(1)       |
| Build heap   | O(n)       |

```python
import heapq

# Min-heap
heap = [3, 1, 4, 1, 5]
heapq.heapify(heap)           # O(n)
heapq.heappush(heap, 2)       # O(log n)
min_val = heapq.heappop(heap) # O(log n)

# Max-heap — negate values
max_heap = [-x for x in [3,1,4,1,5]]
heapq.heapify(max_heap)
max_val = -heapq.heappop(max_heap)
```

**When to use:** Dijkstra, Prim's MST, K largest/smallest,
merge K sorted lists, median of stream.

---

## 8. Binary Search Tree (BST)

**Internal:** Binary tree where left < node < right at every node.

| Operation | Average  | Worst (skewed) |
|-----------|----------|----------------|
| Search    | O(log n) | O(n)           |
| Insert    | O(log n) | O(n)           |
| Delete    | O(log n) | O(n)           |

```python
class BST:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

    def insert(self, val):
        if val < self.val:
            if self.left:  self.left.insert(val)
            else:          self.left = BST(val)
        else:
            if self.right: self.right.insert(val)
            else:          self.right = BST(val)
```

**When to use:** sorted data with frequent insertions/deletions,
range queries, in-order gives sorted sequence.

---

## 9. Trie (Prefix Tree)

**Internal:** Tree where each node represents one character.
Root → all words with that prefix share the same path.

| Operation      | Complexity |
|----------------|------------|
| Insert word    | O(m)       |
| Search word    | O(m)       |
| Prefix search  | O(m)       |

m = length of the word.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end   = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
```

**When to use:** autocomplete, spell checking, IP routing,
word search in a grid, prefix matching.

---

## 10. Graph Representations

```python
# Adjacency List — sparse graphs (most common)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B'],
}

# Adjacency Matrix — dense graphs or when O(1) edge lookup needed
n = 4
matrix = [[0]*n for _ in range(n)]
matrix[0][1] = 1   # edge from 0 to 1

# Edge List — simple, used in Kruskal's MST
edges = [(0,1,4),(0,2,3),(1,3,2)]  # (u, v, weight)
```

**Complexity comparison:**

| Representation  | Space    | Add Edge | Edge Query |
|-----------------|----------|----------|------------|
| Adjacency List  | O(V+E)   | O(1)     | O(degree)  |
| Adjacency Matrix| O(V^2)   | O(1)     | O(1)       |
| Edge List       | O(E)     | O(1)     | O(E)       |
