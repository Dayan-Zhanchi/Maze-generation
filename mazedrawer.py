import pygame
import constants as c


class MazeDrawer:

    def __init__(self, maze_generation_algorithm):
        self.maze_generation_algorithms = maze_generation_algorithm

    # start generating a randomly constructed maze
    def start_game_loop(self):
        screen = self.init_game_screen()
        pygame.display.update()
        running = True
        clock = pygame.time.Clock()
        while running:
            self.handle_button_event(clock, screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_p]:
                        self.run_algorithm(screen, clock, 'Prims')
                    elif pygame.key.get_pressed()[pygame.K_r]:
                        self.run_algorithm(screen, clock, 'Recursive backtracking')
        pygame.quit()
        pygame.display.quit()

    def init_game_screen(self):
        pygame.init()
        screen = pygame.display.set_mode((c.canvas_width, c.canvas_height))
        screen.fill(c.WHITE)
        # draw the foundation of the maze as a 2d grid
        self.draw_2d_grid(screen)
        # draw the buttons for the different maze generation algorithms
        self.draw_algo_buttons(screen, c.button_start_x, c.button_width, "Prims")
        self.draw_algo_buttons(screen, c.button_start_x + c.button_width + c.button_offset_x,
                               c.button_width, "RB")
        return screen

    def draw_2d_grid(screen):
        pygame.draw.rect(screen, c.BLACK, (c.start_x, c.start_y, c.maze_width, c.maze_height), 1)
        # draw the vertical lines
        for i in range(1, c.number_of_vertical_lines):
            start_x_line = c.start_x + int(c.maze_width / c.number_of_vertical_lines) * i
            pygame.draw.line(screen, c.BLACK, (start_x_line, c.start_y), (start_x_line, c.start_y + c.maze_height))
        # draw the horizontal lines
        for i in range(1, c.number_of_horizontal_lines):
            start_y_line = c.start_y + int(c.maze_height / c.number_of_horizontal_lines) * i
            pygame.draw.line(screen, c.BLACK, (c.start_x, start_y_line), (c.start_x + c.maze_width, start_y_line))

    def draw_algo_buttons(screen, button_start_x, button_end_x, algo_name):
        # draw button for triggering prims algorithm
        pygame.draw.rect(screen, c.BLACK, (button_start_x, c.button_start_y,
                                           button_end_x, c.button_height), 1)
        small_text = pygame.font.Font("freesansbold.ttf", 17)
        text_surf, text_rect = MazeDrawer.text_objects(algo_name, small_text)
        text_rect.center = ((button_start_x + (c.button_width / 2)), (c.button_start_y + (c.button_height / 2)))
        screen.blit(text_surf, text_rect)

    def text_objects(text, font):
        text_surface = font.render(text, True, c.BLACK)
        return text_surface, text_surface.get_rect()

    def handle_button_event(self, clock, screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            if c.button_start_y <= mouse[1] <= c.button_start_y + c.button_height and \
                    c.button_start_x <= mouse[0] <= c.button_start_x + c.button_width:
                self.run_algorithm(screen, clock, 'Prims')
            elif c.button_start_x + c.button_width + c.button_offset_x <= mouse[0] <= c.button_start_x + c.button_width + c.button_offset_x + c.button_width and \
                    c.button_start_y <= mouse[1] <= c.button_start_y + c.button_height:
                # Reset maze to initial state
                self.run_algorithm(screen, clock, 'Recursive backtracking')

    def run_algorithm(self, screen, clock, algorithm):
        # Reset maze to initial state before running algo
        self.draw_2d_grid(screen)
        self.maze_generation_algorithms[algorithm](screen, clock)
