import pygame

import constants as c
from components import button as b
from setup_maze_algos import create_mappings_for_generation_algos, create_mappings_for_pathfinder_algos
from utils import draw_utils as du


class Game:

    def __init__(self):
        self.maze = []
        self.algo_buttons = []
        self.screen = du.create_canvas()
        self.clock = pygame.time.Clock()
        self.pathfinder_algorithm = create_mappings_for_pathfinder_algos()
        self.maze_generation_algorithms = create_mappings_for_generation_algos()

    def start_game_loop(self):
        pygame.init()
        self.init_game_screen()
        pygame.display.update()
        running = True
        while running:
            self.handle_button_event()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                running = self.handle_keydowns(event, running)
        pygame.quit()

    def init_game_screen(self):
        # draw the foundation of the maze as a 2d grid
        du.draw_2d_grid(self.screen)
        # draw the buttons for the different maze generation algorithms
        self.initialize_algo_buttons()

    def initialize_algo_buttons(self):
        # TODO: Perhaps create a class that wraps the relevant parameters for the button
        #  creation, may be less messy and shorten the code
        button_1_start_x = c.button_start_x
        button_2_start_x = button_1_start_x + c.button_width + c.button_offset_x
        button_3_start_x = button_1_start_x + c.button_width * 2 + c.button_offset_x * 2
        second_row_buttons_start_y = c.button_start_y + c.button_height + c.button_offset_y

        self.algo_buttons.append(b.Button(self.screen, button_1_start_x, c.button_width,
                                          c.button_start_y, c.button_height, c.text_prim))
        self.algo_buttons.append(b.Button(self.screen, button_2_start_x, c.button_width,
                                          c.button_start_y, c.button_height, c.text_rb))
        self.algo_buttons.append(b.Button(self.screen, button_3_start_x, c.button_width,
                                          c.button_start_y, c.button_height, c.text_hunt_and_kill))
        self.algo_buttons.append(b.Button(self.screen, button_1_start_x, c.button_width,
                                          second_row_buttons_start_y, c.button_height, c.text_kurskal))
        self.algo_buttons.append(b.Button(self.screen, button_2_start_x, c.button_width,
                                          second_row_buttons_start_y, c.button_height, c.text_binary_tree))
        self.algo_buttons.append(b.Button(self.screen, button_3_start_x, c.button_width,
                                          second_row_buttons_start_y, c.button_height, c.text_growing_tree))

    def handle_button_event(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            for button in self.algo_buttons:
                if button.is_pressed(mouse):
                    self.run_algorithm(button.button_name)

    def handle_keydowns(self, event, running):
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_p]:
                self.run_algorithm('Prims')
            elif pygame.key.get_pressed()[pygame.K_r]:
                self.run_algorithm('RB')
            elif pygame.key.get_pressed()[pygame.K_h]:
                self.run_algorithm('HAK')
            elif pygame.key.get_pressed()[pygame.K_k]:
                self.run_algorithm('Kruskal')
            elif pygame.key.get_pressed()[pygame.K_b]:
                self.run_algorithm('BT')
            elif pygame.key.get_pressed()[pygame.K_g]:
                self.run_algorithm('GT')
            elif pygame.key.get_pressed()[pygame.K_s]:
                self.run_pathfinder(self.maze)
            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
        return running

    def run_algorithm(self, algorithm):
        # reset maze to initial state before running algo
        du.draw_2d_grid(self.screen)
        self.maze = self.maze_generation_algorithms[algorithm](self.screen, self.clock)
        du.draw_entrance_and_exit(self.screen)

    def run_pathfinder(self, maze):
        # reset cells to initial state before running pathfinder
        du.reset_all_cells(self.screen)
        self.pathfinder_algorithm(self.screen, self.clock, maze)
