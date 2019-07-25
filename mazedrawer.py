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
        # TODO: Perhaps create a class that wraps the relevant parameters for the button
        #  creation, may be less messy and shorten the code
        button_1_start_x = c.button_start_x
        button_2_start_x = button_1_start_x + c.button_width + c.button_offset_x
        button_3_start_x = button_1_start_x + c.button_width * 2 + c.button_offset_x * 2
        second_row_buttons_start_y = c.button_start_y + c.button_height + c.button_offset_y

        algo_buttons.append(b.Button(screen, button_1_start_x, c.button_width,
                                     c.button_start_y, c.button_height, c.text_prim))
        algo_buttons.append(b.Button(screen, button_2_start_x, c.button_width,
                                     c.button_start_y, c.button_height, c.text_rb))
        algo_buttons.append(b.Button(screen, button_3_start_x, c.button_width,
                                     c.button_start_y, c.button_height, c.text_hunt_and_kill))
        algo_buttons.append(b.Button(screen, button_1_start_x, c.button_width,
                                     second_row_buttons_start_y, c.button_height, c.text_kurskal))
        algo_buttons.append(b.Button(screen, button_2_start_x, c.button_width,
                                     second_row_buttons_start_y, c.button_height, c.text_binary_tree))
        algo_buttons.append(b.Button(screen, button_3_start_x, c.button_width,
                                     second_row_buttons_start_y, c.button_height, c.text_growing_tree))
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
            elif pygame.key.get_pressed()[pygame.K_h]:
                self.run_algorithm(screen, clock, 'HAK')
            elif pygame.key.get_pressed()[pygame.K_b]:
                self.run_algorithm(screen, clock, 'BT')
            elif pygame.key.get_pressed()[pygame.K_g]:
                self.run_algorithm(screen, clock, 'GT')
            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
        return running

    def run_algorithm(self, screen, clock, algorithm):
        # Reset maze to initial state before running algo
        du.draw_2d_grid(screen)
        self.maze_generation_algorithms[algorithm](screen, clock)
