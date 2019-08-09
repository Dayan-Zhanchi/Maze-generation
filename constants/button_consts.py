from constants.dimension_consts import maze_width, canvas_height, start_y, maze_height, start_x

# buttons
text_rb = "RB"
text_prim = "Prims"
text_hunt_and_kill = "HAK"
text_kurskal = "Kruskal"
text_binary_tree = "BT"
text_recursive_division = "RD"
text_growing_tree = "GT"
button_width = int(maze_width / 6)
# the 10 in the division is experimental, seems like a nice balance for the height of the button
button_height = int((canvas_height - start_y - maze_height) / 10) + 20
# divide with 4 because there will be 4 offsets in total (since we have 3 buttons) and we want equal length for each offset
button_offset_x = int((maze_width - button_width * 3) / 4)
# the value of the denominator is derived experimentally for a nice placement of the button beneath the maze
button_offset_y = int((canvas_height - start_y - maze_height) / 6)
button_start_x = start_x + button_offset_x
button_start_y = start_y + button_offset_y + maze_height