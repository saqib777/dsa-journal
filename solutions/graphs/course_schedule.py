# Algorithm: Topological Sort — Cycle Detection via DFS (3-colour marking)
# Time Complexity:  O(V + E) — V = courses, E = prerequisites
# Space Complexity: O(V + E) — adjacency list + visited arrays

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """
    Determine if it is possible to finish all courses.

    prerequisites[i] = [a, b] means you must take b before a.

    This reduces to: does the directed graph contain a cycle?
    If a cycle exists, you can never satisfy all prerequisites.

    Approach: DFS with 3 states per node:
        0 = unvisited
        1 = visiting (currently in the DFS call stack)
        2 = visited  (fully processed — no cycle from here)

    If we reach a node marked 1 (visiting), we found a cycle.
    """
    graph   = [[] for _ in range(num_courses)]
    visited = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)

    def has_cycle(node: int) -> bool:
        if visited[node] == 1:   # back edge — cycle found
            return True
        if visited[node] == 2:   # already fully processed
            return False

        visited[node] = 1        # mark as visiting

        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True

        visited[node] = 2        # mark as fully processed
        return False

    for course in range(num_courses):
        if has_cycle(course):
            return False

    return True


def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """
    Variant: return the order to take courses, or [] if impossible.
    Uses the same DFS approach but appends to order on finish.
    """
    graph   = [[] for _ in range(num_courses)]
    visited = [0] * num_courses
    order   = []

    for course, prereq in prerequisites:
        graph[prereq].append(course)

    def dfs(node: int) -> bool:
        if visited[node] == 1: return True   # cycle
        if visited[node] == 2: return False
        visited[node] = 1
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        visited[node] = 2
        order.append(node)
        return False

    for course in range(num_courses):
        if dfs(course):
            return []

    return order[::-1]


if __name__ == "__main__":
    print(can_finish(2, [[1, 0]]))               # True  → take 0 then 1
    print(can_finish(2, [[1, 0], [0, 1]]))       # False → cycle
    print(find_order(4, [[1,0],[2,0],[3,1],[3,2]]))  # [0,1,2,3] or similar
