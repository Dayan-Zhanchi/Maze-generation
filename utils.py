import random
import pygame
import constants as c


def get_random_cell(unvisited_neighbours):
    if len(unvisited_neighbours) > 1:
        return unvisited_neighbours[random.randint(0, len(unvisited_neighbours) - 1)]
    return unvisited_neighbours[0]


def get_unvisited_neighbours(neighbours, visited):
    unvisited_neighbours = []
    for neighbour in neighbours:
        x, y = neighbour[0], neighbour[1]
        if not visited[x][y]:
            unvisited_neighbours.append(neighbour)
    return unvisited_neighbours


def get_neighbours(x, y, direction):
    neighbours = []
    north_cell = y - 1
    east_cell = x + 1
    south_cell = y + 1
    west_cell = x - 1

    if north_cell >= 0:
        if direction:
            neighbours.append((x, north_cell, 'N'))
        else:
            neighbours.append((x, north_cell))
    if east_cell < c.number_of_vertical_lines:
        if direction:
            neighbours.append((east_cell, y, 'E'))
        else:
            neighbours.append((east_cell, y))
    if south_cell < c.number_of_horizontal_lines:
        if direction:
            neighbours.append((x, south_cell, 'S'))
        else:
            neighbours.append((x, south_cell))
    if west_cell >= 0:
        if direction:
            neighbours.append((west_cell, y, 'W'))
        else:
            neighbours.append((west_cell, y))

    return neighbours


def remove_line(screen, current_cell_x, current_cell_y, direction):
    offset = 1  # offset is needed to avoid creating white pixels around the very beginning and end of an erased line
    grid_size_x = int(c.maze_width / c.number_of_vertical_lines)
    grid_size_y = int(c.maze_height / c.number_of_horizontal_lines)
    start_x_line = c.start_x + grid_size_x * current_cell_x  # start x position of the current cell
    start_y_line = c.start_y + grid_size_y * current_cell_y  # start y position of the current cell

    if direction == 'N':
        pygame.draw.line(screen, c.WHITE, (start_x_line + offset, start_y_line),
                         (start_x_line + grid_size_x - offset, start_y_line))
    elif direction == 'E':
        pygame.draw.line(screen, c.WHITE, (start_x_line + grid_size_x, start_y_line + offset),
                         (start_x_line + grid_size_x, start_y_line + grid_size_y - offset))
    elif direction == 'S':
        pygame.draw.line(screen, c.WHITE, (start_x_line + offset, start_y_line + grid_size_y),
                         (start_x_line + grid_size_x - offset, start_y_line + grid_size_y))
    else:
        pygame.draw.line(screen, c.WHITE, (start_x_line, start_y_line + offset),
                         (start_x_line, start_y_line + grid_size_y - offset))
