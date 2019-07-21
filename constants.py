# lines for the grid
number_of_horizontal_lines = 20
number_of_vertical_lines = 20

# dimensions for the game screen
height = 600
width = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

maze_width = 500
maze_height = 500

# the offsets needed to place the maze in the very middle of the game screen
margin_width = int((width - maze_width) / 2)
margin_height = int((height - maze_height) / 2)
start_x = 0 + margin_width
start_y = 0 + margin_height

# Maximum frames per second
frames_rb = 150
frames_prim = 400
