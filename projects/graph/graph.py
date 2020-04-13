"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Cannot create edge on given vertices')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # make sure the vertex exists, otherwise spit error
        if self.vertices[vertex_id]:
            return self.vertices[vertex_id]
        else:
            raise IndexError('Vertex not found')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # instantiate queue
        q = Queue()
        # # put root node in queue
        q.enqueue(starting_vertex)
        # make a list for nodes visited
        visited = set()

        # Loop while there's something in the queue
        while q.size():
            # print('inside while loop')
            # Take the current node off the front of the queue
            node = q.dequeue()
        #     # print('made the node')
        #     # check visited list; if not there add to list, then add it's friends to queue
            if node not in visited:
                visited.add(node)
                print(node)
                for friend in self.get_neighbors(node):
                    # print('inside for neighbors loop')
                    if friend is not None:
                        q.enqueue(friend)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Instantiate stack
        stack = Stack()
        #drop starting point in stack
        stack.push(starting_vertex)
        #start a list for nodes visited
        visited = set()

        # Loop while there is something in the stack
        while stack.size():
            # pop what's on top
            c_node = stack.pop()
            # Check visited list ...
            if not c_node in visited:
                # if not there, add it to visited ...
                visited.add(c_node)
                print(c_node)
                # ... and add all the neighbor-friends to the stack
                for friend in self.vertices[c_node]:
                    stack.push(friend)


            # if not c_node in visited:
                
            #     visited.add(vertex)
            #     for vert in self.vertices[vertex]:
            #         stack.push(vert)



    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # If no set of visited exists, create one
        if visited == None:
            visited = set()
        # check visited list, if it's not there...
        if not starting_vertex in visited:
            # ... add it to the visited list
            visited.add(starting_vertex)
            print(starting_vertex)
            # do the recursion to all neighbors (friend vertices)
            for friend in self.vertices[starting_vertex]:
                self.dft_recursive(friend, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Instantiate queue
        q = Queue()
        # This time add the starting point as a list...
        q.enqueue([starting_vertex])
        # Start the visited set
        visited = set()

        #Loop while there is something in the queue
        while q.size():
            # Just like bft take what's at the front of the que. This time a path of nodes/vertices
            c_path = q.dequeue()
            # declare which is last in the path
            last = c_path[-1]
            # 
            if not last in visited:
                visited.add(last)
                # check to see if we've found the destination...
                if last == destination_vertex:
                    return c_path
                # ... if it's not the destination:
                for thing in self.get_neighbors(last):
                    copy = c_path.copy()
                    if not thing in copy:
                        copy.append(thing)
                    q.enqueue(copy)

        # # Loop while there's something in the queue
        # while q.size():
        #     # Take the current node off the front of the queue
        #     c_node = q.dequeue()
        #     # check visited list; if not there add to list, then add it's friends to queue
        #     if not c_node in visited:
        #         visited.add(c_node)
        #         for friend in self.vertices[c_node]:
        #             q.enqueue(friend)
        #         # for friend in self.vertices[last]:
                        #q.enqueue([*c_path, friend]) 


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Instantiate stack
        stack = Stack()
        # This time add the starting point as a list...
        stack.push([starting_vertex])
        # Start the visited set
        visited = set()

        #Loop while there is something in the queue
        while stack.size():
            # Just like bft take what's at the front of the que. This time a path of nodes/vertices
            c_path = stack.pop()
            # declare which is last in the path
            last = c_path[-1]
            # 
            if not last in visited:
                visited.add(last)
                # check to see if we've found the destination...
                if last == destination_vertex:
                    return c_path
                # ... if it's not the destination:
                for thing in self.get_neighbors(last):
                    copy = c_path.copy()
                    if not thing in copy:
                        copy.append(thing)
                    stack.push(copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path
        for friend in self.vertices[starting_vertex]:
            if friend not in visited:
                new_path = self.dfs_recursive(friend, destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None


if __name__ == '__main__':
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

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
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
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
