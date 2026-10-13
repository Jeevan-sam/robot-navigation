
import matplotlib.pyplot as plt


def show_path(grid_map, robots):
    fig, ax = plt.subplots(figsize=(8, 8))

    # Draw obstacles
    for x, y in grid_map.obstacles:
        ax.add_patch(
            plt.Rectangle(
                (x - 0.5, y - 0.5),
                1, 1,
                color="black"
            )
        )

    colors = ["blue", "red", "green", "purple"]

    for index, robot in enumerate(robots):
        if not robot.path:
            continue

        color = colors[index % len(colors)]
        path_x = [point[0] for point in robot.path]
        path_y = [point[1] for point in robot.path]

        ax.plot(
            path_x, path_y,
            marker="o",
            color=color,
            label=f"Robot {robot.robot_id}"
        )

        ax.scatter(
            *robot.start,
            marker="s",
            color=color,
            s=100
        )

        ax.scatter(
            *robot.goal,
            marker="*",
            color=color,
            s=200
        )

    ax.set_xlim(-0.5, grid_map.width - 0.5)
    ax.set_ylim(-0.5, grid_map.height - 0.5)
    ax.set_xticks(range(grid_map.width))
    ax.set_yticks(range(grid_map.height))
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.set_title("Multi-Robot Warehouse Planner")
    ax.grid(True)
    ax.legend()
    ax.set_aspect("equal")
    plt.tight_layout()
    plt.show()
