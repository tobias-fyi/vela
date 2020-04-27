"""
Graphs - Sprint Challenge :: Traversal graph
"""

import random

from util import Stack, Queue
from room import Room


class TraverseGraph:
    def __init__(self):
        """Represent a graph as a dictionary of rooms 
        mapping rooms and connections."""
        self.rooms = {}
        # Lookup for opposite directions
        self.opposites = {"n": "s", "s": "n", "w": "e", "e": "w"}

    def add_room(self, room: Room) -> None:
        """Add a room to the graph, including connections."""
        # Each room will have dict of neighbors — `direction: room.id`
        self.rooms[room.id] = {}
        # Set each of the available exits initially to not visited ("?")
        for exit in room.get_exits():
            self.rooms[room.id][exit] = "?"

    def add_next_room_to_graph(
        self, current_room: Room, next_room: Room, direction: str,
    ) -> None:
        """Visits room by setting prev room's direction
        to the destination room's id and vice versa."""
        # If next_room is not in the graph, add it
        if next_room.id not in self.rooms:
            self.add_room(next_room)
        # Set the previous room's direction value to next room's id
        self.rooms[current_room.id][direction] = next_room.id
        # And vice versa...
        opp_dir = self.opposites[direction]  # Find opposite direction
        # Set next room's id for current room
        self.rooms[next_room.id][opp_dir] = current_room.id

    def choose_random_direction(self, room: Room) -> str:
        """Chooses a random direction from room's available exits."""
        return random.choice(room.get_exits())

    def choose_unexplored_direction(self, room: Room) -> str:
        """Picks a random unexplored adjacent room (direction to it).
        Returns None if room has no unexplored adjacents."""
        unexplored = []
        if room.id in self.rooms and "?" in self.rooms[room.id].values():
            for exit_dir, room in self.rooms[room.id].items():
                if room == "?":
                    unexplored.append(exit_dir)

            return random.choice(unexplored)
        else:
            return None

    def has_unexplored(self, room: Room) -> str:
        """True if room has one or more unexplored adjacent rooms.
        Returns None if room has no unexplored adjacents."""
        if room.id in self.rooms and "?" in self.rooms[room.id].values():
            return True
        else:
            return False

    def get_adjacent(self, room: Room) -> dict:
        """Get all of a room's adjacent rooms."""
        if room.id in self.rooms:
            return self.rooms[room.id]
        else:
            return None

    def bft(self, start_room: Room) -> list:
        """Return list of moves that traverses entire graph."""
        pass
