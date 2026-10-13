
from map import GridMap
from pathfinder import find_path, calculate_path_length
from robot import Robot
from visualize import show_path


def reserve_path(path, reservations, max_time=60):
    if not path:
        return

    for t in range(max_time + 1):
        position = path[min(t, len(path) - 1)]
        reservations["cells"].setdefault(t, set()).add(position)

    for t in range(1, len(path)):
        previous = path[t - 1]
        current = path[t]

        reservations["edges"].setdefault(t, set()).add(
            (current, previous)
        )


def main():
    warehouse = GridMap()

    robots = [
        Robot(1, (0, 0), (9, 0)),
        Robot(2, (0, 9), (9, 9)),
        Robot(3, (9, 2), (0, 2))
    ]

    reservations = {
        "cells": {},
        "edges": {}
    }

    print("=== Multi-Robot Warehouse Planner ===")
    print("Warehouse size: 10 x 10")
    print("Obstacles:", sorted(warehouse.obstacles))

    for robot in robots:
        path = find_path(
            warehouse,
            robot.start,
            robot.goal,
            reservations
        )

        robot.set_path(path)

        if not path:
            print(f"\nRobot {robot.robot_id}: No safe path found.")
            continue

        reserve_path(path, reservations)

        print(f"\nRobot {robot.robot_id}")
        print("Start:", robot.start)
        print("Goal:", robot.goal)
        print("Path:", robot.path)
        print("Total steps:", calculate_path_length(robot.path))

    successful_robots = [
        robot for robot in robots if robot.path
    ]

    print("\n=== Planning Summary ===")
    print(
        f"Successfully planned: "
        f"{len(successful_robots)}/{len(robots)} robots"
    )

    if successful_robots:
        show_path(warehouse, successful_robots)


if __name__ == "__main__":
    main()
