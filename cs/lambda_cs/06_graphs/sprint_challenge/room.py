"""
Graphs — Sprint Challenge :: Room

A class to hold room information: name and description attributes.
"""

from __future__ import annotations

from player import Player


class Room:
    def __init__(
        self, name: str, description: str, id: int = 0, x: int = None, y: int = None
    ):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y

    def __str__(self):
        return f"\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.get_exits_string()}\n"

    def print_room_description(self, player: Player) -> None:
        print(str(self))

    def get_exits(self) -> list:
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.w_to is not None:
            exits.append("w")
        if self.e_to is not None:
            exits.append("e")
        return exits

    def get_exits_string(self) -> str:
        return f"Exits: [{', '.join(self.get_exits())}]"

    def connect_rooms(self, direction: str, connecting_room: Room) -> None:
        if direction == "n":
            self.n_to = connecting_room
            connecting_room.s_to = self
        elif direction == "s":
            self.s_to = connecting_room
            connecting_room.n_to = self
        elif direction == "e":
            self.e_to = connecting_room
            connecting_room.w_to = self
        elif direction == "w":
            self.w_to = connecting_room
            connecting_room.e_to = self
        else:
            print("INVALID ROOM CONNECTION")
            return None

    def get_room_in_direction(self, direction: str) -> Room:
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    def get_coords(self) -> list:
        return [self.x, self.y]
