
class Robot:
    def __init__(self, robot_id, start, goal):
        self.robot_id = robot_id
        self.start = start
        self.goal = goal
        self.position = start
        self.path = []
        self.steps = 0

    def set_path(self, path):
        self.path = path if path else []
        self.steps = max(0, len(self.path) - 1)

    def move_to(self, position):
        self.position = position

    def __str__(self):
        return (
            f"Robot {self.robot_id}: "
            f"Position={self.position}, Goal={self.goal}"
        )
