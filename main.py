import mazedrawer as md
from algorithms.prims import prims
from algorithms.recursive_backtracking import recursive_backtracking


def main():
    algortims = {
        "Prims": prims,
        "RB": recursive_backtracking
    }
    md.MazeDrawer(algortims).start_game_loop()


if __name__ == '__main__':
    main()
