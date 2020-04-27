"""
Graphs — Sprint Challenge :: Adventure!
"""

from ast import literal_eval
from collections import deque  # To test out different queue
import os
import random

from traverse_graph import TraverseGraph
from player import Player
from room import Room
from util import Queue, Stack
from world import World

# === Load world === #
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
file_path = "06_graphs/sprint_challenge/"
# map_path = "maps/test_line.txt"
# map_path = "maps/test_cross.txt"
# map_path = "maps/test_loop.txt"
# map_path = "maps/test_loop_fork.txt"
map_path = "maps/main_maze.txt"

# Path constructor for debugger (Uncomment when using vscode debugger)
# map_path = os.path.join(file_path, map_path)

# === Loads the map into a dictionary === #
room_graph = literal_eval(open(map_path, "r").read())
world.load_graph(room_graph)

# === Print an ASCII map === #
world.print_rooms()

player = Player(world.starting_room)


# ====== Populate the Traversal Graph ====== #
def traverse_room_graph(player: Player) -> list:
    tg = TraverseGraph()
    stack = Stack()
    traversal_path = []  # List to be returned

    # Starting room
    player.current_room = world.starting_room
    # Add starting room to graph
    tg.add_room(player.current_room)

    while len(tg.rooms) < len(room_graph):
        # Keep track of if player moves this iteration
        travel = False
        # If room has unexplored, go to unexplored
        # Choose the first available unexplored neighbor
        for exit_dir, room in tg.rooms[player.current_room.id].items():
            if room == "?":
                # Get next Room object
                next_room = getattr(player.current_room, f"{exit_dir}_to")
                # Add room to graph
                tg.add_next_room_to_graph(player.current_room, next_room, exit_dir)

                # Push direction onto stack and set previous
                stack.push(exit_dir)
                traversal_path.append(exit_dir)

                # Move in that exit_dir
                player.travel(exit_dir)
                # Indicate that travel happened
                travel = True
                # Go back to step #2 and repeat the process
                break  # AKA: break out of inner for loop

        if not travel:  # No travel this iteration
            # Backtrack to last unexplored room
            # Start going back up the stack in the opposite direction
            exit_dir = tg.opposites[stack.pop()]
            traversal_path.append(exit_dir)  # Append the opposite direction as well
            player.travel(exit_dir)

        # TODO: if no unexplored adjacent rooms, but has more than one option
        # Choose random direction

    # TODO: Now that graph is populated, use it to find shorter path

    return traversal_path


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = traverse_room_graph(player)

# === Traversal Test === #
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
