import constants as c
from algorithms.binary_tree import binary_tree
from algorithms.growing_tree import growing_tree
from algorithms.hunt_and_kill import hunt_and_kill
from algorithms.kruskal import kruskal
from algorithms.pathfinder.a_star import a_star
from algorithms.prims import prims
from algorithms.recursive_backtracking import recursive_backtracking


def create_mappings_for_generation_algos():
    algorithms = {
        c.text_prim: prims,
        c.text_rb: recursive_backtracking,
        c.text_hunt_and_kill: hunt_and_kill,
        c.text_binary_tree: binary_tree,
        c.text_growing_tree: growing_tree,
        c.text_kurskal: kruskal
    }
    return algorithms


def create_mappings_for_pathfinder_algos():
    return a_star
