# Maze-generation
Maze generation using different [maze algorithms](https://en.wikipedia.org/wiki/Maze_generation_algorithm).
Pygame was used to visualize the process.

### List of maze algorithms progression
- [x] Recursive backtracking 
- [x] Prims 
- [ ] Hunt and kill
- [ ] Kruskal 
- [ ] Binary tree 
- [ ] Recrusive division

### How to run
Download Pygame if you don't already have it:


    pip install pygame


To start the screen run the following command:


    py main.py


When the screen appears with a 2D grid, press either button to start the maze generation. To generate a new maze simply
click either buttons again when the current generation has finished. The different buttons represent the different algorithms.


You can also press p for activating prims algorithm or r for recursive backtracking.


To exit simply click on the x on the upper right corner of the screen.

### Maze generation with recursive backtracking
![Maze generation visualization RB](./assets/RB%20maze%20generation.gif)


### Maze generation with Prims algorithm
![Maze generation visualization Prims](./assets/prims%20maze%20generation.gif)
