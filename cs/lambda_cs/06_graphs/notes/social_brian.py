"""
Graphs :: Day 3 - Social network graph
"""

import os
import random
import sys

sys.path.append(os.path.abspath("../projects/graph"))
from util import Stack, Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id: int, friend_id: int) -> bool:
        """Creates a bi-directional friendship."""
        if user_id == friend_id:
            # You cannot be friends with yourself
            return False
        elif (
            friend_id in self.friendships[user_id]
            or user_id in self.friendships[friend_id]
        ):
            # Friendship already exists
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name: str) -> None:
        """Create a new user with a sequential integer ID."""
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users: int, avg_friendships: int) -> None:
        """Takes a number of users and an average number of friendships
        as arguments. Creates that number of users and a randomly
        distributed friendships between those users.

        The number of users must be greater than the average number of friendships.
        """
        # === Reset graph === #
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # === Add users === #
        # Use add_user num_user times
        for i in range(num_users):
            self.add_user(f"user_{i}")

        # === New / improved friendship method === #
        # Randomly generate friendships, keep new / rejecting dupes
        # Until we get to number we need (num_users * avg_friendships / 2)

        # Keep track of good friendships and collisions
        target_friendships = num_users * avg_friendships // 2
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship(user_id, friend_id):
                total_friendships += 1  # 1 b/c doubling is dealt with above (// 2)
            else:
                collisions += 1

        print(f"{collisions} collisions")

        # === Old friendship method === #
        # # === Create friendships === #
        # # Generate all friendship combinations
        # poss_frenship = []

        # # Avoid dupes my making first number smaller than second
        # for user_id in self.users:
        #     for friend_id in range(user_id + 1, self.last_id + 1):
        #         poss_frenship.append((user_id, friend_id))

        # # Shuffle all possible friendships
        # random.shuffle(poss_frenship)

        # # Create for first X pairs - X is total // 2
        # for i in range(num_users * avg_friendships // 2):
        #     frenship = poss_frenship[i]
        #     self.add_friendship(frenship[0], frenship[1])

    def get_all_social_paths(self, user_id: int) -> dict:
        """Takes a user's user_id as an argument; returns a dictionary
        containing every user in that user's extended network with the
        shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}

        # Shortest - tells us breadth first
        # Extended network - traversal, connected component

        # Planning
        # How to build the graph? Already done
        # Start at given user id, return the path to each friend

        # Traversal
        # Create queue
        qq = Queue()
        # Enqueue path
        qq.enqueue([user_id])
        # While queue not empty
        while qq.size() > 0:
            # Dequeue first path
            path = qq.dequeue()
            vertex = path[-1]
            # If not visited
            if vertex not in visited:
                # Add path to visited (DO THE THANG)
                visited[vertex] = path
                # For each friend
                for friend in self.friendships[vertex]:
                    # Copy path and enqueue
                    qq.enqueue(path + [friend])

        return visited


if __name__ == "__main__":
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
    # === Average path length === #
    degrees = []
    for conn in connections:
        degrees.append(len(connections[conn]))

    avg_degree = sum(degrees) / len(connections)
    print(f"Average degree of separation between user_{user_id} and their network:")
    print(f"-> {avg_degree}")

    sg3 = SocialGraph()
    sg3.populate_graph(1000, 5)
    print("Total friendships:", len(sg3.friendships))

    user_id = 500
    conn3 = sg3.get_all_social_paths(user_id=user_id)
    print(f"Total connections for user_{user_id}:", len(conn3))
    print(
        f"or user_{user_id} knows {len(conn3) / len(sg3.friendships) * 100}% of users"
    )
    # >>> 99.0%

    # === Average path length === #
    degrees = []
    for conn in conn3:
        degrees.append(len(conn3[conn]))

    avg_degree = sum(degrees) / len(conn3)
    print(f"Average degree of separation between user_{user_id} and their network:")
    print(f"-> {avg_degree}")

    user_id = 28
    conn3 = sg3.get_all_social_paths(user_id=user_id)
    print(f"Total connections for {user_id}:", len(conn3))
    print(
        f"or user_{user_id} knows {len(conn3) / len(sg3.friendships) * 100}% of users"
    )
    # >>> 99.0%

    # === Average path length === #
    degrees = []
    for conn in conn3:
        degrees.append(len(conn3[conn]))

    avg_degree = sum(degrees) / len(conn3)
    print(f"Average degree of separation between user_{user_id} and their network:")
    print(f"-> {avg_degree}")

    # === Test with even larger sample size === #
    sg4 = SocialGraph()
    sg4.populate_graph(1000, 10)
    print("Total friendships:", len(sg4.friendships))

    user_id = 500
    conn4 = sg4.get_all_social_paths(user_id=user_id)
    print(f"Total connections for user_{user_id}:", len(conn4))
    print(
        f"or user_{user_id} knows {len(conn4) / len(sg4.friendships) * 100}% of users"
    )
    # >>> 99.1%

    user_id = 28
    conn4 = sg4.get_all_social_paths(user_id=user_id)
    print(f"Total connections for {user_id}:", len(conn4))
    print(
        f"or user_{user_id} knows {len(conn4) / len(sg4.friendships) * 100}% of users"
    )
    # >>> 99.1%

    # === Average path length === #
    degrees = []
    for conn in conn4:
        degrees.append(len(conn4[conn]))

    avg_degree = sum(degrees) / len(conn4)
    print(f"Average degree of separation between user_{user_id} and their network:")
    print(f"-> {avg_degree}")
