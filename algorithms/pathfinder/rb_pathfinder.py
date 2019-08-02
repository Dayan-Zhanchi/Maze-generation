import constants as c
import utils.draw_utils as du
from utils import algo_utils


def rb_pathfinder(screen, clock, maze):
    visited = [[0 for _ in range(c.number_of_vertical_lines)] for _ in range(c.number_of_horizontal_lines)]
    x, y = 0, 0
    current_cell = maze[x][y]
    """
        Ugly solution but always need to add double the cell to be able to erase color of a cell that we eventually backtrack to.
        In essence the problem is when we pop an unvisited cell from the stack, fill it with a color (since it's
        unvisited) and then add more unvisited cells from it, and finally backtrack back to it, then we will
        have lost the reference to it (we plopped it from the stack earlier and since it's now visited we will never add it back
        because we always get unvisited neighbours from a given cell) and ultimately can't erase the color. This problem 
        gives rise to multiple colored cells sporadically distributed outside of the original path. If we instead
        put 2 identical cell of a cell each time we put a cell, then at the second iteration we will be able to erase
        the color of the cell. This modification will not affect the normal execution (cases where this doesn't happen),
        it will however only lead to more unnecessary backtracking.
    """
    stack = [current_cell, current_cell]
    while True:
        clock.tick(c.frames_rb_pathfinder)
        neighbours = algo_utils.get_unvisited_neighbours(current_cell.neighbours, visited)
        if not visited[current_cell.x][current_cell.y]:
            du.color_cell_with_update(screen, c.GREEN, current_cell.x, current_cell.y)
            if current_cell.x == c.number_of_vertical_lines - 1 and current_cell.y == c.number_of_horizontal_lines - 1: break
        visited[current_cell.x][current_cell.y] = True

        if neighbours:
            # mark the current cell
            # stack.append(current_cell)
            for n in neighbours:
                next_cell_x, next_cell_y = n
                next_cell = maze[next_cell_x][next_cell_y]
                if next_cell not in stack:
                    stack.append(next_cell)
                    stack.append(next_cell)
                current_cell = next_cell
        elif not neighbours and stack:
            # reached a dead end so we backtrack, the stack keeps track of previous cells
            # make sure to color the current cell white before backtracking indicating we are turning back
            current_cell = stack.pop()
            du.color_cell_with_update(screen, c.WHITE, current_cell.x, current_cell.y)
