import pygame, sys
import recursive_backtracking as rec_b
import constants as c


class MazeDrawer:

    def __init__(self):

        pygame.init()
        screen = pygame.display.set_mode((c.height, c.width))
        screen.fill(c.WHITE)

        # draw the foundation of the maze as a 2d grid
        self.draw_2d_grid(screen)

        maze_grid = [[Cell((i, j), self.get_neighbours(i, j)) for j in range(c.number_of_vertical_lines)] for i in range(c.number_of_horizontal_lines)]
        visited = [[0 for _ in range(c.number_of_vertical_lines)] for _ in range(c.number_of_horizontal_lines)]

        pygame.display.update()
        finished = False
        running = True
        clock = pygame.time.Clock()
        maze_generator = rec_b.Rec_backtrack(screen, clock, maze_grid, visited)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_s]:
                        if not finished:
                            # generate the maze
                            finished = maze_generator.recursive_backtracking()
        pygame.quit()
        pygame.display.quit()
        sys.exit()

    def draw_2d_grid(self, screen):
        pygame.draw.rect(screen, c.BLACK, (c.start_x, c.start_y, c.maze_width, c.maze_height), 1)
        # draw the vertical lines
        for i in range(1, c.number_of_vertical_lines):
            start_x_line = c.start_x + int(c.maze_width / c.number_of_vertical_lines) * i
            pygame.draw.line(screen, c.BLACK, (start_x_line, c.start_y), (start_x_line, c.start_y + c.maze_height))
        # draw the horizontal lines
        for i in range(1, c.number_of_horizontal_lines):
            start_y_line = c.start_y + int(c.maze_height / c.number_of_horizontal_lines) * i
            pygame.draw.line(screen, c.BLACK, (c.start_x, start_y_line), (c.start_x + c.maze_width, start_y_line))

    @staticmethod
    def get_neighbours(x, y):
        neighbours = []
        north_cell = y - 1
        east_cell = x + 1
        south_cell = y + 1
        west_cell = x - 1

        if north_cell >= 0:
            neighbours.append((x, north_cell, 'N'))
        if east_cell < c.number_of_vertical_lines:
            neighbours.append((east_cell, y, 'E'))
        if south_cell < c.number_of_horizontal_lines:
            neighbours.append((x, south_cell, 'S'))
        if west_cell >= 0:
            neighbours.append((west_cell, y, 'W'))

        return neighbours


class Cell:
    def __init__(self, position, neighbours):
        self.visited = False
        self.x, self.y = position
        self.neighbours = neighbours


maze = MazeDrawer()
