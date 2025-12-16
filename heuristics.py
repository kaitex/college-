from heapq import heappush, heappop

# Heuristic values (straight-line estimates to goal J)
H = {
    'A': 11, 'B': 6, 'C': 5, 'D': 7,
    'E': 3, 'F': 6, 'G': 5, 'H': 3,
    'I': 1, 'J': 0
}

# Graph: node -> (neighbor, cost)
Graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('J', 3)]
}

# ------------------------------
# Greedy Best-First Search (GBFS)
# ------------------------------
def gbfs(start, goal):
    pq, visited = [(H[start], start, [start])], set()
    while pq:
        _, node, path = heappop(pq)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neigh, _ in Graph.get(node, []):
            heappush(pq, (H[neigh], neigh, path + [neigh]))
    return None

# ------------------------------
# A* Search
# ------------------------------
def astar(start, goal):
    pq = [(H[start], 0, start, [start])]
    g = {start: 0}
    visited = set()
    while pq:
        f, cost, node, path = heappop(pq)
        if node == goal:
            return path, cost
        if node in visited:
            continue
        visited.add(node)
        for neigh, w in Graph.get(node, []):
            new_g = cost + w
            if neigh not in g or new_g < g[neigh]:
                g[neigh] = new_g
                heappush(pq, (new_g + H[neigh], new_g, neigh, path + [neigh]))
    return None

# ------------------------------
# Run the algorithms
# ------------------------------
print("Greedy Best-First Search Path:", gbfs("A", "J"))
path, cost = astar("A", "J")
print("A* Path:", path, "with total cost =", cost)

