
from collections import deque


def find_path(grid_map, start, goal):
    if not grid_map.is_walkable(start):
        return None

    if not grid_map.is_walkable(goal):
        return None

    queue = deque([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for neighbor in grid_map.get_neighbors(current):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    return None


def calculate_path_length(path):
    if not path:
        return 0

    return len(path) - 1
