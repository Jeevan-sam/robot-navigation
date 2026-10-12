
from map import GridMap
from pathfinder import find_path, calculate_path_length
from robot import Robot
from visualize import show_path


def main():
    grid = GridMap(width=10, height=10)

    print("=== Robot Navigation System ===")

    print("Enter robot start position (0-9):")
    start_x = int(input("Start X: "))
    start_y = int(input("Start Y: "))

    print("Enter robot goal position (0-9):")
    goal_x = int(input("Goal X: "))
    goal_y = int(input("Goal Y: "))

    start = (start_x, start_y)
    goal = (goal_x, goal_y)

    if not grid.is_walkable(start):
        print("Invalid start position or start is an obstacle!")
        return

    if not grid.is_walkable(goal):
        print("Invalid goal position or goal is an obstacle!")
        return

    print("\nStart:", start)
    print("Goal:", goal)

    # Find the path BEFORE using it
    path = find_path(grid, start, goal)

    if path:
        robot = Robot(robot_id=1, start_position=start)
        robot.set_path(path)

        print("\nPath found!")
        print("Path:", path)
        print("Total steps:", calculate_path_length(path))

        print("\nRobot movement:")
        print(robot)

        while robot.move():
            print(robot)

        # Original path stays unchanged
        show_path(grid, path, start, goal)

    else:
        print("No valid path found.")


if __name__ == "__main__":
    main()
