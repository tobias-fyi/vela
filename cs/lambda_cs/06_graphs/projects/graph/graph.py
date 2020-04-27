"""
Simple graph implementation
"""

from util import Stack, Queue  # These may come in handy


class Graph:
    def __init__(self):
        """Represent a graph as a dictionary of vertices mapping labels to edges."""
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """Add a vertex to the graph."""
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """Add a directed edge to the graph, from v1 to v2."""
        # Check if exist
        if v1 in self.vertices and v2 in self.vertices:
            # add the edge
            self.vertices[v1].add(v2)
        else:
            print(f"Error: Vertex not found")

    def get_neighbors(self, vertex_id):
        """Get all neighbors (edges) of a vertex."""
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a q and n q starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create set of traversed vertices
        visited = set()
        while qq.size() > 0:  # While queue is not empty
            path = qq.dequeue()  # Dequeue first vertex
            if path[-1] not in visited:
                print(path[-1])  # DO THE THANG
                visited.add(path[-1])  # Mark as visited
                # Enqueue all neighbors
                for ngbr in self.get_neighbors(path[-1]):
                    new_path = path + [ngbr]
                    qq.enqueue(new_path)

    def dft(self, starting_vertex):
        """Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create stack and push starting vertex
        stack = Stack()
        stack.push([starting_vertex])
        # Create set of traversed vertices
        visited = set()
        while stack.size() > 0:
            path = stack.pop()  # Pop first vertex
            # If not in traversed
            if path[-1] not in visited:
                print(path[-1])  # DO THE THANG
                visited.add(path[-1])  # Mark as visited
                # Push all neighbors
                for ngbr in self.get_neighbors(path[-1]):
                    new_path = path + [ngbr]
                    stack.push(new_path)

    def dft_recursive(self, starting_vertex, visited=None):
        """Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        # Base case: vertex has been visited
        if starting_vertex in visited:
            return
        visited.add(starting_vertex)
        print(starting_vertex)
        # Recursive case: call self on neighbors
        for ngbr in self.get_neighbors(starting_vertex):
            self.dft_recursive(ngbr, visited)

    def bfs(self, starting_vertex, dst_vertex):
        """Return a list containing the shortest path from
        starting_vertex to dst_vertex in breath-first order.
        """
        # Create a q and n q starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create set of traversed vertices
        visited = set()
        while qq.size() > 0:  # While queue is not empty
            path = qq.dequeue()  # Dequeue first vertex
            if path[-1] == dst_vertex:  # If last node in path is dest
                # Return full path and stop function execution
                return path
            elif path[-1] not in visited:
                visited.add(path[-1])  # Mark as visited
                # Enqueue all neighbors
                for ngbr in self.get_neighbors(path[-1]):
                    new_path = path + [ngbr]
                    qq.enqueue(new_path)

    def dfs(self, starting_vertex, dst_vertex):
        """Return a list containing a path from
        starting_vertex to dst_vertex in depth-first order.
        """
        # Create stack and push starting vertex
        stack = Stack()
        stack.push([starting_vertex])
        # Create set of traversed vertices
        visited = set()
        while stack.size() > 0:
            path = stack.pop()  # Pop first vertex
            if path[-1] == dst_vertex:  # If last node in path is dest
                # Return full path and stop function execution
                return path
            if path[-1] not in visited:
                visited.add(path[-1])  # Mark as visited
                # Push all neighbors
                for ngbr in self.get_neighbors(path[-1]):
                    new_path = path + [ngbr]
                    stack.push(new_path)

    def dfs_recursive(self, start, dst, path=None, visited=None):
        """Return a list containing a path from
        path to destination vertex in depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:  # No path the first function call
            path = [start]
        # Base case (ultimate): vertex is the destination
        if path[-1] == dst:  # If last node in path is dst, then...
            return path  # Return the path — goes back down call stack
        # Base case (intermediate): if visited, return None
        if path[-1] in visited:
            return None
        visited.add(path[-1])  # If not visited or dst, add to visited
        # Recursive case: call self on neighbors
        for ngbr in self.get_neighbors(path[-1]):
            if ngbr not in visited:  # Check if neighbor has been visited
                result = self.dfs_recursive(ngbr, dst, path + [ngbr], visited)
                # If the result contains the path variable, return it
                if result is not None:
                    return result


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    print(graph.vertices)

    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """
    graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    graph.dft(1)
    graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
