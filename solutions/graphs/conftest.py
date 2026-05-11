# Shared fixtures for graph test files

import pytest
from collections import deque


def build_grid(rows: list[str]) -> list[list[str]]:
    """Convert list of strings to 2D char grid."""
    return [list(r) for r in rows]


def bfs_levels(graph: dict, start) -> dict:
    """Return dict of {node: level} for BFS from start."""
    levels  = {start: 0}
    queue   = deque([start])
    while queue:
        node = queue.popleft()
        for neighbour in graph.get(node, []):
            if neighbour not in levels:
                levels[neighbour] = levels[node] + 1
                queue.append(neighbour)
    return levels


@pytest.fixture
def simple_graph():
    return {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2],
    }


@pytest.fixture
def cyclic_directed():
    return {0: [1], 1: [2], 2: [0]}


@pytest.fixture
def acyclic_directed():
    return {0: [1, 2], 1: [3], 2: [3], 3: []}


@pytest.fixture
def weighted_graph():
    return {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [],
    }


@pytest.fixture
def small_grid():
    return build_grid(['110', '110', '001'])


@pytest.fixture
def empty_grid():
    return []
