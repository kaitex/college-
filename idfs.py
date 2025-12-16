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

def dls(node, goal, limit, path):
    path.append(node)

    if node == goal:
        return True

    if limit <= 0:
        path.pop()
        return False

    for neighbour in Graph.get(node, []):
        if dls(neighbour, goal, limit - 1, path):
            return True

    path.pop()
    return False



def iddfs(start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = []
        if dls(start, goal, depth, visited):
            return visited

    return None


# Function call
result = iddfs('A', 'H', 5)

if result:
    print("IDDFS Traversal:", result)
else:
    print("Goal not found")
