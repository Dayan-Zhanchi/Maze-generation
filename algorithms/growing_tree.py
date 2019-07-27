import random
import cell as ce
import constants as c
import utils.draw_utils as du
from algorithms.common_data import initialize_common_data
from utils import algo_utils



def growing_tree(screen, clock):
    grid, visited = initialize_common_data()
    generating_approach = ['Prims', 'RB']
    x, y = random.randint(0, c.number_of_horizontal_lines - 1), random.randint(0, c.number_of_vertical_lines - 1)
    cells = [grid[x][y]]
    visited[x][y] = True
    while cells:
        clock.tick(c.frames_growing_tree)
        # randomly select an approach, either Prims or recursive backtracking
        approach = random.randint(0, len(generating_approach) - 1)
        if approach == 'RB':
            current_cell = cells[-1]
        else:
            current_cell = algo_utils.get_random_cell(cells)

        unvisited_neighbours = algo_utils.get_unvisited_neighbours(current_cell.neighbours, visited)
        if not unvisited_neighbours:
            if approach == 'RB':
                cells.pop()
            else:
                cells.remove(current_cell)
            continue
        x, y, direction = algo_utils.get_random_cell(unvisited_neighbours)
        visited[x][y] = True
        du.remove_line(screen, current_cell.x, current_cell.y, direction)
        cells.append(grid[x][y])
