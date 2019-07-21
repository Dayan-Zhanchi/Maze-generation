import cell as ce
import constants as c
from prims import prims
import mazedrawer as md
from utils import get_neighbours
from recursive_backtracking import recursive_backtracking


def main():
    #grid_rb = [[ce.Cell((i, j), get_neighbours(i, j, True)) for j in range(c.number_of_vertical_lines)] for i in range(c.number_of_horizontal_lines)]
    grid_p = [[ce.Cell((i, j), get_neighbours(i, j, False)) for j in range(c.number_of_vertical_lines)] for i in range(c.number_of_horizontal_lines)]
    #md.MazeDrawer(recursive_backtracking).start_game_loop(grid_rb)
    md.MazeDrawer(prims).start_game_loop(grid_p)


if __name__ == '__main__':
    main()
