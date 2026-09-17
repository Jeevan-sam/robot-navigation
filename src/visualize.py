import matplotlib.pyplot as plt


def show_path(grid, path):
    plt.figure(figsize=(6, 6))

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1:
                plt.fill_between(
                    [x, x + 1],
                    y,
                    y + 1
                )

    if path:
        x_values = [p[0] + 0.5 for p in path]
        y_values = [p[1] + 0.5 for p in path]

        plt.plot(x_values, y_values, marker="o")

    plt.xlim(0, len(grid[0]))
    plt.ylim(0, len(grid))
    plt.gca().invert_yaxis()
    plt.grid(True)

    plt.title("Robot Navigation Path")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.show()