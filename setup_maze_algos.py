import constants as c
from algorithms.prims import prims
from algorithms.kruskal import kruskal
from algorithms.binary_tree import binary_tree
from algorithms.growing_tree import growing_tree
from algorithms.hunt_and_kill import hunt_and_kill
from algorithms.recursive_backtracking import recursive_backtracking
from algorithms.pathfinder.a_star import a_star
from algorithms.pathfinder.rb_pathfinder import rb_pathfinder


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
