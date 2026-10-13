
from collections import deque


def find_path(grid_map, start, goal, reservations=None, max_time=60):
    if reservations is None:
        reservations = {"cells": {}, "edges": {}}

    if not grid_map.is_walkable(start):
        return None

    if not grid_map.is_walkable(goal):
        return None

    if start == goal:
        return [start]

    queue = deque([(start, 0)])
    parent = {(start, 0): None}

    moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]

    final_state = None

    while queue:
        position, time = queue.popleft()

        if position == goal:
            final_state = (position, time)
            break

        if time >= max_time:
            continue

        x, y = position
        next_time = time + 1

        for dx, dy in moves:
            next_position = (x + dx, y + dy)

            if not grid_map.is_walkable(next_position):
                continue

            if next_position in reservations["cells"].get(next_time, set()):
                continue

            edge = (position, next_position)

            if edge in reservations["edges"].get(next_time, set()):
                continue

            state = (next_position, next_time)

            if state in parent:
                continue

            parent[state] = (position, time)
            queue.append(state)

    if final_state is None:
        return None

    path = []
    state = final_state

    while state is not None:
        path.append(state[0])
        state = parent[state]

    return path[::-1]


def calculate_path_length(path):
    if not path:
        return 0

    return len(path) - 1
