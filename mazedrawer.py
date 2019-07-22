import pygame
import button as b
import constants as c
from utils import draw_utils as du


class MazeDrawer:

    def __init__(self, maze_generation_algorithm):
        self.maze_generation_algorithms = maze_generation_algorithm

    def start_game_loop(self):
        pygame.init()
        screen, algo_buttons = self.init_game_screen()
        pygame.display.update()
        running = True
        clock = pygame.time.Clock()
        while running:
            self.handle_button_event(clock, screen, algo_buttons)
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
        algo_buttons = MazeDrawer.initialize_algo_buttons(screen)
        return screen, algo_buttons

    @staticmethod
    def initialize_algo_buttons(screen):
        algo_buttons = []
        algo_buttons.append(b.Button(screen, c.button_start_x, c.button_width,
                                     c.button_start_y, c.button_height,
                                     c.button_offset_x, c.button_offset_y, "Prims"))
        algo_buttons.append(b.Button(screen, c.button_start_x + c.button_width + c.button_offset_x,
                                     c.button_width, c.button_start_y, c.button_height,
                                     c.button_offset_x, c.button_offset_y, 'RB'))
        algo_buttons.append(b.Button(screen, c.button_start_x + c.button_width * 2 + c.button_offset_x * 2,
                                     c.button_width, c.button_start_y, c.button_height,
                                     c.button_offset_x, c.button_offset_y, 'HAK'))
        algo_buttons.append(b.Button(screen, c.button_start_x, c.button_width,
                                     c.button_start_y + c.button_height + c.button_offset_y, c.button_height,
                                     c.button_offset_x, c.button_offset_y, "Kruskal"))
        algo_buttons.append(b.Button(screen, c.button_start_x + c.button_width + c.button_offset_x,
                                     c.button_width, c.button_start_y + c.button_height + c.button_offset_y, c.button_height,
                                     c.button_offset_x, c.button_offset_y, 'BT'))
        algo_buttons.append(b.Button(screen, c.button_start_x + c.button_width * 2 + c.button_offset_x * 2,
                                     c.button_width, c.button_start_y + c.button_height + c.button_offset_y, c.button_height,
                                     c.button_offset_x, c.button_offset_y, 'RD'))
        return algo_buttons

    def handle_button_event(self, clock, screen, algo_buttons):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            for button in algo_buttons:
                if button.is_pressed(mouse):
                    self.run_algorithm(screen, clock, button.button_name)

    def handle_keydowns(self, clock, event, running, screen):
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_p]:
                self.run_algorithm(screen, clock, 'Prims')
            elif pygame.key.get_pressed()[pygame.K_r]:
                self.run_algorithm(screen, clock, 'RB')
            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
        return running

    def run_algorithm(self, screen, clock, algorithm):
        # Reset maze to initial state before running algo
        du.draw_2d_grid(screen)
        self.maze_generation_algorithms[algorithm](screen, clock)
