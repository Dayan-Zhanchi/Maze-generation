import pygame
import random
import constants as c


class Rec_backtrack():

    def __init__(self, screen, clock, grid, visited):
        self.screen = screen
        self.clock = clock
        self.grid = grid
        self.visited = visited

    def recursive_backtracking(self):
        current_cell = self.grid[0][0]
        stack = []
        stack.append(current_cell)
        while stack:
            self.clock.tick(150)
            current_cell_x, current_cell_y = current_cell.x, current_cell.y
            neighbours = self.get_unvisited_neighbour(current_cell.neighbours)
            self.visited[current_cell_x][current_cell_y] = True

            if neighbours:
                next_cell_x, next_cell_y, direction = self.get_random_neighbour(neighbours)
                next_cell = self.grid[next_cell_x][next_cell_y]
                stack.append(next_cell)
                # removing line of a grid to make the maze
                self.remove_line(current_cell_x, current_cell_y, direction)
                current_cell = next_cell
                pygame.display.update()
            elif stack:
                current_cell = stack.pop()

        return True

    def get_unvisited_neighbour(self, neighbours):
        unvisited_neighbours = []
        for neighbour in neighbours:
            x, y = neighbour[0], neighbour[1]
            if not self.visited[x][y]:
                unvisited_neighbours.append(neighbour)
        return unvisited_neighbours

    def get_random_neighbour(self, unvisited_neighbours):
        if len(unvisited_neighbours) > 1:
            return unvisited_neighbours[random.randint(0, len(unvisited_neighbours) - 1)]
        return unvisited_neighbours[0]

    def remove_line(self, current_cell_x, current_cell_y, direction):
        # offset is needed to avoid creating white pixels around the very beginning and end of an erased line
        offset = 1
        grid_size_x = int(c.maze_width / c.number_of_vertical_lines)
        grid_size_y = int(c.maze_height / c.number_of_horizontal_lines)
        start_x_line = c.start_x + grid_size_x * current_cell_x
        start_y_line = c.start_y + grid_size_y * current_cell_y

        if direction == 'N':
            pygame.draw.line(self.screen, c.WHITE, (start_x_line + offset, start_y_line), (start_x_line + grid_size_x - offset, start_y_line))
        elif direction == 'E':
            pygame.draw.line(self.screen, c.WHITE, (start_x_line + grid_size_x, start_y_line + offset), (start_x_line + grid_size_x, start_y_line + grid_size_y - offset))
        elif direction == 'S':
            pygame.draw.line(self.screen, c.WHITE, (start_x_line + offset, start_y_line + grid_size_y), (start_x_line + grid_size_x - offset, start_y_line + grid_size_y))
        else:
            pygame.draw.line(self.screen, c.WHITE, (start_x_line, start_y_line + offset), (start_x_line, start_y_line + grid_size_y - offset))
