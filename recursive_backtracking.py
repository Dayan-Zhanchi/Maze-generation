import pygame
import random
import constants as c


def recursive_backtracking(screen, clock, grid):
    visited = [[0 for _ in range(c.number_of_vertical_lines)] for _ in range(c.number_of_horizontal_lines)]
    current_cell = grid[0][0]
    stack = [current_cell]
    while stack:
        clock.tick(150)
        neighbours = get_unvisited_neighbour(current_cell.neighbours, visited)
        visited[current_cell.x][current_cell.y] = True

        if neighbours:
            next_cell_x, next_cell_y, direction = get_random_neighbour(neighbours)
            next_cell = grid[next_cell_x][next_cell_y]
            stack.append(next_cell)
            # removing line of a grid to make the maze
            remove_line(screen, current_cell.x, current_cell.y, direction)
            current_cell = next_cell
            pygame.display.update()
        elif stack:
            current_cell = stack.pop()

    return True


def get_random_neighbour(unvisited_neighbours):
    if len(unvisited_neighbours) > 1:
        return unvisited_neighbours[random.randint(0, len(unvisited_neighbours) - 1)]
    return unvisited_neighbours[0]


def get_unvisited_neighbour(neighbours, visited):
    unvisited_neighbours = []
    for neighbour in neighbours:
        x, y = neighbour[0], neighbour[1]
        if not visited[x][y]:
            unvisited_neighbours.append(neighbour)
    return unvisited_neighbours


def remove_line(screen, current_cell_x, current_cell_y, direction):
    offset = 1  # offset is needed to avoid creating white pixels around the very beginning and end of an erased line
    grid_size_x = int(c.maze_width / c.number_of_vertical_lines)
    grid_size_y = int(c.maze_height / c.number_of_horizontal_lines)
    start_x_line = c.start_x + grid_size_x * current_cell_x  # start x position of the current cell
    start_y_line = c.start_y + grid_size_y * current_cell_y  # start y position of the current cell

    if direction == 'N':
        pygame.draw.line(screen, c.WHITE, (start_x_line + offset, start_y_line), (start_x_line + grid_size_x - offset, start_y_line))
    elif direction == 'E':
        pygame.draw.line(screen, c.WHITE, (start_x_line + grid_size_x, start_y_line + offset), (start_x_line + grid_size_x, start_y_line + grid_size_y - offset))
    elif direction == 'S':
        pygame.draw.line(screen, c.WHITE, (start_x_line + offset, start_y_line + grid_size_y), (start_x_line + grid_size_x - offset, start_y_line + grid_size_y))
    else:
        pygame.draw.line(screen, c.WHITE, (start_x_line, start_y_line + offset), (start_x_line, start_y_line + grid_size_y - offset))
