import random
import constants as c
import utils.draw_utils as du
from utils.alg_util import get_neighbours

def kruskal(screen, clock):
    maze_size = c.number_of_vertical_lines * c.number_of_horizontal_lines
    maze = UnionFind(maze_size)
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
            for (x, y, direction) in get_neighbours(i, j):
                cell_pos_flattened = i * c.number_of_vertical_lines + j
                adj_pos_flattened = x * c.number_of_vertical_lines + y
                edge_list.append((cell_pos_flattened, adj_pos_flattened, direction))
    return edge_list


"""
    Implemented as described by Antii Laaksonen in Competitive programmer's handbook 2018
    can be found on page 146
"""


class UnionFind:

    def __init__(self, n):
        self.link = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        while x != self.link[x]:
            x = self.link[x]
        return x

    def same(self, a, b):
        return self.find(a) == self.find(b)

    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if self.size[a] < self.size[b]:
            a, b = self.__swap(a, b)
        self.size[a] += self.size[b]
        self.link[b] = a

    @staticmethod
    def __swap(a, b):
        c = a
        a = b
        b = c
        return a, b
