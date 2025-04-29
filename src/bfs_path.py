from collections import deque

def bfs_shortest_path(graph, start_node, end_node):
    visited = set()
    queue = deque([(start_node, [start_node])])

    while queue:
        current_node, path = queue.popleft()

        if current_node == end_node:
            return path

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  
# No path found
