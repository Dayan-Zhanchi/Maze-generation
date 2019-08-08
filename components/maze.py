import constants as c
from components import cell as ce
from utils.alg_util import get_neighbours


class Maze:
    def __init__(self):
        self.grid, self.visited, self.path = self.__initialize_data()

    @staticmethod
    def __initialize_data():
        grid = [[ce.Cell((i, j), get_neighbours(i, j)) for j in range(c.number_of_vertical_lines)]
                for i in range(c.number_of_horizontal_lines)]

        visited = [[0 for _ in range(c.number_of_vertical_lines)] for _ in range(c.number_of_horizontal_lines)]

        path = [[ce.Cell((i, j), []) for j in range(c.number_of_vertical_lines)]
                for i in range(c.number_of_horizontal_lines)]

        return grid, visited, path
