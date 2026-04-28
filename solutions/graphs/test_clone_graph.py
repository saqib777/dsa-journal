import pytest
from clone_graph import clone_graph, build_graph, graph_to_adj, Node


def test_basic_four_nodes():
    original = build_graph([[2,4],[1,3],[2,4],[1,3]])
    clone    = clone_graph(original)
    assert graph_to_adj(clone) == graph_to_adj(original)

def test_deep_copy_not_same_object():
    original = build_graph([[2,4],[1,3],[2,4],[1,3]])
    clone    = clone_graph(original)
    assert clone is not original

def test_single_node_no_neighbors():
    node  = Node(1)
    clone = clone_graph(node)
    assert clone.val == 1
    assert clone.neighbors == []
    assert clone is not node

def test_single_node_self_loop():
    node            = Node(1)
    node.neighbors  = [node]
    clone           = clone_graph(node)
    assert clone.val == 1
    assert clone.neighbors[0] is clone      # self-loop preserved
    assert clone.neighbors[0] is not node   # but not the original

def test_none_input():
    assert clone_graph(None) is None

def test_two_nodes_connected():
    original = build_graph([[2],[1]])
    clone    = clone_graph(original)
    assert graph_to_adj(clone) == [[2],[1]]

def test_linear_graph():
    original = build_graph([[2],[1,3],[2]])
    clone    = clone_graph(original)
    assert graph_to_adj(clone) == graph_to_adj(original)

def test_all_nodes_are_new_objects():
    original = build_graph([[2,3],[1,3],[1,2]])
    clone    = clone_graph(original)
    # BFS collect all original nodes
    from collections import deque
    visited_orig  = set()
    visited_clone = set()
    q = deque([(original, clone)])
    while q:
        o, c = q.popleft()
        if id(o) in visited_orig:
            continue
        visited_orig.add(id(o))
        visited_clone.add(id(c))
        assert o is not c
        for on, cn in zip(o.neighbors, c.neighbors):
            q.append((on, cn))
