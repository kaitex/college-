from collections import deque

def water_jug_bfs(capA, capB, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print((x, y))

        if x == target or y == target:
            print("Goal reached!")
            return

        # All possible operations
        states = [
            (capA, y),        # Fill jug A
            (x, capB),        # Fill jug B
            (0, y),           # Empty jug A
            (x, 0),           # Empty jug B
            (x - min(x, capB - y), y + min(x, capB - y)),  # A → B
            (x + min(y, capA - x), y - min(y, capA - x))   # B → A
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    print("Goal not possible")

water_jug_bfs(4, 3, 2)
