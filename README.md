# Maze-generation
Maze generation using different [maze algorithms](https://en.wikipedia.org/wiki/Maze_generation_algorithm).
Pygame was used to visualize the process.

### List of maze algorithms progression
- [x] Recursive backtracking 
- [x] Prims 
- [x] Hunt and kill
- [ ] Kruskal 
- [ ] Binary tree 
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
| `r` | Run recursive backtracking |
| `h` | Run hunt and kill|
| `esc` | Exit |


### Maze generation with recursive backtracking
![Maze generation visualization RB](./assets/RB%20maze%20generation.gif)


### Maze generation with Prims 
![Maze generation visualization Prims](./assets/prims%20maze%20generation.gif)

### Maze generation with hunt and kill
![Maze generation visualization hunt and kill](./assets/hak%20generation.gif)
