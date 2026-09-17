class Map:
    def __init__(self):
        self.grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]

    def display(self):
        for row in self.grid:
            print(row)