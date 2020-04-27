        # edges
        edges = self.get_neighbors(starting_vertex)

        if visited is None:
            # instantiate empty set for visited 
            visited = set()
        
        if path is None:
            # instantiate empty list for path
            path = []

        # mark current vertex as visited
        visited.add(starting_vertex)

        # defining path
        path = path + [starting_vertex]

        # when destination found, return path
        if starting_vertex == destination_vertex:
            return path

        # our base case is if we found the destination vertex,
        # so it will recurse and will define the new_path
        for edge in edges:
            if edge not in visited:
                new_path = self.dfs_recursive(edge, destination_vertex, visited, path)
                if new_path:
                    return new_path

        # return None if path does not exist
        return None