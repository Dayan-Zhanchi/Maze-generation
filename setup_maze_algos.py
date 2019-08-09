from constants import pathfinder_consts
from constants import button_consts
from algorithms.binary_tree import binary_tree
from algorithms.growing_tree import growing_tree
from algorithms.hunt_and_kill import hunt_and_kill
from algorithms.kruskal import kruskal
from algorithms.prims import prims
from algorithms.recursive_backtracking import recursive_backtracking
from algorithms.pathfinder.a_star import a_star
from algorithms.pathfinder.rb_pathfinder import rb_pathfinder


def create_mappings_for_generation_algos():
    algorithms = {
        button_consts.text_prim: prims,
        button_consts.text_rb: recursive_backtracking,
        button_consts.text_hunt_and_kill: hunt_and_kill,
        button_consts.text_binary_tree: binary_tree,
        button_consts.text_growing_tree: growing_tree,
        button_consts.text_kurskal: kruskal
    }
    return algorithms


def create_mappings_for_pathfinder_algos():
    pathfinders = {
        pathfinder_consts.text_pathfinder_a_star: a_star,
        pathfinder_consts.text_pathfinder_rb: rb_pathfinder
    }
    return pathfinders
