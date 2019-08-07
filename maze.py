import random
import cell as ce
import constants as c
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

    def set_grid(self, grid):
        self.grid = grid

    def set_visited(self, visited):
        self.visited = visited

    @staticmethod
    def get_random_cell(cells):
        if len(cells) > 1:
            return cells[random.randint(0, len(cells) - 1)]
        return cells[0]

    # Get the direction of a randomly selected visited adjacent cell
    # x and y coord is for an unvisited cell
    @staticmethod
    def get_random_adj_cell_direction(cell, visited):
        adj_cells = get_neighbours(cell.x, cell.y)
        adj_cell_direction = []
        for (x, y, direction) in adj_cells:
            if visited[x][y] != 0:
                adj_cell_direction.append(direction)
        return adj_cell_direction[random.randint(0, len(adj_cell_direction) - 1)]

    # append current cell and next cell to the neighbours of each other
    def add_cell_to_walkable_path(self, current_cell, next_cell):
        if (next_cell.x, next_cell.y) not in self.path[current_cell.x][current_cell.y].neighbours:
            self.path[current_cell.x][current_cell.y].neighbours.append((next_cell.x, next_cell.y))
        if (current_cell.x, current_cell.y) not in self.path[next_cell.x][next_cell.y].neighbours:
            self.path[next_cell.x][next_cell.y].neighbours.append((current_cell.x, current_cell.y))
