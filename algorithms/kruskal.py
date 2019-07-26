import random
from .data_structure.union_find import union_find
import constants as c
import utils.draw_utils as du
from utils import algo_utils


def kruskal(screen, clock):
    maze_size = c.number_of_vertical_lines * c.number_of_horizontal_lines
    maze = union_find(maze_size)
    edge_list = initialize_edge_list()

    while edge_list:
        clock.tick(c.frames_kruskal)
        a, b, direction = edge_list[random.randint(0, len(edge_list) - 1)]
        if not maze.same(a, b):
            maze.unite(a, b)
            du.remove_line(screen, int(a / c.number_of_vertical_lines), a % c.number_of_vertical_lines, direction)
        else:
            edge_list.remove((a, b, direction))


def initialize_edge_list():
    edge_list = []
    for i in range(c.number_of_vertical_lines):
        for j in range(c.number_of_horizontal_lines):
            for (x, y, direction) in algo_utils.get_neighbours(i, j, True):
                cell_pos_flattened = i * c.number_of_vertical_lines + j
                adj_pos_flattened = x * c.number_of_vertical_lines + y
                edge_list.append((cell_pos_flattened, adj_pos_flattened, direction))
    return edge_list
