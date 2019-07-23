import mazedrawer as md
from algorithms.prims import prims
from algorithms.recursive_backtracking import recursive_backtracking
from algorithms.hunt_and_kill import hunt_and_kill


def main():
    algortims = {
        "Prims": prims,
        "RB": recursive_backtracking,
        "HAK": hunt_and_kill
    }
    md.MazeDrawer(algortims).start_game_loop()


if __name__ == '__main__':
    main()
