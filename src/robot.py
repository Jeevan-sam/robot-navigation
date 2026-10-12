\
class Robot:
    def __init__(self, robot_id, start_position):
        self.robot_id = robot_id
        self.position = start_position
        self.path = []
        self.steps_taken = 0

    def set_path(self, path):
        self.path = path.copy()

    def move(self):
        if len(self.path) > 1:
            self.path.pop(0)
            self.position = self.path[0]
            self.steps_taken += 1
            return True

        return False

    def __str__(self):
        return (
            f"Robot {self.robot_id} | "
            f"Position: {self.position} | "
            f"Steps: {self.steps_taken}"
        )
