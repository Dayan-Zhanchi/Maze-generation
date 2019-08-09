# lines for the grid
number_of_horizontal_lines = 20
number_of_vertical_lines = 20

# dimensions for the game screen
canvas_width = 600
canvas_height = 900

maze_width = 500
maze_height = 500

# the offsets needed to place the maze in the very middle of the game screen
margin_width = int((canvas_width - maze_width) / 2)
# the bigger the denominator number is for the height the closer the maze is to the upper screen
margin_height = int((canvas_height - maze_height) / 6)
start_x = margin_width
start_y = margin_height

# offset is needed to avoid creating white pixels around the very beginning and end of an erased line
offset = 1
grid_size_x = int(maze_width / number_of_vertical_lines)
grid_size_y = int(maze_height / number_of_horizontal_lines)
