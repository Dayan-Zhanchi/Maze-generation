import random

import constants as c
import utils.draw_utils
from components.maze import Maze
from utils.alg_util import get_unvisited_neighbours, get_random_cell, add_cell_to_walkable_path


def recursive_backtracking(screen, clock):
    maze = Maze()
    x, y = random.randint(0, c.number_of_horizontal_lines - 1), random.randint(0, c.number_of_vertical_lines - 1)
    current_cell = maze.grid[x][y]
    stack = [current_cell]
    while stack:
        clock.tick(c.frames_rb)
        neighbours = get_unvisited_neighbours(current_cell, maze.visited)
        maze.visited[current_cell.x][current_cell.y] = True

        if neighbours:
            next_cell_x, next_cell_y, direction = get_random_cell(neighbours)
            next_cell = maze.grid[next_cell_x][next_cell_y]
            stack.append(next_cell)
            utils.draw_utils.remove_line(screen, current_cell.x, current_cell.y, direction)
            add_cell_to_walkable_path(current_cell, next_cell, maze.path)
            current_cell = next_cell
        elif stack:
            # reached a dead end so we backtrack, the stack keeps track of previous cells
            current_cell = stack.pop()

    return maze.path
