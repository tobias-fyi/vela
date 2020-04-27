"""
Graphs :: Day 2 Project
"""

import sys
import os

sys.path.append(os.path.abspath("../graph"))
from graph import Graph


def earliest_ancestor(ancestors: list, starting_node: int) -> int:
    # === Instantiate graph === #
    graph = Graph()
    for rel in ancestors:  # Loop through input to add all vertices
        # === Unpack tuple for readability: (parent, child) === #
        parent, child = rel
        # === Add vertices to graph if needed === #
        if parent not in graph.vertices:  # Check if parent exists
            graph.add_vertex(parent)  # If not, add it
        if child not in graph.vertices:  # Check if child exists
            graph.add_vertex(child)  # If not, add it
        # === Add the edge between child -> parent === #
        # This relation b/c direction of search is child -> parent
        graph.add_edge(child, parent)
    # === Once graph is built, search! === #
    if len(graph.vertices[starting_node]) < 1:
        return -1  # If vertex has no parent, return -1
    # Otherwise, bft returns the furthest connected node from start
    return graph.bft(starting_node)


if __name__ == "__main__":
    # === Give 'er a little test
    test_ancestors = [
        (1, 3),
        (2, 3),
        (3, 6),
        (5, 6),
        (5, 7),
        (4, 5),
        (4, 8),
        (8, 9),
        (11, 8),
        (10, 1),
    ]
    earliest_ancestor(test_ancestors, 2)
    earliest_ancestor(test_ancestors, 6)
