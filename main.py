import mazedrawer as md
from algorithms.prims import prims
from algorithms.binary_tree import binary_tree
from algorithms.hunt_and_kill import hunt_and_kill
from algorithms.recursive_backtracking import recursive_backtracking


def main():
    algorithms = {
        "Prims": prims,
        "RB": recursive_backtracking,
        "HAK": hunt_and_kill,
        "BT": binary_tree
    }
    md.MazeDrawer(algorithms).start_game_loop()


if __name__ == '__main__':
    main()
