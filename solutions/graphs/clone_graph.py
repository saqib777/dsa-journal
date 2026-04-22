# Algorithm: BFS with Hash Map (Original → Clone mapping)
# Time Complexity:  O(V + E) — visit every node and edge once
# Space Complexity: O(V)     — hash map stores all cloned nodes

from collections import deque


class Node:
    def __init__(self, val: int, neighbors: list = None):
        self.val       = val
        self.neighbors = neighbors if neighbors else []


def clone_graph(node: Node) -> Node:
    """
    Return a deep copy of an undirected connected graph.
    Each node contains a value and a list of neighbours.

    Approach: BFS. Use a hash map { original: clone } to
    track visited nodes and avoid infinite loops in cycles.
    When we visit a node, create its clone immediately.
    When we process its neighbours, create their clones
    (if not already done) and wire them up.
    """
    if not node:
        return None

    cloned  = {node: Node(node.val)}
    queue   = deque([node])

    while queue:
        current = queue.popleft()
        for neighbor in current.neighbors:
            if neighbor not in cloned:
                cloned[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            cloned[current].neighbors.append(cloned[neighbor])

    return cloned[node]


def build_graph(adj: list[list[int]]) -> Node:
    """Helper: build graph from adjacency list. Nodes are 1-indexed."""
    if not adj:
        return None
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, neighbors in enumerate(adj):
        nodes[i].neighbors = [nodes[n - 1] for n in neighbors]
    return nodes[0]


def graph_to_adj(node: Node) -> list[list[int]]:
    """Helper: convert cloned graph back to adjacency list for testing."""
    if not node:
        return []
    visited = {}
    queue   = deque([node])
    while queue:
        curr = queue.popleft()
        if curr.val in visited:
            continue
        visited[curr.val] = sorted([n.val for n in curr.neighbors])
        for n in curr.neighbors:
            if n.val not in visited:
                queue.append(n)
    return [visited[i] for i in sorted(visited)]


if __name__ == "__main__":
    original = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
    clone    = clone_graph(original)
    print(graph_to_adj(clone))   # [[2,4],[1,3],[2,4],[1,3]]
    print(original is not clone) # True — deep copy confirmed
