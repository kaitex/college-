# Graph representation
Graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'I'],
    'D': ['G'],
    'E': ['H', 'J'],
    'F': ['K'],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}

def dfs(start, goal):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)

            if node == goal:
                break

            # reverse to maintain left-to-right order
            for neighbour in reversed(Graph.get(node, [])):
                stack.append(neighbour)

    return visited

# Function call
print("DFS Traversal:", dfs('A', 'H'))
