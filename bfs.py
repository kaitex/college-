# TITLE: Implementation of Blind Search Algorithm
# Theory:
# Blind BFS goes through the tree level by level, visiting all of the
# nodes on the top level first and all node on second level & so on.

# Source Code:
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
} # Note: The handwritten graph structure is slightly ambiguous 
  # on the children of C, D, E, but I transcribed it as best as possible.

def bfs(start, goal):
    visited = []
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        
        if node not in visited:
            visited.append(node)
            
            if node == goal:
                break
                
            queue.extend(Graph.get(node, [])) # queue += Graph[node]
            
    return visited
print(bfs('A', 'H'))
