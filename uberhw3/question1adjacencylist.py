from collections import defaultdict, deque

def adjacency_set(edges):
    graph = defaultdict(set)

    for src, dest in edges:
        graph[src].add(dest)
        graph[dest].add(src)  # Undirected edge, add both directions

    return graph

def bfs(target, graph):
    visited = set()
    queue = deque()

    queue.append(target)
    visited.add(target)

    while queue:
        current = queue.popleft()

        if current == target:
            return True

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return False

def dfs(target, graph):
    visited = set()
    return dfs_helper(target, graph, visited)

def dfs_helper(current, graph, visited):
    if current == target:
        return True

    visited.add(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            if dfs_helper(neighbor, graph, visited):
                return True

    return False

def topological_sort(graph):
    result = []
    in_degree = {node: 0 for node in graph}

    for src, neighbors in graph.items():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    queue = deque(node for node in graph if in_degree[node] == 0)

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result

# Test
edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
graph = adjacency_set(edges)
print(graph)

target_node = 3
print("BFS:", bfs(target_node, graph))
print("DFS:", dfs(target_node, graph))
print("Topological Sort:", topological_sort(graph))