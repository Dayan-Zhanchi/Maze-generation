import cell as ce
import constants as c
from utils.algo_utils import get_neighbours

def initialize_common_data():
    grid = [[ce.Cell((i, j), get_neighbours(i, j)) for j in range(c.number_of_vertical_lines)]
            for i in range(c.number_of_horizontal_lines)]
    visited = [[0 for _ in range(c.number_of_vertical_lines)] for _ in range(c.number_of_horizontal_lines)]
    return grid, visited