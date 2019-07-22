import mazedrawer as md
from prims import prims
from recursive_backtracking import recursive_backtracking


def main():
    algortims = {
        "Prims": prims,
        "Recursive backtracking": recursive_backtracking
    }
    md.MazeDrawer(algortims).start_game_loop()


if __name__ == '__main__':
    main()
