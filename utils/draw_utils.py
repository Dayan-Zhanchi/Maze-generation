import pygame
import constants as c


def create_canvas():
    screen = pygame.display.set_mode((c.canvas_width, c.canvas_height))
    screen.fill(c.WHITE)
    return screen


def draw_2d_grid(screen):
    dimen_params_for_grid = (c.start_x, c.start_y, c.maze_width, c.maze_height)
    pygame.draw.rect(screen, c.WHITE, dimen_params_for_grid)
    pygame.draw.rect(screen, c.BLACK, dimen_params_for_grid, 1)
    # draw the vertical lines
    for i in range(1, c.number_of_vertical_lines):
        start_x_line = c.start_x + int(c.maze_width / c.number_of_vertical_lines) * i
        pygame.draw.line(screen, c.BLACK, (start_x_line, c.start_y), (start_x_line, c.start_y + c.maze_height))
    # draw the horizontal lines
    for i in range(1, c.number_of_horizontal_lines):
        start_y_line = c.start_y + int(c.maze_height / c.number_of_horizontal_lines) * i
        pygame.draw.line(screen, c.BLACK, (c.start_x, start_y_line), (c.start_x + c.maze_width, start_y_line))


def draw_algo_button(screen, start_x, button_width, start_y, button_height, algo_name):
    pygame.draw.rect(screen, c.BLACK, (start_x, start_y,
                                       button_width, button_height), 1)
    small_text = pygame.font.Font("freesansbold.ttf", 17)
    text_surf, text_rect = text_objects(algo_name, small_text)
    text_rect.center = ((start_x + (button_width / 2)), (start_y + (button_height / 2)))
    screen.blit(text_surf, text_rect)


def text_objects(text, font):
    text_surface = font.render(text, True, c.BLACK)
    return text_surface, text_surface.get_rect()


def remove_line(screen, x, y, direction):
    start_x_line = c.start_x + c.grid_size_x * x  # start x position of the current cell
    start_y_line = c.start_y + c.grid_size_y * y  # start y position of the current cell

    if direction == 'N':
        pygame.draw.line(screen, c.WHITE, (start_x_line + c.offset, start_y_line),
                         (start_x_line + c.grid_size_x - c.offset, start_y_line))
    elif direction == 'E':
        pygame.draw.line(screen, c.WHITE, (start_x_line + c.grid_size_x, start_y_line + c.offset),
                         (start_x_line + c.grid_size_x, start_y_line + c.grid_size_y - c.offset))
    elif direction == 'S':
        pygame.draw.line(screen, c.WHITE, (start_x_line + c.offset, start_y_line + c.grid_size_y),
                         (start_x_line + c.grid_size_x - c.offset, start_y_line + c.grid_size_y))
    else:
        pygame.draw.line(screen, c.WHITE, (start_x_line, start_y_line + c.offset),
                         (start_x_line, start_y_line + c.grid_size_y - c.offset))

    pygame.display.update()


def color_cell(screen, color, x, y):
    start_x_line = c.start_x + c.grid_size_x * x  # start x position of the current cell
    start_y_line = c.start_y + c.grid_size_y * y  # start y position of the current cell
    circle_x = start_x_line + (int(c.grid_size_x / 2))  # middle of the cell x
    circle_j = start_y_line + (int(c.grid_size_y / 2))  # middle of the cell y
    pygame.draw.circle(screen, color, (circle_x, circle_j), int((c.grid_size_x + c.grid_size_y) / 8))
    pygame.display.update()
