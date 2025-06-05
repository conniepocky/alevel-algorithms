graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []}

visited = []

def dfs(node):
    for child in graph[node]:
        if child not in visited:
            dfs(child)

    visited.append(node) 

dfs("A")
print(visited)