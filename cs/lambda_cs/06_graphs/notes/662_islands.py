"""
Takes a 2D binary array and returns the number of 1 islands.
An island consists of 1s that are connected to the north, south, east or west.

For example:

```py
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4
```

* Islands consist of Connected components
* Connected neighbors (edges)
* Directions: nsew (edges)
* 2D array: graph
* Returns (shape of solution) number of islands
"""


"""
Each point can be represented by a tuple of its index location
i.e. (1, 3)
"""


def get_neighbors(node: tuple):
    """How to write a get_neighbors function for this shape?
    * Offset coordinates

    In order to get neighbors in directions:

    * south: first index +1, second index same
    * north: first index -1, second index same
    * west : first index same, second index -1
    * east : first index same, second index +1
    """
    neighbors = {
        "south": (node[0] + 1, node[1]),
        "north": (node[0] - 1, node[1]),
        "west": (node[0], node[1] - 1),
        "east": (node[0], node[1] + 1),
    }
    return neighbors


# The visited can be a set that holds the index location
# i.e. {(0, 0), (0, 1)}
visited = ()


def island_counter(matrix):
    pass


# How to find extent of island?
# Either of traversals (BFT, DFT) to find all nodes in island

# How to explore the larger set?
# Loop through and call traversal if find and unvisited 1
