
import matplotlib.pyplot as plt


def show_path(grid_map, path, start, goal):
    fig, ax = plt.subplots(figsize=(8, 8))

    ax.set_xlim(-0.5, grid_map.width - 0.5)
    ax.set_ylim(-0.5, grid_map.height - 0.5)

    ax.set_xticks(range(grid_map.width))
    ax.set_yticks(range(grid_map.height))
    ax.grid(True, color="lightgray")

    # Draw obstacles
    for x, y in grid_map.obstacles:
        ax.scatter(x, y, color="black", marker="s", s=300)

    # Draw complete planned path
    path_x = [point[0] for point in path]
    path_y = [point[1] for point in path]

    ax.plot(
        path_x,
        path_y,
        color="blue",
        linewidth=3,
        marker="o",
        markersize=5,
        label="Planned Path",
        zorder=2
    )

    # Start and goal
    ax.scatter(
        *start, color="green", s=180,
        label="Start", zorder=4
    )

    ax.scatter(
        *goal, color="purple", marker="*",
        s=300, label="Goal", zorder=5
    )

    # Robot marker
    robot_dot, = ax.plot(
        [], [],
        marker="o",
        color="orange",
        markersize=12,
        label="Robot",
        zorder=7
    )

    # Travelled route
    travel_line, = ax.plot(
        [], [],
        color="red",
        linewidth=3,
        label="Travelled Route",
        zorder=6
    )

    ax.set_title("Robot Navigation")
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.set_aspect("equal")
    ax.invert_yaxis()
    ax.legend()
    plt.tight_layout()

    travelled_x = []
    travelled_y = []

    for step, (x, y) in enumerate(path):
        travelled_x.append(x)
        travelled_y.append(y)

        robot_dot.set_data([x], [y])
        travel_line.set_data(travelled_x, travelled_y)

        ax.set_title(
            f"Robot Navigation - Step {step}/{len(path) - 1}"
        )

        plt.pause(0.5)

    plt.show()


if __name__ == "__main__":
    print("Run this file using: python src/main.py")
