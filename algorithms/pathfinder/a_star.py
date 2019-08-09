import queue
from itertools import count

from constants import dimension_consts as c, dimension_consts
from constants import frame_consts
from constants import color_consts
import utils.draw_utils as du
from utils.alg_util import get_unvisited_neighbours

start_x, start_y = 0, 0
goal_x, goal_y = 19, 19


def a_star(screen, clock, maze):
    distances = [[0 for _ in range(c.number_of_vertical_lines)] for _ in range(c.number_of_horizontal_lines)]
    current = maze[start_x][start_y]
    came_from = {}
    q = queue.PriorityQueue()
    unique = count()
    q.put((0, next(unique), current))
    while not q.empty():
        clock.tick(frame_consts.frames_a_star_pathfinder)
        _, _, current = q.get()

        if (current.x, current.y) == (goal_x, goal_y): break

        for x, y in get_unvisited_neighbours(current, distances):
            new_cost = distances[current.x][current.y] + 1
            next_cell = maze[x][y]
            if distances[x][y] == 0 or new_cost < distances[x][y]:
                distances[x][y] = new_cost
                dist_to_goal = new_cost + heuristic_manhattan_dist(x, y)
                q.put((dist_to_goal, next(unique), next_cell))
                came_from[next_cell] = current

                du.color_cell_with_update(screen, color_consts.RED, x, y)

    path = construct_path(came_from, maze)
    display_path(screen, path)
    remove_wrong_paths(screen, path, came_from)


def heuristic_manhattan_dist(x, y):
    return abs(goal_x - x) + abs(goal_y - y)


def construct_path(came_from, maze):
    path = []
    current = (goal_x, goal_y)
    start = (start_x, start_y)
    while current != start:
        path.append(current)
        curr_x = current[0]
        curr_y = current[1]
        cell = came_from[maze[curr_x][curr_y]]
        current = (cell.x, cell.y)
    path.append(start)
    path.reverse()
    return path


def display_path(screen, path):
    for x, y in path:
        du.color_cell_with_update(screen, color_consts.GREEN, x, y)


def remove_wrong_paths(screen, path, came_from):
    for cell, _ in came_from.items():
        if (cell.x, cell.y) not in path:
            du.color_cell_with_update(screen, color_consts.WHITE, cell.x, cell.y)
