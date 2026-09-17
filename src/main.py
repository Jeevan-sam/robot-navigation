from robot import Robot
from map import Map
from pathfinder import find_path,calculate_path_length
from visualize import show_path

my_map = Map()

print("=== Robot Navigation ===")

try:
    start_x = int(input("Enter start X (0-4): "))
    start_y = int(input("Enter start Y (0-4): "))
    goal_x = int(input("Enter goal X (0-4): "))
    goal_y = int(input("Enter goal Y (0-4): "))

    start = (start_x, start_y)
    goal = (goal_x, goal_y)

    rows = len(my_map.grid)
    cols = len(my_map.grid[0])

    if not (0 <= start_x < cols and 0 <= start_y < rows):
        print("Invalid start position!")
    elif not (0 <= goal_x < cols and 0 <= goal_y < rows):
        print("Invalid goal position!")
    elif my_map.grid[start_y][start_x] == 1:
        print("Start position is an obstacle!")
    elif my_map.grid[goal_y][goal_x] == 1:
        print("Goal position is an obstacle!")
    else:
        path = find_path(my_map.grid, start, goal)

        if path:
            print("\nPath found!")
            print("Path:", path)
            print("Total steps:", calculate_path_length(path))

            robot = Robot()
            robot.follow_path(path)

            show_path(my_map.grid, path)
        else:
            print("\nNo path available!")

except ValueError:
    print("Please enter numbers only!")