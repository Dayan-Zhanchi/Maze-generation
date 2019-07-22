# lines for the grid
number_of_horizontal_lines = 20
number_of_vertical_lines = 20

# dimensions for the game screen
canvas_width = 600
canvas_height = 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

maze_width = 500
maze_height = 500

# the offsets needed to place the maze in the very middle of the game screen
margin_width = int((canvas_width - maze_width) / 2)
margin_height = int((canvas_height - maze_height) / 4)  # 4 because want the maze closer to the upper screen
start_x = margin_width
start_y = margin_height

# Maximum frames per second
frames_rb = 150
frames_prim = 150

# buttons
text_rb = "RB"
text_prim = "Prims"
text_hunt_and_kill = "HAK"
text_kurskal = "Kruskal"
text_binary_tree = "BT"
text_recursive_division = "RD"
button_width = int(maze_width / 6)  # button width have to be at least button_width < maze_width / 3
button_height = int((canvas_height - start_y - maze_height) / 10) + 20 # the 10 in the division is experimental, seems like a nice balance for the height of the button
button_offset_x = int((maze_width - button_width * 3) / 4)  # divide with 4 because there will be 4 offsets in total (since we have 3 buttons) and we want equal length for each offset
button_offset_y = int((canvas_height - start_y - maze_height) / 6)  # 6 is derived experimentally for a nice placement of the button beneath the maze
button_start_x = start_x + button_offset_x
button_start_y = start_y + button_offset_y + maze_height
