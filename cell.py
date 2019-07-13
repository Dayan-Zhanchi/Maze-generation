class Cell:
    def __init__(self, position, neighbours):
        self.visited = False
        self.x, self.y = position
        self.neighbours = neighbours
