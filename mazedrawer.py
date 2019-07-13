import pygame
import constants as c


class MazeDrawer:

    def __init__(self, maze_generation_algorithm):
        self.__maze_generation_algorithm = maze_generation_algorithm

    # start generating a randomly constructed maze
    def start_game_loop(self, grid):
        screen = self.__init_game_screen()
        pygame.display.update()
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_s]:
                        # generate maze
                        self.__draw_2d_grid(screen)
                        self.__maze_generation_algorithm(screen, clock, grid[:])

        pygame.quit()
        pygame.display.quit()

    def __init_game_screen(self):
        pygame.init()
        screen = pygame.display.set_mode((c.height, c.width))
        screen.fill(c.WHITE)
        # draw the foundation of the maze as a 2d grid
        self.__draw_2d_grid(screen)
        return screen

    @staticmethod
    def __draw_2d_grid(screen):
        pygame.draw.rect(screen, c.BLACK, (c.start_x, c.start_y, c.maze_width, c.maze_height), 1)
        # draw the vertical lines
        for i in range(1, c.number_of_vertical_lines):
            start_x_line = c.start_x + int(c.maze_width / c.number_of_vertical_lines) * i
            pygame.draw.line(screen, c.BLACK, (start_x_line, c.start_y), (start_x_line, c.start_y + c.maze_height))
        # draw the horizontal lines
        for i in range(1, c.number_of_horizontal_lines):
            start_y_line = c.start_y + int(c.maze_height / c.number_of_horizontal_lines) * i
            pygame.draw.line(screen, c.BLACK, (c.start_x, start_y_line), (c.start_x + c.maze_width, start_y_line))
