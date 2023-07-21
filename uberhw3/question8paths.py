from collections import deque

def shortest_alternating_path(edges, origin, destination):
    graph = {}
    for u, v, color in edges:
        if u not in graph:
            graph[u] = {}
        graph[u][v] = color

    queue = deque([(origin, "", 0)])  # (node, last_color, distance)
    visited = set()

    while queue:
        node, last_color, distance = queue.popleft()

        if node == destination:
            return distance

        if (node, last_color) in visited:
            continue

        visited.add((node, last_color))

        for neighbor, color in graph.get(node, {}).items():
            if color != last_color:
                queue.append((neighbor, color, distance + 1))
