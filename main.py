import mazedrawer as md
from algorithms.prims import prims
from algorithms.binary_tree import binary_tree
from algorithms.recursive_backtracking import recursive_backtracking
from algorithms.hunt_and_kill import hunt_and_kill
from algorithms.growing_tree import growing_tree
from algorithms.kruskal import kruskal
import constants as c

def main():
    algorithms = {
        c.text_prim: prims,
        c.text_rb: recursive_backtracking,
        c.text_hunt_and_kill: hunt_and_kill,
        c.text_binary_tree: binary_tree,
        c.text_growing_tree: growing_tree,
        c.text_kurskal: kruskal
    }
    md.MazeDrawer(algorithms).start_game_loop()


if __name__ == '__main__':
    main()
