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

def dls(node, goal, limit, visited):
    visited.append(node)

    if node == goal:
        return True

    if limit == 0:
        return False

    for neighbour in Graph.get(node, []):
        if neighbour not in visited:
            if dls(neighbour, goal, limit - 1, visited):
                return True

    return False


# Function call
visited = []
found = dls('A', 'H', 3, visited)

if found:
    print("DLS Traversal:", visited)
else:
    print("Goal not found within depth limit")
