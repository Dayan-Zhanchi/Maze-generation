import random
import constants as c


# TODO: Refactor entire file to use inheritance
def get_random_cell(cells):
    if len(cells) > 1:
        return cells[random.randint(0, len(cells) - 1)]
    return cells[0]


def get_unvisited_neighbours(neighbours, visited):
    unvisited_neighbours = []
    for neighbour in neighbours:
        x, y = neighbour[0], neighbour[1]
        if not visited[x][y]:
            unvisited_neighbours.append(neighbour)
    return unvisited_neighbours


def get_neighbours(x, y, retrieve_direction):
    neighbours = []
    north_cell = y - 1
    east_cell = x + 1
    south_cell = y + 1
    west_cell = x - 1

    if north_cell >= 0:
        if retrieve_direction:
            neighbours.append((x, north_cell, 'N'))
        else:
            neighbours.append((x, north_cell))
    if east_cell < c.number_of_vertical_lines:
        if retrieve_direction:
            neighbours.append((east_cell, y, 'E'))
        else:
            neighbours.append((east_cell, y))
    if south_cell < c.number_of_horizontal_lines:
        if retrieve_direction:
            neighbours.append((x, south_cell, 'S'))
        else:
            neighbours.append((x, south_cell))
    if west_cell >= 0:
        if retrieve_direction:
            neighbours.append((west_cell, y, 'W'))
        else:
            neighbours.append((west_cell, y))

    return neighbours


# Get the direction of a randomly selected visited adjacent cell
# x and y coord is for an unvisited cell
def get_random_adj_cell_direction(x, y, visited):
    adj_cells = get_neighbours(x, y, True)
    adj_cell_direction = []
    for (x, y, direction) in adj_cells:
        if visited[x][y] != 0:
            adj_cell_direction.append(direction)
    return adj_cell_direction[random.randint(0, len(adj_cell_direction) - 1)]
