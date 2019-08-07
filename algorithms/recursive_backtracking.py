import random
import cell as ce
import constants as c
import utils.draw_utils
from utils import algo_utils
from utils.algo_utils import initialize_common_data


def recursive_backtracking(screen, clock):
    grid, visited = initialize_common_data()
    x, y = random.randint(0, c.number_of_horizontal_lines - 1), random.randint(0, c.number_of_vertical_lines - 1)
    current_cell = grid[x][y]
    stack = [current_cell]
    walkable_path = [[ce.Cell((i, j), []) for j in range(c.number_of_vertical_lines)]
                     for i in range(c.number_of_horizontal_lines)]
    while stack:
        clock.tick(c.frames_rb)
        neighbours = algo_utils.get_unvisited_neighbours(current_cell.neighbours, visited)
        visited[current_cell.x][current_cell.y] = True

        if neighbours:
            next_cell_x, next_cell_y, direction = algo_utils.get_random_cell(neighbours)
            next_cell = grid[next_cell_x][next_cell_y]
            stack.append(next_cell)
            # removing line of a grid to make the maze
            utils.draw_utils.remove_line(screen, current_cell.x, current_cell.y, direction)
            add_cell_to_walkable_path(current_cell, next_cell_x, next_cell_y, walkable_path)
            current_cell = next_cell
        elif stack:
            # reached a dead end so we backtrack, the stack keeps track of previous cells
            current_cell = stack.pop()

    return walkable_path


# append current cell and next cell to the neighbours of each other
def add_cell_to_walkable_path(current_cell, next_cell_x, next_cell_y, walkable_path):
    if (next_cell_x, next_cell_y) not in walkable_path[current_cell.x][current_cell.y].neighbours:
        walkable_path[current_cell.x][current_cell.y].neighbours.append((next_cell_x, next_cell_y))
    if (current_cell.x, current_cell.y) not in walkable_path[next_cell_x][next_cell_y].neighbours:
        walkable_path[next_cell_x][next_cell_y].neighbours.append((current_cell.x, current_cell.y))
