import sys

# Increase recursion limit
sys.setrecursionlimit(10000)

# Example graph and DFS function as before
def dfs_all_paths(graph, start, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    path = path + [start]
    visited.add(start)

    if start not in graph or not graph[start]:
        return [path]

    paths = []
    for node in graph[start]:
        if node not in visited:  # Check if node has not been visited in the current path
            new_paths = dfs_all_paths(graph, node, path, visited)
            for p in new_paths:
                paths.append(p)
    
    visited.remove(start)  # Remove node from visited to allow other paths to use it
    return paths

# Example graph
graph = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['C', 'A', 'E'],
    'E': ['A', 'D']
}

# Find all possible paths starting from node 'A'
all_paths = dfs_all_paths(graph, 'A')

# Print all paths
for path in all_paths:
    print('Path:', path)
