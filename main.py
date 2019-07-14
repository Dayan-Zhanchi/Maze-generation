import cell as ce
import constants as c
import mazedrawer as md
from recursive_backtracking import recursive_backtracking


def main():
    grid = [[ce.Cell((i, j), get_neighbours(i, j)) for j in range(c.number_of_vertical_lines)] for i in range(c.number_of_horizontal_lines)]
    md.MazeDrawer(recursive_backtracking).start_game_loop(grid)


def get_neighbours(x, y):
    neighbours = []
    north_cell = y - 1
    east_cell = x + 1
    south_cell = y + 1
    west_cell = x - 1

    if north_cell >= 0:
        neighbours.append((x, north_cell, 'N'))
    if east_cell < c.number_of_vertical_lines:
        neighbours.append((east_cell, y, 'E'))
    if south_cell < c.number_of_horizontal_lines:
        neighbours.append((x, south_cell, 'S'))
    if west_cell >= 0:
        neighbours.append((west_cell, y, 'W'))

    return neighbours


if __name__ == '__main__':
    main()
