# lines for the grid
number_of_horizontal_lines = 20
number_of_vertical_lines = 20

# dimensions for the game screen
canvas_width = 600
canvas_height = 700

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

maze_width = 500
maze_height = 500

# the offsets needed to place the maze in the very middle of the game screen
margin_width = int((canvas_width - maze_width) / 2)
margin_height = int((canvas_height - maze_height) / 4) # want the maze closer to the upper screen
start_x = margin_width
start_y = margin_height

# Maximum frames per second
frames_rb = 150
frames_prim = 150

# buttons
text_rb = "Recursive backtracking"
text_prim = "Prims"
button_width = int(maze_width / 5)  # button width have to be at least button_width < maze_width / 3
button_height = int((canvas_height - start_y - maze_height) / 10) + 20
button_offset_x = int((maze_width - button_width * 2) / 3)
button_offset_y = int((canvas_height - start_y - maze_height) / 3)
button_start_x = start_x + button_offset_x
button_start_y = start_y + button_offset_y + maze_height
