import random
import constants as c
import utils.draw_utils as du
from maze import Maze
from utils.alg_util import get_unvisited_neighbours


def hunt_and_kill(screen, clock):
    maze = Maze()
    x, y = random.randint(0, c.number_of_horizontal_lines - 1), random.randint(0, c.number_of_vertical_lines - 1)
    current_cell = maze.grid[x][y]
    while True:
        clock.tick(c.frames_hunt_and_kill)
        maze.visited[current_cell.x][current_cell.y] = True
        unvisited_neighbours = get_unvisited_neighbours(current_cell, maze.visited)
        if unvisited_neighbours:
            x, y, direction = maze.get_random_cell(unvisited_neighbours)
            du.remove_line(screen, current_cell.x, current_cell.y, direction)  # remove line from the current cell and not from the unvisited neighbour
            current_cell = maze.grid[x][y]
        else:
            hunt, (x, y) = hunt_scan(maze.grid, maze.visited)
            if hunt:
                cell = maze.grid[x][y]
                du.remove_line(screen, cell.x, cell.y, maze.get_random_adj_cell_direction(cell, maze.visited))
                current_cell = cell
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
