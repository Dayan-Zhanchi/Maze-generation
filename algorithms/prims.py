import random

import constants as c
import utils.draw_utils
from components.maze import Maze
from utils.alg_util import get_unvisited_neighbours, get_random_cell, get_random_adj_cell_direction

""" 
    Since there are no weights in the cells the modification of Prims is that we only randomly select the upcoming cells.
    The removal of lines is done by randomly selecting the direction of an adjacent cell to the current cell
"""

maze = Maze()


def prims(screen, clock):
    global maze

    x, y = random.randint(0, c.number_of_horizontal_lines - 1), random.randint(0, c.number_of_vertical_lines - 1)
    current_cell = maze.grid[x][y]
    upcoming_cells = []
    add_upcoming_cells(current_cell, upcoming_cells, maze.visited)
    maze.visited[current_cell.x][current_cell.y] = True
    working_maze = [[0 for _ in range(c.number_of_vertical_lines)] for _ in range(c.number_of_horizontal_lines)]
    working_maze[current_cell.x][current_cell.y] = current_cell

    while upcoming_cells:
        clock.tick(c.frames_prim)

        x, y = get_random_cell(upcoming_cells)
        current_cell = maze.grid[x][y]
        if maze.visited[current_cell.x][current_cell.y]: continue
        maze.visited[current_cell.x][current_cell.y] = True

        direction = get_random_adj_cell_direction(current_cell, working_maze)
        utils.draw_utils.remove_line(screen, current_cell.x, current_cell.y, direction)
        upcoming_cells.remove((current_cell.x, current_cell.y))

        add_upcoming_cells(current_cell, upcoming_cells, maze.visited)
        working_maze[current_cell.x][current_cell.y] = current_cell


# Add unvisited adjacent cells
def add_upcoming_cells(current_cell, upcoming_cells, visited):
    neighbours = get_unvisited_neighbours(current_cell, visited)
    for n in neighbours:
        x, y, _ = n
        if not visited[x][y] and (x, y) not in upcoming_cells:
            upcoming_cells.append((x, y))
