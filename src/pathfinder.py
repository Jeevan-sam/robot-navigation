from collections import deque


def find_path(grid, start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        x, y = path[-1]

        if (x, y) == goal:
            return path

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (
                0 <= ny < len(grid)
                and 0 <= nx < len(grid[0])
                and grid[ny][nx] == 0
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                queue.append(path + [(nx, ny)])

    return None


def calculate_path_length(path):
    if path is None:
        return 0

    return len(path) - 1