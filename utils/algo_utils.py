import random
import constants as c


def get_random_cell(unvisited_neighbours):
    if len(unvisited_neighbours) > 1:
        return unvisited_neighbours[random.randint(0, len(unvisited_neighbours) - 1)]
    return unvisited_neighbours[0]


def get_unvisited_neighbours(neighbours, visited):
    unvisited_neighbours = []
    for neighbour in neighbours:
        x, y = neighbour[0], neighbour[1]
        if not visited[x][y]:
            unvisited_neighbours.append(neighbour)
    return unvisited_neighbours


def get_neighbours(x, y, direction):
    neighbours = []
    north_cell = y - 1
    east_cell = x + 1
    south_cell = y + 1
    west_cell = x - 1

    if north_cell >= 0:
        if direction:
            neighbours.append((x, north_cell, 'N'))
        else:
            neighbours.append((x, north_cell))
    if east_cell < c.number_of_vertical_lines:
        if direction:
            neighbours.append((east_cell, y, 'E'))
        else:
            neighbours.append((east_cell, y))
    if south_cell < c.number_of_horizontal_lines:
        if direction:
            neighbours.append((x, south_cell, 'S'))
        else:
            neighbours.append((x, south_cell))
    if west_cell >= 0:
        if direction:
            neighbours.append((west_cell, y, 'W'))
        else:
            neighbours.append((west_cell, y))

    return neighbours
