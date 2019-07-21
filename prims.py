import utils
import pygame
import random
import numpy as np
import constants as c


def prims(screen, clock, grid):
    visited = [[0 for _ in range(c.number_of_vertical_lines)] for _ in range(c.number_of_horizontal_lines)]
    x, y = random.randint(0, c.number_of_horizontal_lines - 1), random.randint(0, c.number_of_vertical_lines - 1)
    current_cell = grid[x][y]
    upcoming_cells = []
    add_upcoming_cells(current_cell, upcoming_cells, visited)
    visited[current_cell.x][current_cell.y] = True
    maze = [[0 for _ in range(c.number_of_vertical_lines)] for _ in range(c.number_of_horizontal_lines)]
    maze[current_cell.x][current_cell.y] = current_cell

    while not (np.asarray(visited) == 1).all():
        clock.tick(c.frames_prim)

        x, y = utils.get_random_cell(upcoming_cells)
        current_cell = grid[x][y]
        if visited[current_cell.x][current_cell.y]: continue
        visited[current_cell.x][current_cell.y] = True

        direction = get_random_adj_cell_direction(current_cell.x, current_cell.y, maze)
        utils.remove_line(screen, current_cell.x, current_cell.y, direction)
        upcoming_cells.remove((current_cell.x, current_cell.y))
        pygame.display.update()

        add_upcoming_cells(current_cell, upcoming_cells, visited)  # there may be dead ends, hopefully that will be okay
        maze[current_cell.x][current_cell.y] = current_cell


def add_upcoming_cells(current_cell, upcoming_cells, visited):
    neighbours = utils.get_unvisited_neighbours(current_cell.neighbours, visited)
    for n in neighbours:
        x, y = n
        if not visited[x][y]: upcoming_cells.append(n)


def get_random_adj_cell_direction(x, y, maze):
    unvisited_adj_cells = utils.get_neighbours(x, y, True)
    adj_cell_direction = []
    for (x, y, direction) in unvisited_adj_cells:
        if maze[x][y] != 0:
            adj_cell_direction.append(direction)
    return adj_cell_direction[random.randint(0, len(adj_cell_direction) - 1)]
