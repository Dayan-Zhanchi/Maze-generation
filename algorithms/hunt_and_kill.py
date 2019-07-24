import pygame
import random
import cell as ce
import constants as c
import utils.draw_utils as du
from utils import algo_utils


def hunt_and_kill(screen, clock):
    grid = [[ce.Cell((i, j), algo_utils.get_neighbours(i, j, True)) for j in range(c.number_of_vertical_lines)]
            for i in range(c.number_of_horizontal_lines)]
    visited = [[0 for _ in range(c.number_of_vertical_lines)] for _ in range(c.number_of_horizontal_lines)]
    x, y = random.randint(0, c.number_of_horizontal_lines - 1), random.randint(0, c.number_of_vertical_lines - 1)
    current_cell = grid[x][y]
    while True:
        clock.tick(c.frames_hunt_and_kill)
        visited[current_cell.x][current_cell.y] = True
        unvisited_neighbours = algo_utils.get_unvisited_neighbours(current_cell.neighbours, visited)
        if unvisited_neighbours:
            x, y, direction = algo_utils.get_random_cell(unvisited_neighbours)
            du.remove_line(screen, current_cell.x, current_cell.y,
                           direction)  # remove line from the current cell and not from the unvisited neighbour
            current_cell = grid[x][y]
        else:
            hunt, (x, y) = hunt_scan(grid, visited)
            if hunt:
                du.remove_line(screen, x, y, algo_utils.get_random_adj_cell_direction(x, y, visited))
                current_cell = grid[x][y]
            else:
                break

def hunt_scan(grid, visited):
    cell = (0, 0)
    hunt = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not visited[i][j]:
                visited_neighbours = get_visited_neighbours(grid[i][j].neighbours, visited)
                if not visited_neighbours: continue
                cell = (i, j)
                hunt = True
                break
        if hunt: break
    return hunt, cell


def get_visited_neighbours(neighbours, visited):
    visited_neighbours = []
    for (x, y, _) in neighbours:
        if visited[x][y]:
            visited_neighbours.append((x, y))
    return visited_neighbours
