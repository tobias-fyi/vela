# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]

# island_counter(islands) # returns 4
# Keywords
# islands - they consist of connected components
# connected - the neighbors (edges)
# directions - north, south, east, west (edges)
# 2d array - the grap
# returns the number of islands

# How could we write a get neighbor function that uses this shape?
# Offset coordinates, pick a 1 that checks north south east west

# How can we find the extent of an island?
# Either traversal method to find all nodes in island

# How do I explore the larger set?
# Loop through and call a traversal if we find an unvisited 1

visited = [[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


def island_counter(islands, visited):
    num_islands = 0
    # iterate through the islands
    for y in range(0, len(islands)):
        for x in range(0, len(islands[y])):
            # if the island-node is part of an island and hasn't been visited
            if islands[y][x] == 1 and visited[y][x] == 0:
                # you've found an island, so increment
                num_islands += 1
                # BFT through the island-node's neighbors
                visited = visit_neighbors(x, y, islands, visited)
    return num_islands


def visit_neighbors(x, y, islands, visited):
    # NORTH
    if y > 0:  # if not at northern edge
        # and neighbor is an island-node that hasn't been visited
        if islands[y-1][x] == 1 and visited[y-1][x] == 0:
            # mark it visited
            visited[y-1][x] = 1
            # and visit all it's neighbors
            visited = visit_neighbors(x, y-1, islands, visited)

    # SOUTH
    if y < 4:
        if islands[y+1][x] == 1 and visited[y+1][x] == 0:
            visited[y+1][x] = 1
            visited = visit_neighbors(x, y+1, islands, visited)

    # EAST
    if x < 4:
        if islands[y][x+1] == 1 and visited[y][x+1] == 0:
            visited[y][x+1] = 1
            visited = visit_neighbors(x+1, y, islands, visited)

    # WEST
    if x > 0:
        if islands[y][x-1] == 1 and visited[y][x-1] == 0:
            visited[y][x-1] = 1
            visited = visit_neighbors(x-1, y, islands, visited)

    return visited


result = island_counter(islands, visited)

print(result)
