
class GridMap:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height

        self.obstacles = {
            (3, 2), (3, 3), (3, 4),
            (5, 5), (6, 5), (7, 5),
            (7, 6), (7, 7)
        }

    def is_valid(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def is_walkable(self, position):
        return (
            self.is_valid(position)
            and position not in self.obstacles
        )

    def get_neighbors(self, position):
        x, y = position

        possible_moves = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]

        return [
            point for point in possible_moves
            if self.is_walkable(point)
        ]
