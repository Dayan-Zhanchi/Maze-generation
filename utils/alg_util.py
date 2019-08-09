from random import randint

from constants import dimension_consts as c


def get_random_cell(cells):
    if len(cells) > 1:
        return cells[randint(0, len(cells) - 1)]
    return cells[0]


# Get the direction of a randomly selected visited adjacent cell
# x and y coord is for an unvisited cell
def get_random_adj_cell_direction(cell, visited):
    adj_cells = get_neighbours(cell.x, cell.y)
    adj_cell_direction = []
    for (x, y, direction) in adj_cells:
        if visited[x][y] != 0:
            adj_cell_direction.append(direction)
    return adj_cell_direction[randint(0, len(adj_cell_direction) - 1)]


# append current cell and next cell to the neighbours of each other
def add_cell_to_walkable_path(current_cell, next_cell, path):
    if (next_cell.x, next_cell.y) not in path[current_cell.x][current_cell.y].neighbours:
        path[current_cell.x][current_cell.y].neighbours.append((next_cell.x, next_cell.y))
    if (current_cell.x, current_cell.y) not in path[next_cell.x][next_cell.y].neighbours:
        path[next_cell.x][next_cell.y].neighbours.append((current_cell.x, current_cell.y))


def get_neighbours(x, y):
    neighbours = []
    north_cell = y - 1
    east_cell = x + 1
    south_cell = y + 1
    west_cell = x - 1

    if north_cell >= 0:
        neighbours.append((x, north_cell, 'N'))
    if east_cell < c.number_of_vertical_lines:
        neighbours.append((east_cell, y, 'E'))
    if south_cell < c.number_of_horizontal_lines:
        neighbours.append((x, south_cell, 'S'))
    if west_cell >= 0:
        neighbours.append((west_cell, y, 'W'))

    return neighbours


def get_unvisited_neighbours(cell, visited):
    unvisited_neighbours = []
    for neighbour in cell.neighbours:
        x, y = neighbour[0], neighbour[1]
        if not visited[x][y]:
            unvisited_neighbours.append(neighbour)
    return unvisited_neighbours
