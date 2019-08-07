import constants as c


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
