# DFS.py

def depth_first_search(graph, start):
    """Perform a depth-first search on a graph."""
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))  # Add neighbors in reverse order for correct DFS

    return visited

# Example usage:
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }
# print(depth_first_search(graph, 'A'))