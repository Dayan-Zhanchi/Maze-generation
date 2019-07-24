import pygame
import constants as c


def create_canvas():
    screen = pygame.display.set_mode((c.canvas_width, c.canvas_height))
    screen.fill(c.WHITE)
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


def draw_algo_button(screen, start_x, end_x, start_y, end_y, algo_name):
    pygame.draw.rect(screen, c.BLACK, (start_x, start_y,
                                       end_x, end_y), 1)
    small_text = pygame.font.Font("freesansbold.ttf", 17)
    text_surf, text_rect = text_objects(algo_name, small_text)
    text_rect.center = ((start_x + (end_x / 2)), (start_y + (end_y / 2)))
    screen.blit(text_surf, text_rect)


def text_objects(text, font):
    text_surface = font.render(text, True, c.BLACK)
    return text_surface, text_surface.get_rect()


def remove_line(screen, current_cell_x, current_cell_y, direction):
    offset = 1  # offset is needed to avoid creating white pixels around the very beginning and end of an erased line
    grid_size_x = int(c.maze_width / c.number_of_vertical_lines)
    grid_size_y = int(c.maze_height / c.number_of_horizontal_lines)
    start_x_line = c.start_x + grid_size_x * current_cell_x  # start x position of the current cell
    start_y_line = c.start_y + grid_size_y * current_cell_y  # start y position of the current cell

    if direction == 'N':
        pygame.draw.line(screen, c.WHITE, (start_x_line + offset, start_y_line),
                         (start_x_line + grid_size_x - offset, start_y_line))
    elif direction == 'E':
        pygame.draw.line(screen, c.WHITE, (start_x_line + grid_size_x, start_y_line + offset),
                         (start_x_line + grid_size_x, start_y_line + grid_size_y - offset))
    elif direction == 'S':
        pygame.draw.line(screen, c.WHITE, (start_x_line + offset, start_y_line + grid_size_y),
                         (start_x_line + grid_size_x - offset, start_y_line + grid_size_y))
    else:
        pygame.draw.line(screen, c.WHITE, (start_x_line, start_y_line + offset),
                         (start_x_line, start_y_line + grid_size_y - offset))

    pygame.display.update()
