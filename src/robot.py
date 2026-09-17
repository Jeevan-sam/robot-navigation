import time
class Robot:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == "up":
            self.y += 1
        elif direction == "down":
            self.y -= 1
        elif direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1

        print(f"Robot position: ({self.x}, {self.y})")
            
    def follow_path(self, path):
        for position in path:
            self.x, self.y = position
            print(f"Robot moved to: ({self.x}, {self.y})")
            time.sleep(0.5)