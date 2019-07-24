# Maze-generation
Maze generation using different [maze algorithms](https://en.wikipedia.org/wiki/Maze_generation_algorithm). A very good resource with
in depth explanations and also visualizations can be found [here](http://weblog.jamisbuck.org/2011/2/7/maze-generation-algorithm-recap).
However, I created my own visualizations and went with my own interpretations of the maze algorithms. Pygame was used to visualize the process.

### List of maze algorithms progression
- [x] Recursive backtracking 
- [x] Prims 
- [x] Hunt and kill
- [ ] Kruskal 
- [x] Binary tree 
- [ ] Recursive division

### How to run
Download the packages in the requirements file:


    pip install -r requirements.txt


To start the screen run the following command:


    py main.py


When the screen appears with a 2D grid, press either button to start the maze generation. To generate a new maze simply
click either buttons again when the current generation has finished. The different buttons represent the different algorithms.


### Commands
You can also use commands to start the generation or exit the screen.


| Command | Description |
| ------- | ----------- |
| `p` | Run Prims algorithm |
| `r` | Run Recursive backtracking |
| `h` | Run Hunt and kill |
| `b` | Run Binary tree |
| `esc` | Exit |


### Recursive backtracking
![Maze generation visualization RB](./assets/RB%20maze%20generation.gif)

### Prims 
![Maze generation visualization Prims](./assets/prims%20maze%20generation.gif)

### Hunt and kill
![Maze generation visualization hunt and kill](./assets/hak%20generation.gif)

### Binary tree
![Maze generation visualization binary tree](./assets/BT%20generation.gif)