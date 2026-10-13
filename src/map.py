class GridMap:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.obstacles = {
            (1,1), (1,2), (1,3), (1,6), (1,7), (1,8),
            (2,3), (2,6), (2,8),
            (3,1), (3,2), (3,5), (3,6), (3,8),
            (4,2), (4,5), (4,8),
            (5,1), (5,3), (5,4), (5,7), (5,8),
            (6,1), (6,4), (6,7),
            (7,1), (7,2), (7,4), (7,8),
            (8,2), (8,5), (8,6), (8,8),
            (0,4), (0,7), (2,1), (2,5),
            (4,1), (4,7), (6,2), (6,8),
            (9,4), (9,6)
        }

    def is_valid(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def is_walkable(self, position):
        return self.is_valid(position) and position not in self.obstacles

    def get_neighbors(self, position):
        x, y = position
        moves = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        return [p for p in moves if self.is_walkable(p)]
