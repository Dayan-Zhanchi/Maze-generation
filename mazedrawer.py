import pygame
from utils import draw_utils as du
import constants as c


class MazeDrawer:

    def __init__(self, maze_generation_algorithm):
        self.maze_generation_algorithms = maze_generation_algorithm

    def start_game_loop(self):
        pygame.init()
        screen = self.init_game_screen()
        pygame.display.update()
        running = True
        clock = pygame.time.Clock()
        while running:
            self.handle_button_event(clock, screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                running = self.handle_keydowns(clock, event, running, screen)
        pygame.quit()

    @staticmethod
    def init_game_screen():
        screen = du.create_canvas()
        # draw the foundation of the maze as a 2d grid
        du.draw_2d_grid(screen)
        # draw the buttons for the different maze generation algorithms
        du.draw_algo_button(screen, c.button_start_x, c.button_width, "Prims")
        du.draw_algo_button(screen, c.button_start_x + c.button_width + c.button_offset_x,
                            c.button_width, "RB")
        return screen

    def handle_button_event(self, clock, screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            if c.button_start_y <= mouse[1] <= c.button_start_y + c.button_height and \
                    c.button_start_x <= mouse[0] <= c.button_start_x + c.button_width:
                self.run_algorithm(screen, clock, 'Prims')
            elif c.button_start_x + c.button_width + c.button_offset_x <= mouse[0] <= c.button_start_x + c.button_width + c.button_offset_x + c.button_width and \
                    c.button_start_y <= mouse[1] <= c.button_start_y + c.button_height:
                self.run_algorithm(screen, clock, 'Recursive backtracking')

    def handle_keydowns(self, clock, event, running, screen):
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_p]:
                self.run_algorithm(screen, clock, 'Prims')
            elif pygame.key.get_pressed()[pygame.K_r]:
                self.run_algorithm(screen, clock, 'Recursive backtracking')
            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
        return running

    def run_algorithm(self, screen, clock, algorithm):
        # Reset maze to initial state before running algo
        du.draw_2d_grid(screen)
        self.maze_generation_algorithms[algorithm](screen, clock)
